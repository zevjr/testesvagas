from app import create_app
from app.config import Config
from app.services.data_loader import load_movies_from_csv
from app.database import db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        load_movies_from_csv(Config.DATA_FILE_PATH)
    app.run(host='0.0.0.0', port=5000, debug=True)
