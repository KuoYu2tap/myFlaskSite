#coding=utf8

from datetime import datetime
import json
from flask import render_template, request, abort
from . import app
from .models import (Article, Tag, create_article)
from .utils import markdown2html, load_content

@app.errorhandler(403)
def page_not_found(error):
    title = unicode(error)
    message = error.description
    return render_template('errors.html',
                           errortitle=title,
                           message=message),403

@app.errorhandler(404)
def page_not_found(error):
    title = unicode(error)
    message = error.description
    return render_template('errors.html',
                           errortitle=title,
                           message=message),404

@app.errorhandler(500)
def internal_server_error(error):
    title = unicode(error)
    message = error.description
    return render_template('errors.html',
                           errortitle=title,
                           message=message),500

@app.route('/')
def homepage():
  return render_template('homepage.html')
  
@app.route('/index')
def index():
    tagz = Tag.query.all()
    pagination = Article.query.order_by(Article.id.desc()).paginate(1)
    return render_template('index.html',
                           pagination=pagination,
                           tagz=tagz,
			   flag='blog')


@app.route('/article/<id>')
def show_article(id):
    article = Article.query.get_or_404(id)
    tagz = Tag.query.all()
    return render_template('page.html',
                           title=article.title,
                           content=article.content,
                           pub_time=article.pub_time,
                           tags=article.tags,
                           tagz = tagz,
			   flag='blog')

@app.route('/tags')
def show_tags():
    tags = Tag.query.all()
    return render_template('tags.html',
                           tags=tags,
                           tagz=tags,
			   flag='tag' )

@app.route('/tag/<id>')
def show_tag(id):
    tag = Tag.query.get_or_404(id)
    tagz = Tag.query.all()
    articles = tag.articles.all()
    return render_template('tag.html',
                           tag=tag,
                           tagz=tagz,
                           entries=articles,
			   flag='tag')


# @app.route('/about')
# def about():
#     content = load_content('about')
#     return render_template('page.html',
#                            title='About',
#                            content=content)


@app.route('/links')
def links():
    content = load_content('links')
    tagz = Tag.query.all()
    return render_template('page.html',
                           title='Links',
                           content=content,
                           tagz=tagz,
			   flag='link')


@app.route('/publish', methods=['GET', 'POST'])
def publish():
    if request.method == 'GET':
        abort(404)

    # authorization
    token = request.form.get('token', '')
    if token != app.config['TOKEN']:
        return 'invalid access token', 500

    title = request.form.get('title', None)
    if not title:
        return 'no title found', 500

    summary = request.form.get('summary', None)
    if not summary:
        return 'no summary found', 500

    content = request.form.get('content', None)
    if not content:
        return 'no content found', 500
    content = markdown2html(content)

    pub_time = request.form.get('pub_time', None)
    if pub_time:
        pub_time = datetime.strptime(pub_time, app.config['TIME_FORMAT'])

    tags = request.form.getlist('tags')

    create_article(title, summary, content, pub_time, tags)
    return '', 200
