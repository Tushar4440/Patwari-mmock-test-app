from flask import Flask
from flask_cors import CORS
from models import db
from routes import api

import os

def create_app():
    # Use /tmp for the database because Vercel's file system is read-only
    # On local machine, it will still work but might save to a different temp location
    database_path = '/tmp/database.db' if os.environ.get('VERCEL') else 'sqlite:///database.db'
    
    app = Flask(__name__, instance_path='/tmp' if os.environ.get('VERCEL') else None)
    CORS(app)
    
    if os.environ.get('VERCEL'):
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    app.register_blueprint(api, url_prefix='/api')

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
