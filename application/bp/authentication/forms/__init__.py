from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Regexp

# Basic regex pattern for emails (not exhaustive but works for common cases)
basic_email_regex = r'^[^@]+@[^@]+\.[^@]+$'

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Regexp(basic_email_regex, message="Invalid email address")
    ])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    pass
