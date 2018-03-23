from flask import Flask
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

# Initialize Flask extensions
db   = SQLAlchemy(app)                          # Initialize Flask-SQLAlchemy
mail = Mail(app)                                # Initialize Flask-Mail


# import must be after app is created (so that decorators work...)
from .models import User
import DataWeb.db_utils, DataWeb.views, DataWeb.models
from .forms import StyleForm

# Setup Flask-User
db_adapter   = SQLAlchemyAdapter(db, User)        # Register the User model
user_manager = UserManager(db_adapter,
                           app)

