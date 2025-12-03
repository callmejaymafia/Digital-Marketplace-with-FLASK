from flask import Blueprint, render_template, request, flash, redirect
from app.forms import Signup, Signin

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/sign-up", methods=["POST", "GET"])
def signup():
    form = Signup()
    return render_template("sign_up.html", title="Sign Up", form=form)


@auth.route("/sign-in", methods=["POST", "GET"])
def signin():
    form = Signin()
    if form.validate_on_submit():
        flash(
            f"Login requested {form.identifier.data}, Remember me {form.rememberMe.data}"
        )
        return redirect("/dashboard")
    return render_template("sign_in.html", title="Sign In", form=form)


@auth.route("/sign-out")
def signout():
    pass
