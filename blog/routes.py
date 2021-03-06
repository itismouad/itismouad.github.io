from flask import render_template

from . import app
from .utils import months, get_title_from_slug
from .articles import articles_data

# Handlers
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html', articles_data=reversed(articles_data))

@app.route('/blog/<year>/<month>/<slug>')
def blog_article(year, month, slug):
    try:
        year = int(year)
        month = int(month)
    except Exception as e:
        return error_404(e)

    try:
        template_path = "{year}/{month}/{slug}.html".format(
            year=year,
            month=month,
            slug=slug
        )

        time_of_writing = months[month] + " " + str(year)
        title = get_title_from_slug(slug) or 'No title'

        return render_template(
            template_path,
            title=title,
            time_of_writing=time_of_writing
        )

    except TemplateNotFound as e:
        return error_404(e)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

# @app.route('/reads')
# def reads():
#     return render_template('reads.html')

@app.route('/python')
def python():
    import sys
    return str(sys.version_info)
