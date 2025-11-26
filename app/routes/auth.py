from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint("auth", __name__)


@auth.route("/sign-in")
def signin():
    return "Sign in Page"
