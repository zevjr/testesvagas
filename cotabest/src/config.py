import os


def config_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv(
        "SQLALCHEMY_TRACK_MODIFICATIONS"
    )

    return app
