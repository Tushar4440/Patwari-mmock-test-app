from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    attempts = db.relationship('TestAttempt', backref='user', lazy=True)

class MockTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    questions = db.relationship('Question', backref='test', lazy=True, cascade="all, delete-orphan")
    attempts = db.relationship('TestAttempt', backref='test', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('mock_test.id'), nullable=False)
    section = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    options = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.String(200), nullable=False)
    explanation = db.Column(db.Text, nullable=True)

class TestAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('mock_test.id'), nullable=False)
    score = db.Column(db.Float, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    section_scores = db.Column(db.Text, nullable=True)
