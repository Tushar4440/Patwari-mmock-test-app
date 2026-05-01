from flask import Blueprint, request, jsonify
from models import db, MockTest, Question, TestAttempt, User
from ai_service import generate_mock_test_from_syllabus
import json

api = Blueprint('api', __name__)

@api.route('/upload_syllabus', methods=['POST'])
def upload_syllabus():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
        
    syllabus_text = "Extracted text from syllabus file."
    return jsonify({"message": "Syllabus uploaded successfully", "text_snippet": syllabus_text[:100]}), 200

@api.route('/generate_test', methods=['POST'])
def generate_test():
    data = request.json
    syllabus_text = data.get('syllabus_text', '')
    section = data.get('section', 'full')
    title = data.get('title', 'UKSSSC Mock Test')
    
    generated_questions = generate_mock_test_from_syllabus(syllabus_text, section)
    
    new_test = MockTest(title=title)
    db.session.add(new_test)
    db.session.commit()
    
    for q_data in generated_questions:
        q = Question(
            test_id=new_test.id,
            section=q_data['section'],
            text=q_data['text'],
            options=q_data['options'],
            correct_answer=q_data['correct_answer'],
            explanation=q_data['explanation']
        )
        db.session.add(q)
        
    db.session.commit()
    
    return jsonify({"message": "Test generated successfully", "test_id": new_test.id}), 201

@api.route('/tests', methods=['GET'])
def get_tests():
    tests = MockTest.query.all()
    result = [{"id": t.id, "title": t.title, "created_at": t.created_at} for t in tests]
    return jsonify(result), 200

@api.route('/tests/<int:test_id>', methods=['GET'])
def get_test(test_id):
    test = MockTest.query.get_or_404(test_id)
    questions = Question.query.filter_by(test_id=test_id).all()
    
    q_list = []
    for q in questions:
        q_list.append({
            "id": q.id,
            "section": q.section,
            "text": q.text,
            "options": json.loads(q.options)
        })
        
    return jsonify({"id": test.id, "title": test.title, "questions": q_list}), 200

@api.route('/submit_test', methods=['POST'])
def submit_test():
    data = request.json
    test_id = data.get('test_id')
    user_id = data.get('user_id', 1)
    answers = data.get('answers', {})
    
    test = MockTest.query.get_or_404(test_id)
    questions = Question.query.filter_by(test_id=test_id).all()
    
    score = 0
    total = len(questions)
    section_scores = {}
    
    review_data = []
    
    for q in questions:
        if q.section not in section_scores:
            section_scores[q.section] = {"score": 0, "total": 0}
            
        section_scores[q.section]["total"] += 1
        
        user_answer = answers.get(str(q.id))
        if user_answer == q.correct_answer:
            score += 1
            section_scores[q.section]["score"] += 1
            
        review_data.append({
            "id": q.id,
            "correct_answer": q.correct_answer,
            "explanation": q.explanation
        })
            
    user = User.query.get(user_id)
    if not user:
        user = User(id=user_id, username="Student")
        db.session.add(user)
        db.session.commit()
            
    attempt = TestAttempt(
        user_id=user_id,
        test_id=test_id,
        score=score,
        total_questions=total,
        section_scores=json.dumps(section_scores)
    )
    db.session.add(attempt)
    db.session.commit()
    
    return jsonify({
        "score": score,
        "total": total,
        "section_scores": section_scores,
        "review_data": review_data,
        "message": "Test submitted successfully"
    }), 200

@api.route('/analytics/<int:user_id>', methods=['GET'])
def get_analytics(user_id):
    attempts = TestAttempt.query.filter_by(user_id=user_id).order_by(TestAttempt.completed_at).all()
    
    history = []
    for a in attempts:
        history.append({
            "attempt_id": a.id,
            "test_id": a.test_id,
            "score": a.score,
            "total": a.total_questions,
            "percentage": (a.score / a.total_questions * 100) if a.total_questions > 0 else 0,
            "date": a.completed_at.strftime("%Y-%m-%d %H:%M")
        })
        
    predicted_score = 0
    if len(history) > 0:
        recent_scores = [h['percentage'] for h in history[-3:]]
        predicted_score = sum(recent_scores) / len(recent_scores) + 5
        predicted_score = min(100, predicted_score)
        
    section_accuracy = {}
    for a in attempts:
        if a.section_scores:
            try:
                scores = json.loads(a.section_scores)
                for section, data in scores.items():
                    if section not in section_accuracy:
                        section_accuracy[section] = {"total_correct": 0, "total_attempted": 0}
                    section_accuracy[section]["total_correct"] += data.get("score", 0)
                    section_accuracy[section]["total_attempted"] += data.get("total", 0)
            except:
                pass
                
    formatted_section_accuracy = []
    for section, data in section_accuracy.items():
        if data["total_attempted"] > 0:
            formatted_section_accuracy.append({
                "section": section,
                "accuracy": round((data["total_correct"] / data["total_attempted"]) * 100, 1),
                "fullMark": 100
            })
            
    return jsonify({
        "history": history,
        "predicted_score": round(predicted_score, 2),
        "section_accuracy": formatted_section_accuracy
    }), 200
