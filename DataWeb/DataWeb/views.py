from __future__ import print_function
from __future__ import absolute_import

from flask import g, render_template, request
from flask_login import current_user
from flask_user import login_required
from DataWeb import app,db,models
from .forms import StyleForm
from DataWeb.forms import BootstrapThemeForm
from DataWeb.config import BootstrapTheme

@app.before_request
def before_request():
    ''' If someone is logged on, use their bootstrap theme
    otherwise use the default.
    '''
    g.user = current_user.get_id()
    if current_user.is_authenticated:
        g.bootstrap_theme = current_user.get_bootstrap_theme().get_name()
    else:
        g.bootstrap_theme = app.config["DEFAULT_BOOTSTRAP_THEME"].get_name()

@app.route('/')
@app.route('/index')
@login_required
def index():
    ''' The home page. Simply show the list of issues
    which route to a blank page for now.
    '''
    issues = models.Issue.query.all()

    return render_template('index.html',title='Home', issues=issues, nav_id='Home')

@app.route('/wait')
@login_required
def wait():
    return render_template('wait.html', nav_id='Chart', pagename='/ajax/wait')

@app.route('/ajax/wait')
@login_required
def ajax_wait():
    import pygal
    import time
    time.sleep(5)
    style = pygal.style.DefaultStyle
    line_chart = pygal.Line(style=style)
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    chart = line_chart.render_data_uri()
    return render_template('ajax_wait.html',chart=chart)


@app.route('/show_pygal_chart',methods=['GET', 'POST'])
@login_required
def show_pygal_chart():
    ''' Use pygal to render a simple chart
    '''
    import pygal

    form = StyleForm()
#    if form.validate_on_submit():
    if request.method == 'POST':
        style = pygal.style.styles[form.style.data]
    else:
        style = pygal.style.DefaultStyle
    line_chart = pygal.Line(style=style)
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    chart = line_chart.render_data_uri()
    return render_template('pygal_chart.html', chart=chart, form=form, nav_id='Chart')

@app.route('/show_bokeh_chart')
@login_required
def show_bokeh_chart():
    ''' Use bokeh to display a simple chart. '''
    from bokeh.plotting import figure
    from bokeh.embed import components

# 	1. Prepare some data
    x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    y0 = [i**2 for i in x]
    y1 = [10**i for i in x]
    y2 = [10**(i**2) for i in x]

# 	2. Create a new plot
    p = figure(tools="pan,box_zoom,reset,save",
               y_axis_type='log',
               y_range=[0.001,10**11],
               title="log axis example",
               plot_width=900,
               plot_height=700,
               x_axis_label="sections",
               y_axis_label="particles")

# 	3. Add some renderers
    p.line(x,x,legend="y=x")
    p.circle(x,x,legend="y=x",fill_color="white",size=5)
    p.line(x,y0,legend="y=x^2",line_width=3)
    p.line(x,y1,legend="y=10^x",line_color="red")
    p.circle(x,y1,legend="y=10^x",fill_color="red",line_color="red",size=6)
    p.line(x,y2,legend="y=10^x^2",line_color="orange",line_dash="4 4")

# 	5. Show the results
    script, div = components(p)
    return render_template('bokeh_chart.html',  div=div, script=script, nav_id='Chart')

@app.route('/show_markdown')
@login_required
def show_markdown():
    ''' Render some sample markdown text '''
    import markdown2
    from flask import Markup
    with app.open_resource('static/markdown/Example_Markdown.md') as f:
        file_contents = f.read()
    content = markdown2.markdown(file_contents,extras=['fenced-code-blocks','tables'])

    return render_template('markdown.html', content=Markup(content), nav_id='Markdown')

@app.route('/change_theme',methods=['GET', 'POST'])
@login_required
def change_theme():
    ''' Allow user to change default bootstrap theme
    '''
    form = BootstrapThemeForm()
    theme_list = []
    for k in list(BootstrapTheme):
        pair = (k.get_name(),k.get_name())
        theme_list.append(pair)
    form.theme.choices = theme_list
    if request.method == 'POST':
        # Get the chosen theme and update user record with it.
        theme = BootstrapTheme[form.theme.data]
        user = models.User.query.get(current_user.get_id())             # @UndefinedVariable
        user.bootstrap_theme = theme.get_name()
        g.bootstrap_theme = user.bootstrap_theme
        db.session.commit()                                             # @UndefinedVariable
        return render_template('change_theme.html',form=form)
    else:
        # Attempt the get the theme currently assigned to User in model
        user = models.User.query.get(current_user.get_id())             # @UndefinedVariable
        theme = user.bootstrap_theme
        if theme is None:
            theme = app.config['DEFAULT_BOOTSTRAP_THEME']
        form.theme.default = theme.get_name()
        form.process()

        return render_template('change_theme.html',form=form)

@app.route('/enhanced_table')
@login_required
def enhanced_table():
    ''' Render a table using table js library '''
    return render_template('enhanced_table.html')


@app.route('/blank_page')
@login_required
def blank_page():
    ''' Dummy page that the issue links point to '''
    return render_template('blank_page.html')

