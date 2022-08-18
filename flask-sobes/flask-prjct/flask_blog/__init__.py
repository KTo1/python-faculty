from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_blog.config import Config


db = SQLAlchemy()
lm = LoginManager()


def create_app():
    print(__name__)
    app = Flask(__name__)

    lm.init_app(app)

    from flask_blog.main.ruotes import main
    app.register_blueprint(main)

    app.config.from_object(Config)

    return app
