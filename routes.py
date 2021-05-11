"""
Routes of the application
"""
from app import app, db
from flask import render_template, request

from forms import GoodNewsForm, RegistrationForm
from models import News, Journalist


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Home page
    :return: render_template function call
    """
    if 'news' in request.form:
        db.session.add(News(title=request.form['news'], text=request.form['news_text']))
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

    return render_template('news.html', news=news,
                           journalist=news.journalist)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(meta={'csrf': False} )
    if form.validate_on_submit():
        user = Journalist(name=form.username.data, email=form.email.data, surname=form.user_surname.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        db.session.add(user)
        db.session.commit()
    return render_template('register.html', title='Register', form=form)
