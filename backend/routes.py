from flask import Blueprint, request, jsonify
from models import db, MockTest, Question, TestAttempt, User
from ai_service import generate_mock_test_from_syllabus
from extracted_questions import UK_GK_QUESTION_BANK
from bs_negi_questions import BS_NEGI_UNITS_METADATA, BS_NEGI_QUESTION_BANK
import json
import math # Import the math module
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
            options=json.dumps(q_data['options'], ensure_ascii=False), # Convert list to JSON string for DB
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
    
    num_questions = data.get('num_questions', 30) # Default to 30 if not provided
    balance_topics = data.get('balance_topics', False) # Default to False if not provided

    set_number = MockTest.query.filter_by(is_extracted=True).count() + 1
    
    default_title = f'Extracted UK GK — Set {set_number}'
    if sub_topic:
        default_title = f'Extracted: {sub_topic} — Set {set_number}'
        
    # If balancing topics, the title should reflect that
    if balance_topics and (sub_topic is None or sub_topic == 'All Topics'):
        default_title = f'Balanced Full Mock ({num_questions} Qs) — Set {set_number}'
        
    title = data.get('title', default_title)

    selected_questions_for_test = []

    # Start with a base query for eligible questions
    eligible_questions_query = MasterQuestion.query
    if exclude_attempted:
        # Get IDs of questions this user has already attempted
        attempted_ids = db.session.query(UserQuestionProgress.master_question_id).filter_by(
            user_id=user_id, is_attempted=True
        ).all()
        attempted_ids = [aid[0] for aid in attempted_ids]
        eligible_questions_query = eligible_questions_query.filter(~MasterQuestion.id.in_(attempted_ids))

    if balance_topics and (sub_topic is None or sub_topic == 'All Topics'):
        # Logic for balancing questions across all sub-topics
        all_sub_topics_in_bank = db.session.query(MasterQuestion.sub_topic).distinct().all()
        all_sub_topics_in_bank = [st[0] for st in all_sub_topics_in_bank if st[0]] # Filter out None

        questions_by_sub_topic = defaultdict(list)
        
        # Fetch all eligible questions for balancing
        eligible_questions = eligible_questions_query.all()

        for q in eligible_questions:
            if q.sub_topic and q.sub_topic in all_sub_topics_in_bank: # Only consider known sub-topics
                questions_by_sub_topic[q.sub_topic].append(q)
        
        total_eligible_questions_for_balancing = sum(len(q_list) for q_list in questions_by_sub_topic.values())
        if total_eligible_questions_for_balancing == 0:
             return jsonify({"error": "No eligible questions found to balance across topics."}), 404

        # Determine how many questions to pick from each sub-topic
        questions_to_pick_per_topic = {}
        for st in all_sub_topics_in_bank:
            if st in questions_by_sub_topic:
                proportion = len(questions_by_sub_topic[st]) / total_eligible_questions_for_balancing
                # Use math.ceil to ensure at least 1 question if a topic has questions
                questions_to_pick_per_topic[st] = max(1, math.ceil(proportion * num_questions))
            else:
                questions_to_pick_per_topic[st] = 0

        # Adjust total if rounding causes it to exceed num_questions or be too low
        current_total_picked = sum(questions_to_pick_per_topic.values())

        # If we picked too many due to rounding, reduce from largest topics first
        while current_total_picked > num_questions:
            # Find the topic with the most questions picked that still has questions available
            largest_topic = None
            max_picked = 0
            for st, count in questions_to_pick_per_topic.items(): # type: ignore
                if count > 0 and count > max_picked:
                    largest_topic = st
                    max_picked = count
            
            if largest_topic:
                questions_to_pick_per_topic[largest_topic] -= 1
                current_total_picked -= 1
            else: # Should not happen if num_questions is reasonable
                break
        
        # If we picked too few, add to topics that still have available questions
        while current_total_picked < num_questions:
            # Find a topic that has more eligible questions than we've picked
            topic_to_add = None
            for st, count in questions_to_pick_per_topic.items():
                if count < len(questions_by_sub_topic[st]):
                    topic_to_add = st
                    break
            
            if topic_to_add:
                questions_to_pick_per_topic[topic_to_add] += 1
                current_total_picked += 1
            else: # No more topics to add to, break
                break


        for st, count in questions_to_pick_per_topic.items():
            if count > 0 and st in questions_by_sub_topic:
                random.shuffle(questions_by_sub_topic[st])
                selected_questions_for_test.extend(questions_by_sub_topic[st][:count])
        
        random.shuffle(selected_questions_for_test) # Shuffle the final list

    else:
        # Existing logic for single topic or no balancing (if balance_topics is False)
        # Apply sub_topic filter here if not balancing across all topics
        if sub_topic and sub_topic != 'All Topics':
            eligible_questions_query = eligible_questions_query.filter_by(sub_topic=sub_topic)
        
        all_questions = eligible_questions_query.all()
        random.shuffle(all_questions)
        
        selected_questions_for_test = all_questions[:num_questions]

    if not selected_questions_for_test:
        msg = f"No eligible questions found for the selected criteria."
        if sub_topic and sub_topic != 'All Topics':
            msg += f" (Sub-topic: {sub_topic})"
        if exclude_attempted:
            msg += " (excluding attempted)"
        return jsonify({"error": msg}), 404

    new_test = MockTest(title=title, is_extracted=True)
    db.session.add(new_test)
    db.session.commit()

    for mq in selected_questions_for_test:
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
        "title": title, # Use the generated title
        "question_count": len(selected_questions_for_test),
        "sub_topic": sub_topic if sub_topic != 'All Topics' else 'All Topics (Balanced)' if balance_topics else 'All Topics'
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
                print(f"Warning: Could not parse section_scores for attempt {a.id}: {a.section_scores}")
                
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

