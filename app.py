"""
Main application module
"""
import logging
from os import environ, path

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

filename = path.splitext(__file__)[0]
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s : %(message)s',
    handlers=[
        logging.FileHandler(f'{filename}.log', mode='w'),
        logging.StreamHandler()
    ])

app.config['SECRET_KEY'] = 'youneverknow'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    environ.get('DATABASE_URL').replace('postgres://', 'postgresql://') \
        if environ.get(
        'DATABASE_URL') else 'sqlite:///myDB.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

import routes, models
