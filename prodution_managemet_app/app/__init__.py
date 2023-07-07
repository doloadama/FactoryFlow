from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app import routes, models


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///production.db'
app.config['SECRET_KEY'] = 'your-secret-key'  # Set a secret key for session security
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
app = Flask(__name__)