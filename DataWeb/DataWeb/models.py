""" Define the database model
"""
#pylint: disable-all
from DataWeb import db,app
from flask_user import UserMixin
from config import BootstrapTheme



class User(db.Model, UserMixin):
    """ Represents a User
    """
    id = db.Column(db.Integer, primary_key=True)                                                #  @UndefinedVariable

    # User authentication information
    username = db.Column(db.String(50), nullable=False, unique=True)                            # @UndefinedVariable
    password = db.Column(db.String(255), nullable=False, server_default='')                     # @UndefinedVariable

    # User email information
    email = db.Column(db.String(255), nullable=True, unique=True)                              # @UndefinedVariable
    confirmed_at = db.Column(db.DateTime())                                                     # @UndefinedVariable

    # User information
    active = db.Column('is_active', db.SmallInteger(), nullable=False, server_default='0')      # @UndefinedVariable
    first_name = db.Column(db.String(100),nullable=False, server_default='')                    # @UndefinedVariable
    last_name = db.Column(db.String(100),nullable=False, server_default='')                     # @UndefinedVariable
    bootstrap_theme = db.Column(db.Enum(BootstrapTheme),nullable=True)                          # @UndefinedVariable

    def get_bootstrap_theme(self):
        ''' Return ther bootstrap theme assigned to user
        or config.default_bootstrap_theme if none defined.
        '''
        if self.bootstrap_theme == None:
            bootstrap_theme = app.config['DEFAULT_BOOTSTRAP_THEME']
        else:
            bootstrap_theme = self.bootstrap_theme

        return bootstrap_theme

    def __repr__(self):
        return '<User %r>' % (self.username)

class Issue(db.Model):
    """ Represents a Data Issue or subject area.
    """

    id = db.Column(db.String(10), primary_key=True)                   # @UndefinedVariable
    description = db.Column(db.String(500),nullable=True)             # @UndefinedVariable
    status = db.Column(db.String(10),nullable=False)                  # @UndefinedVariable

    def __repr__(self):
        return '<Issue %r>' % (self.id)
