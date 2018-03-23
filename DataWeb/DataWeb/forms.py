from __future__ import unicode_literals
from flask_wtf import FlaskForm
from wtforms import SelectField
from pygal.style import styles
from DataWeb.config import BootstrapTheme


class StyleForm(FlaskForm):
    ''' Form containing pygal styles
    '''
    style_list = []
    for k in styles:
        pair = (k,k)
        style_list.append(pair)

    style = SelectField(label='Style Name', choices=style_list,default='default')


class BootstrapThemeForm(FlaskForm):
    ''' Form containing Bootstrap themes
    '''
    theme_list = []
    for k in list(BootstrapTheme):
        pair = (k.get_name(),k.get_name())
        theme_list.append(pair)

    theme = SelectField(label='Theme Name')

