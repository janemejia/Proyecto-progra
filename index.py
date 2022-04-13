from app import app
from utils.db import magodb

with app.app_context():
    magodb.create_all()

if __name__ == "__main__":
    app.run(debug=True)