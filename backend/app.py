from flask import Flask
from flask_cors import CORS
from models import db
from routes import api

import os

def create_app():
    app = Flask(__name__, instance_path='/tmp' if os.environ.get('VERCEL') else None)
    CORS(app)
    
    if os.environ.get('VERCEL'):
        # Vercel uses a read-only file system except for /tmp
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
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
