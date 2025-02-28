from flask import Flask

from .config import Config
from .database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .controllers.award_controller import award_bp

    app.register_blueprint(award_bp)

    return app
