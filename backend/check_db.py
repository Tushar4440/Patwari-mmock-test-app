from app import create_app
from models import MockTest, Question
import json

app = create_app()
with app.app_context():
    test = MockTest.query.order_by(MockTest.id.desc()).first()
    print(f"Test ID: {test.id}, Title: {test.title}")
    questions = Question.query.filter_by(test_id=test.id).all()
    for q in questions:
        print(f"\nSection: {q.section}")
        print(f"Text: {q.text}")
        print(f"Options: {q.options}")
        print(f"Correct: {q.correct_answer}")
