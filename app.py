from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.challenges import challenges
from utils.db import magodb


app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

app.register_blueprint(challenges)
