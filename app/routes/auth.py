from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/sign-in")
def signin():
    return "Sign in Page"