# ─────────────────────────────────────────────────────────────
#  B.S. NEGI MCQ PRACTICE ROUTES
# ─────────────────────────────────────────────────────────────

@api.route('/bs_negi/units', methods=['GET'])
def get_bs_negi_units():
    user_id = request.args.get('user_id', 1, type=int)
    from models import BsNegiProgress
    from collections import defaultdict # Import defaultdict
    from bs_negi_questions import BS_NEGI_QUESTION_BANK
    
    progress_records = BsNegiProgress.query.filter_by(user_id=user_id).all()
    progress_map = {p.question_id: p for p in progress_records}
    
    unit_questions = defaultdict(list)
    for i, q in enumerate(BS_NEGI_QUESTION_BANK):
        unit_questions[q['unit']].append((i, q))
        
    results = []
    for unit_num in sorted(unit_questions.keys()):
        meta = BS_NEGI_UNITS_METADATA.get(unit_num, {
            "title_hi": f"इकाई {unit_num}",
            "title_en": f"Unit {unit_num}"
        })
        chapters = sorted(list(set(q['chapter'] for _, q in unit_questions[unit_num])))
        
        q_list = unit_questions[unit_num]
        q_count = len(q_list)
        attempted_count = 0
        correct_count = 0
        
        for idx, _ in q_list:
            q_id = f"bs_negi_{idx}"
            if q_id in progress_map:
                attempted_count += 1
                if progress_map[q_id].is_correct:
                    correct_count += 1
                    
        results.append({
            "unit_number": unit_num,
            "title_hi": meta["title_hi"],
            "title_en": meta["title_en"],
            "chapters": chapters,
            "question_count": q_count,
            "attempted_count": attempted_count,
            "correct_count": correct_count
        })
    return jsonify(results), 200

