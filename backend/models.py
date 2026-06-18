from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    attempts = db.relationship('TestAttempt', backref='user', lazy=True)
    progress = db.relationship('UserQuestionProgress', backref='user', lazy=True)

class MasterQuestion(db.Model):
    """Central repository for curated questions (Extracted Bank)."""
    id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(100), nullable=False)
    sub_topic = db.Column(db.String(100), nullable=True)
    text = db.Column(db.Text, nullable=False)
    options = db.Column(db.Text, nullable=False) # JSON string
    correct_answer = db.Column(db.String(200), nullable=False)
    explanation = db.Column(db.Text, nullable=True)
    source = db.Column(db.String(300), nullable=True)
    difficulty = db.Column(db.String(20), default='medium')

class UserQuestionProgress(db.Model):
    """Tracks if a user has attempted/passed a specific master question."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    master_question_id = db.Column(db.Integer, db.ForeignKey('master_question.id'), nullable=False)
    is_attempted = db.Column(db.Boolean, default=False)
    is_correct = db.Column(db.Boolean, default=False)
    last_attempted_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class MockTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # is_extracted = True means this test uses real curated questions, not AI-generated
    is_extracted = db.Column(db.Boolean, default=False, nullable=False)
    questions = db.relationship('Question', backref='test', lazy=True, cascade="all, delete-orphan")
    attempts = db.relationship('TestAttempt', backref='test', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('mock_test.id'), nullable=False)
    # Link to MasterQuestion if this is an extracted question
    master_question_id = db.Column(db.Integer, db.ForeignKey('master_question.id'), nullable=True)
    section = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    options = db.Column(db.Text, nullable=False) # JSON string
    correct_answer = db.Column(db.String(200), nullable=False)
    explanation = db.Column(db.Text, nullable=True)
    # source tracks where extracted questions came from
    source = db.Column(db.String(300), nullable=True)

class TestAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('mock_test.id'), nullable=False)
    score = db.Column(db.Float, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    section_scores = db.Column(db.Text, nullable=True) # JSON string

class BsNegiProgress(db.Model):
    """Tracks progress of BS Negi MCQ Practice."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.String(100), nullable=False) # e.g. "bs_negi_1_0" (unit_index)
    is_correct = db.Column(db.Boolean, default=False)
    is_attempted = db.Column(db.Boolean, default=True)
    last_attempted_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

