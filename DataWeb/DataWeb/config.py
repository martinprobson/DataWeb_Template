from __future__ import print_function
import os
import enum
from DataWeb import app
import pkg_resources  # part of setuptools

APP_NAME = app.name
USER_APP_NAME = APP_NAME

APP_VERSION = pkg_resources.require(APP_NAME)[0].version
APP_TEAM    = 'Example Issue dashboard - 2017'
#
# Flask-Mail SMTP settings - These are used by Flask-User to send user email verification emails
#
MAIL_USERNAME       =     os.getenv('MAIL_USERNAME',        'dummy@somewhere')
MAIL_PASSWORD       =     os.getenv('MAIL_PASSWORD',        '<password>')
MAIL_DEFAULT_SENDER =     os.getenv('MAIL_DEFAULT_SENDER',  '<sender>')
MAIL_SERVER         =     os.getenv('MAIL_SERVER',          'smtp server')
MAIL_PORT           =     int(os.getenv('MAIL_PORT',         '587'))
MAIL_USE_TLS        =     int(os.getenv('MAIL_USE_TLS',      True))
MAIL_USE_SSL        =     int(os.getenv('MAIL_USE_SSL',      False))

# Make sure SMTP setting are set correctly above before changing the two
# settings below....
USER_ENABLE_EMAIL=False
USER_ENABLE_LOGIN_WITHOUT_CONFIRM_EMAIL=True


# Initialize the database with dummy issues and a test user?
LOAD_DUMMY_DATA= True

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

BASEDIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR,'Test.db')

SQLALCHEMY_TRACK_MODIFICATIONS=False


class BootstrapTheme(enum.Enum):
    ''' Enum of boostrap themes
        stored against User
    '''
    def get_name(self):
        ''' Return basename of bootstrap theme
        '''
        return "%s" % (self._name_)

    cerulean = 1
    cosmo = 2
    cyborg = 3
    darkly = 4
    flatly = 5
    journal = 6
    lumen = 7
    paper = 8
    readable = 9
    sandstone = 10
    simplex = 11
    slate = 12
    spacelab = 13
    superhero = 14
    united = 15
    yeti = 16

#Default bootstrap theme - this theme is used if
# a) No-one is logged on or
# b) A custom theme is not specified in the user master record.
DEFAULT_BOOTSTRAP_THEME = BootstrapTheme['cerulean']


