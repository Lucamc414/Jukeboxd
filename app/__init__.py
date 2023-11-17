from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object('config')
babel = Babel(app)
db = SQLAlchemy(app)

# Handles all migrations.
migrate = Migrate(app, db)
admin = Admin(app, template_mode='bootstrap4')

from app import views, models
