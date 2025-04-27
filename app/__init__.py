from flask import Flask
from .database import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    Migrate(app, db)
    
    # Register blueprints
    from .routes import main_bp, incidents_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(incidents_bp)
    
    return app
