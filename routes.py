"""
Routes of the application
"""
from app import app, db, login_manager
from flask import flash, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from forms import GoodNewsForm, LoginForm, RegistrationForm
from models import Journalist, News
from werkzeug.utils import redirect


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Home page
    :return: render_template function call
    """
    good_news = News.query.order_by(News.id.desc()).limit(10)
    if current_user.is_authenticated:
        app.logger.info('current user is authenticated')
    else:
        app.logger.info('current user is anonymous')
    return render_template(
        'index.html', good_news=good_news)


@app.route('/news/<int:news_id>')
def news(news_id):
    """
    Specific page for news
    :param news_id: integer
    :return:
    """
    app.logger.info(f'try to open news with id "{news_id}"')
    news = News.query.filter_by(
        id=news_id).first_or_404(description="There is no news with this ID.")

    return render_template('news.html', news=news,
                           journalist=news.journalist,
                           journalist_news=list(news.journalist.news_article))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(meta={'csrf': False})
    if form.validate_on_submit():
        try:
            user = Journalist(
                name=form.username.data,
                email=form.email.data,
                surname=form.user_surname.data)
            app.logger.info(
                f'try register user "{form.username.data}" '
                f'"{form.user_surname.data}" "{form.email.data}"')
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()

        except Exception as e:
            flash("Please enter a valid registration data")
            app.logger.error(f'registration failed: {e}')
        else:
            flash("You successfully register!")
            app.logger.info('registration successful')
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    user = Journalist.query.filter_by(name=username).first_or_404()
    app.logger.info(f'open user page for user "{username}"')
    if 'news' in request.form:
        app.logger.info(
            f'add new to db with title '
            f'"{request.form["news"]}" by user id {user.id}')
        db.session.add(
            News(title=request.form['news'],
                 text=request.form['news_text'],
                 journalist_id=user.id))
        db.session.commit()
        return redirect(url_for('index'))

    return render_template(
        'user.html',
        current_user=user,
        template_form=GoodNewsForm())


@login_manager.user_loader
def load_user(user_id):
    return Journalist.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(meta={'csrf': False})
    if form.validate_on_submit():
        app.logger.info(
            f'try to find user by email "{form.email.data}"')
        user = Journalist.query.filter_by(
            email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            app.logger.info(
                f'user "{user.name}" "{user.surname}" successfully logged in')
            return redirect(url_for('user', username=user.name))
        else:
            app.logger.info(
                f'user "user failed logged in')
            return login_manager.unauthorized()
    return render_template('login.html', form=form)


@login_manager.unauthorized_handler
def unauthorized():
    return "Please logged in to view this page"


@app.route("/logout")
@login_required
def logout():
    app.logger.info('user logged out')
    logout_user()
    return redirect(url_for('index'))
