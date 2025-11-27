from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    EmailField,
)


class Signup(FlaskForm):
    fullName = StringField("Full Name", validators=[DataRequired()])
    userName = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")
