from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Please fill out.')])
    password = PasswordField('Password', validators=[DataRequired(message='Please fill out.')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Please fill out.')])
    email = StringField('Email', validators=[DataRequired(message='Please fill out.'), Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Please fill out.')])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(message='Please fill out.'), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('A user with such username already exists.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('A user with such email already exists.')