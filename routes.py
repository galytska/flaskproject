"""
Routes of the application
"""
from app import app, db
from flask import render_template, request
from flask_wtf import FlaskForm
from models import News
from wtforms import StringField, SubmitField


class GoodNewsForm(FlaskForm):
    """
    Allows add new news
    """
    news = StringField('news')
    submit = SubmitField('Add news')


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Home page
    :return: render_template function call
    """
    if 'news' in request.form:
        db.session.add(News(news_text=request.form['news']))
        db.session.commit()

    return render_template(
        'index.html', good_news=News.query.all(),
        template_form=GoodNewsForm())


@app.route('/news/<int:news_id>')
def news(news_id):
    """
    Specific page for news
    :param news_id: integer
    :return:
    """
    news = News.query.filter_by(
        id=news_id).first_or_404(description="There is no news with this ID.")
    return render_template('news.html', news=news)
