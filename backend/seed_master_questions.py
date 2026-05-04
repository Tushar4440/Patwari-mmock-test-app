from app import app
from models import db, MasterQuestion
from extracted_questions import UK_GK_QUESTION_BANK
import json

def seed_master():
    with app.app_context():
        # Clear existing master questions to avoid duplicates during development
        # In production, we'd use a more sophisticated sync logic
        print("Clearing existing master questions...")
        db.session.query(MasterQuestion).delete()
        
        print(f"Seeding {len(UK_GK_QUESTION_BANK)} questions into MasterQuestion table...")
        
        count = 0
        for q_data in UK_GK_QUESTION_BANK:
            mq = MasterQuestion(
                section=q_data.get('section', 'Uttarakhand GK'),
                sub_topic=q_data.get('sub_topic'),
                text=q_data['text'],
                options=json.dumps(q_data['options']),
                correct_answer=q_data['correct_answer'],
                explanation=q_data.get('explanation'),
                source=q_data.get('source'),
                difficulty='medium'
            )
            db.session.add(mq)
            count += 1
            if count % 100 == 0:
                db.session.commit()
                print(f"Seeded {count} questions...")
        
        db.session.commit()
        print("Seeding complete!")

if __name__ == "__main__":
    seed_master()