@api.route('/ai_practice_questions', methods=['POST'])
def get_ai_practice_questions():
    """
    Generates a set of AI-powered practice questions on demand.
    These questions are not saved to the database as a formal mock test.
    """
    data = request.json
    
    # Dynamically generate syllabus text from BS_NEGI_UNITS_METADATA
    syllabus_parts = []
    for unit_num in sorted(BS_NEGI_UNITS_METADATA.keys()):
        meta = BS_NEGI_UNITS_METADATA[unit_num]
        syllabus_parts.append(f"Unit {unit_num}: {meta['title_en']} ({meta['title_hi']})")
    syllabus_text = "Generate questions based on the following topics from B.S. Negi's Uttarakhand GK book: " + "; ".join(syllabus_parts) + "."

    section = data.get('section', 'full')
    # For practice, generate a smaller set of questions, e.g., 3-5 per section
    num_questions_per_section = data.get('num_questions_per_section', 3) 
    
    try:
        generated_questions = generate_mock_test_from_syllabus(
            syllabus_text=syllabus_text, 
            section=section, 
            num_questions_per_section=num_questions_per_section
        )
        
        # Add a dummy ID for frontend tracking, as these are not saved to DB
        for i, q in enumerate(generated_questions):
            q['id'] = f"ai_practice_{i}"
            q['unit'] = 0 # Dummy unit for display purposes in frontend
            q['chapter'] = q.get('section', 'AI Generated Practice') # Use section as chapter if available
            # Map to keys from improved AI service
            q['text_hi'] = q.get('text_hi', q.get('text', ''))
            q['text_en'] = q.get('text_en', '(AI Generated Question)')
            q['explanation_hi'] = q.get('explanation_hi', q.get('explanation', ''))
            q['explanation_en'] = q.get('explanation_en', '(Detailed AI Analysis)')
            q['attempted'] = False
            q['correct'] = False

        return jsonify(generated_questions), 200
    except Exception as e:
        print(f"Error generating AI practice questions: {e}")
        return jsonify({"error": f"Failed to generate AI practice questions: {str(e)}"}), 500

@api.route('/bs_negi/questions', methods=['GET'])
def get_bs_negi_questions():
    unit_num = request.args.get('unit', type=int)
    user_id = request.args.get('user_id', 1, type=int)
    from models import BsNegiProgress
    from bs_negi_questions import BS_NEGI_QUESTION_BANK
    
    progress_records = BsNegiProgress.query.filter_by(user_id=user_id).all()
    progress_map = {p.question_id: p for p in progress_records}
    
    questions = []
    for i, q in enumerate(BS_NEGI_QUESTION_BANK):
        if unit_num is not None and q['unit'] != unit_num:
            continue
            
        q_id = f"bs_negi_{i}"
        prog = progress_map.get(q_id)
        
        # Shuffle options to ensure the correct answer is not always the first one
        shuffled_options = list(q['options'])
        random.shuffle(shuffled_options)

        questions.append({
            "id": q_id,
            "unit": q['unit'],
            "chapter": q['chapter'],
            "text_hi": q['text_hi'],
            "text_en": q['text_en'],
            "options": shuffled_options,
            "correct_answer": q['correct_answer'],
            "explanation_hi": q['explanation_hi'],
            "explanation_en": q['explanation_en'],
            "attempted": prog.is_attempted if prog else False,
            "correct": prog.is_correct if prog else False
        })
    
    # Shuffle the questions themselves so the order is different every time
    random.shuffle(questions)
    
    return jsonify(questions), 200

@api.route('/bs_negi/progress', methods=['POST'])
def save_bs_negi_progress():
    data = request.json or {}
    user_id = data.get('user_id', 1)
    
    updates = data.get('updates', [])
    if not updates:
        q_id = data.get('question_id')
        is_correct = data.get('is_correct', False)
        if q_id:
            updates = [{"question_id": q_id, "is_correct": is_correct}]
            
    if not updates:
        return jsonify({"error": "No updates provided"}), 400
        
    from models import BsNegiProgress
    
    for item in updates:
        q_id = item.get('question_id')
        is_correct = item.get('is_correct', False)
        if not q_id:
            continue
            
        prog = BsNegiProgress.query.filter_by(user_id=user_id, question_id=q_id).first()
        if not prog:
            prog = BsNegiProgress(user_id=user_id, question_id=q_id)
            db.session.add(prog)
        
        prog.is_attempted = True
        prog.is_correct = is_correct
        
    db.session.commit()
    return jsonify({"message": "Progress updated successfully"}), 200
