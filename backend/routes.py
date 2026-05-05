from flask import Blueprint, request, jsonify
from models import db, MockTest, Question, TestAttempt, User
from ai_service import generate_mock_test_from_syllabus
from extracted_questions import UK_GK_QUESTION_BANK
import json
import random

api = Blueprint('api', __name__)

def _ensure_master_questions():
    """Helper to auto-seed the MasterQuestion table if it's empty (Vercel specific fix)."""
    from models import MasterQuestion
    if MasterQuestion.query.count() == 0:
        print("MasterQuestion table empty. Auto-seeding from static bank...")
        for q_data in UK_GK_QUESTION_BANK:
            opts = list(q_data['options'])
            random.shuffle(opts)
            mq = MasterQuestion(
                section=q_data.get('section', 'Uttarakhand GK'),
                sub_topic=q_data.get('sub_topic'),
                text=q_data['text'],
                options=json.dumps(opts, ensure_ascii=False),
                correct_answer=q_data['correct_answer'],
                explanation=q_data.get('explanation'),
                source=q_data.get('source'),
                difficulty='medium'
            )
            db.session.add(mq)
        db.session.commit()

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
    
    new_test = MockTest(title=title, is_extracted=False)
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
    result = [{"id": t.id, "title": t.title, "created_at": t.created_at, "is_extracted": t.is_extracted} for t in tests]
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
            "source": q.source,
            "options": json.loads(q.options)
        })
        
    return jsonify({"id": test.id, "title": test.title, "is_extracted": test.is_extracted, "questions": q_list}), 200

# ─────────────────────────────────────────────────────────────
#  EXTRACTED MOCK TESTS — Curated UK GK (No AI)
# ─────────────────────────────────────────────────────────────

@api.route('/extracted_tests', methods=['GET'])
def get_extracted_tests():
    """Returns all extracted (curated, non-AI) mock tests."""
    tests = MockTest.query.filter_by(is_extracted=True).order_by(MockTest.created_at.desc()).all()
    result = []
    for t in tests:
        q_count = Question.query.filter_by(test_id=t.id).count()
        result.append({
            "id": t.id,
            "title": t.title,
            "created_at": t.created_at.strftime("%Y-%m-%d"),
            "question_count": q_count,
            "is_extracted": True
        })
    return jsonify(result), 200

@api.route('/extracted_subtopics', methods=['GET'])
def get_extracted_subtopics():
    """Returns unique list of sub-topics available in the MasterQuestion table."""
    from models import MasterQuestion
    _ensure_master_questions()
    sub_topics = db.session.query(MasterQuestion.sub_topic).distinct().all()
    # Flatten list of tuples
    result = [st[0] for st in sub_topics if st[0]]
    return jsonify(sorted(result)), 200

