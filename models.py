from app import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), index=True)
    title = db.Column(db.String(50), index=True)

    journalist_id = db.Column(db.Integer, db.ForeignKey('journalist.id'))


class Journalist(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), index=True, unique=False)
    surname = db.Column(db.String(80), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)

    news_article = db.relationship('News', backref='journalist', lazy='dynamic')

    def __repr__(self):
        return "Journalist: {}".format(self.email)


