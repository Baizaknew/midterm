from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite25'
app.config['SECRET_KEY'] = 'secret_key'

db.init_app(app)

migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from .urls import *
