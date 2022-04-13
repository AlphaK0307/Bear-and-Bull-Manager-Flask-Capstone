from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class SignUpForm(FlaskForm):
    email= StringField('Email', validators=[DataRequired(), Email()])
    username= StringField('Username', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired()])
    confirm_pass= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField('SignUp')

class LoginForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired()])
    submit= SubmitField('Log In')
