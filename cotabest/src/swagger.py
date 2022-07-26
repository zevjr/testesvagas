from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/api/docs"
API_URL = "http://127.0.0.1:5000/spec"


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Cotabest application"},
)
