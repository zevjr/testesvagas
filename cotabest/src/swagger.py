from flask_swagger_ui import get_swaggerui_blueprint
import os

SWAGGER_URL = "/api/docs"
API_URL = os.getenv("SWAGGER_URL")+"/spec"


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Cotabest application"},
)
