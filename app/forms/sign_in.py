from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    BooleanField,
)


class Signin(FlaskForm):
    identifier = StringField("Username or Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    rememberMe = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
