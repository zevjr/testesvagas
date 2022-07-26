import os

from flask import Flask, jsonify
from flask_swagger import swagger

from .config import config_app
from .controllers import cart_bp, product_bp, sales_bp
from .db import db, ma, migrate
from .models import *
from .swagger import swaggerui_blueprint


def create_app():
    app = Flask(__name__)
    app = config_app(app)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(product_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(sales_bp)

    app.register_blueprint(swaggerui_blueprint)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        return jsonify(swag)

    return app