@api.route('/seed_extracted_test', methods=['POST'])
def seed_extracted_test():
    """
    Seeds a new extracted test using the MasterQuestion table.
    Supports filtering by 'sub_topic' and 'exclude_attempted'.
    """
    from models import MasterQuestion, UserQuestionProgress
    _ensure_master_questions()

    data = request.json or {}
    sub_topic = data.get('sub_topic')
    user_id = data.get('user_id', 1)
    exclude_attempted = data.get('exclude_attempted', False)
    
    set_number = MockTest.query.filter_by(is_extracted=True).count() + 1
    
    default_title = f'Extracted UK GK — Set {set_number}'
    if sub_topic:
        default_title = f'Extracted: {sub_topic} — Set {set_number}'
        
    title = data.get('title', default_title)

    # Base query
    query = MasterQuestion.query
    if sub_topic:
        query = query.filter_by(sub_topic=sub_topic)
    
    if exclude_attempted:
        # Get IDs of questions this user has already attempted
        attempted_ids = db.session.query(UserQuestionProgress.master_question_id).filter_by(
            user_id=user_id, is_attempted=True
        ).all()
        attempted_ids = [aid[0] for aid in attempted_ids]
        query = query.filter(~MasterQuestion.id.in_(attempted_ids))

    all_questions = query.all()
    random.shuffle(all_questions)
    
    # Take 20 questions for extracted tests (more manageable than 30)
    selected = all_questions[:20]

    if not selected:
        msg = f"No questions found for sub-topic: {sub_topic}"
        if exclude_attempted:
            msg += " (excluding attempted)"
        return jsonify({"error": msg}), 404

    new_test = MockTest(title=title, is_extracted=True)
    db.session.add(new_test)
    db.session.commit()

    for mq in selected:
        opts = json.loads(mq.options)
        random.shuffle(opts)
        q = Question(
            test_id=new_test.id,
            master_question_id=mq.id,
            section=mq.section,
            text=mq.text,
            options=json.dumps(opts, ensure_ascii=False),
            correct_answer=mq.correct_answer,
            explanation=mq.explanation,
            source=mq.source
        )
        db.session.add(q)

    db.session.commit()
    return jsonify({
        "message": "Extracted test seeded successfully",
        "test_id": new_test.id,
        "title": title,
        "question_count": len(selected),
        "sub_topic": sub_topic
    }), 201

# ─────────────────────────────────────────────────────────────

@api.route('/submit_test', methods=['POST'])
def submit_test():
    from models import UserQuestionProgress
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
        is_correct = (user_answer == q.correct_answer)
        
        if is_correct:
            score += 1
            section_scores[q.section]["score"] += 1
            
        # Record progress if it's a master question
        if q.master_question_id:
            progress = UserQuestionProgress.query.filter_by(
                user_id=user_id, master_question_id=q.master_question_id
            ).first()
            if not progress:
                progress = UserQuestionProgress(
                    user_id=user_id, master_question_id=q.master_question_id
                )
                db.session.add(progress)
            
            progress.is_attempted = True
            if is_correct:
                progress.is_correct = True
            
        review_data.append({
            "id": q.id,
            "correct_answer": q.correct_answer,
            "explanation": q.explanation
        })
            
    user = User.query.get(user_id)
    if not user:
        user = User(id=user_id, username="Student")
        db.session.add(user)
            
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

@api.route('/user_progress/<int:user_id>', methods=['GET'])
def get_user_progress(user_id):
    """Returns the user's progress through the MasterQuestion bank."""
    from models import MasterQuestion, UserQuestionProgress
    _ensure_master_questions()
    
    total_bank = MasterQuestion.query.count()
    attempted_count = UserQuestionProgress.query.filter_by(user_id=user_id, is_attempted=True).count()
    correct_count = UserQuestionProgress.query.filter_by(user_id=user_id, is_correct=True).count()
    
    # Sub-topic breakdown
    sub_topics = db.session.query(MasterQuestion.sub_topic).distinct().all()
    sub_topic_stats = []
    
    for st_tuple in sub_topics:
        st = st_tuple[0]
        if not st: continue
        
        st_total = MasterQuestion.query.filter_by(sub_topic=st).count()
        # Join with progress to see how many attempted in this sub-topic
        st_attempted = db.session.query(UserQuestionProgress).join(MasterQuestion).filter(
            UserQuestionProgress.user_id == user_id,
            UserQuestionProgress.is_attempted == True,
            MasterQuestion.sub_topic == st
        ).count()
        
        sub_topic_stats.append({
            "sub_topic": st,
            "total": st_total,
            "attempted": st_attempted,
            "percentage": round((st_attempted / st_total * 100), 1) if st_total > 0 else 0
        })
        
    return jsonify({
        "total_bank": total_bank,
        "attempted_count": attempted_count,
        "correct_count": correct_count,
        "overall_progress": round((attempted_count / total_bank * 100), 1) if total_bank > 0 else 0,
        "sub_topic_stats": sorted(sub_topic_stats, key=lambda x: x['percentage'], reverse=True)
    }), 200
