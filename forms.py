from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo



class GoodNewsForm(FlaskForm):
    """
    Allows add new news
    """
    news = StringField('news')
    news_text = TextAreaField('News text')
    submit = SubmitField('Add news')


class RegistrationForm(FlaskForm):
    """
    Form to add a new user
    """
    username = StringField('Username', validators=[DataRequired()])
    user_surname = StringField('User Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Register')


class LoginForm(FlaskForm):
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')
