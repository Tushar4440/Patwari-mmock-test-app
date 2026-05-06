import json
import random
from app import app
from models import db, MasterQuestion

def import_from_json():
    try:
        with open('scraped_questions.json', 'r', encoding='utf-8') as f:
            questions = json.load(f)
    except FileNotFoundError:
        print("Error: scraped_questions.json not found. Run the scraper first.")
        return

    with app.app_context():
        print(f"Importing {len(questions)} questions into MasterQuestion table...")
        
        added_count = 0
        for q_data in questions:
            # Check for duplicates by text
            exists = MasterQuestion.query.filter_by(text=q_data['text']).first()
            if not exists:
                opts = q_data['options']
                random.shuffle(opts)
                
                mq = MasterQuestion(
                    section=q_data['section'],
                    sub_topic=q_data['sub_topic'],
                    text=q_data['text'],
                    options=json.dumps(opts, ensure_ascii=False),
                    correct_answer=q_data['correct_answer'],
                    explanation=q_data['explanation'],
                    source=q_data['source'],
                    difficulty='medium'
                )
                db.session.add(mq)
                added_count += 1
        
        db.session.commit()
        print(f"Successfully added {added_count} new questions to the database!")

if __name__ == "__main__":
    import_from_json()