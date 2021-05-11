from datetime import datetime

from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), index=True)
    title = db.Column(db.String(50), index=True)

    journalist_id = db.Column(db.Integer, db.ForeignKey('journalist.id'))


class Journalist(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), index=True, unique=False)
    surname = db.Column(db.String(80), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    joined_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)

    news_article = db.relationship('News', backref='journalist', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return "Journalist: {}".format(self.email)
