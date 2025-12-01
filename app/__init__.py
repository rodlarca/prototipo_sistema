from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev_key_123'

    db.init_app(app)

    # 👇 ESTA LÍNEA ES CLAVE
    from . import models

    from .routes import main
    app.register_blueprint(main)

    return app