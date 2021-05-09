"""
Main application module
"""
from os import environ

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'youneverknow'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    environ.get('DATABASE_URL').replace('postgres://', 'postgresql://') \
         if environ.get(
        'DATABASE_URL') else 'sqlite:///myDB.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import routes
