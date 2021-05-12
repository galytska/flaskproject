"""
Routes of the application
"""
from flask_login import login_required, login_user
from werkzeug.utils import redirect

from app import app, db, login_manager
from flask import render_template, request, url_for, flash

from forms import GoodNewsForm, RegistrationForm, LoginForm
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
    form = RegistrationForm(meta={'csrf': False})
    if form.validate_on_submit():
        try:
            user = Journalist(name=form.username.data, email=form.email.data, surname=form.user_surname.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()

            db.session.add(user)
            db.session.commit()
        except:
            flash("Please enter a valid registration data")
        else:
            flash("You successfully register!")
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = Journalist.query.filter_by(name=username).first_or_404()
    return render_template('user.html', user=user)


@login_manager.user_loader
def load_user(user_id):
    return Journalist.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(meta={'csrf': False})
    if form.validate_on_submit():
        user = Journalist.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            # next_page = request.args.get('next')
            # return redirect(next_page) if next_page else redirect(url_for('index', _external=True, _scheme='http'))
            return redirect(url_for('index', _external=True, _scheme='http'))
        else:
            return redirect(url_for('login', _external=True, _scheme='http'))
    return render_template('login.html', form=form)
