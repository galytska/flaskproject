from os import environ

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'youneverknow'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL?sslmode=require').replace('postgres://',
                                                                                            'postgresql://') or 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news_text = db.Column(db.String(100), index=True)


class GoodNewsForm(FlaskForm):
    news = StringField('news')
    submit = SubmitField('Add news')


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'news' in request.form:
        db.session.add(News(news_text=request.form['news']))
        db.session.commit()

    return render_template('index.html', good_news=News.query.all(), template_form=GoodNewsForm())
