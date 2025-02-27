from flask import Flask
from .config import Config
from .database import db
from .services.data_loader import load_movies_from_csv



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    breakpoint()
    if not Config.TESTING:
        with app.app_context():
            db.create_all()
            load_movies_from_csv(Config.DATA_FILE_PATH)

    from .controllers.award_controller import award_bp
    app.register_blueprint(award_bp)

    return app
