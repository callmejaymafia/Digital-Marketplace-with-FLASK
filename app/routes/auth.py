from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.forms import Signup, Signin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from app.models import Vendor
from app import login_manager

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/sign-up", methods=["POST", "GET"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("vendor.dashboard"))
    form = Signup()
    if form.validate_on_submit():
        fullName = form.fullName.data
        userName = form.userName.data
        email = form.email.data
        password = form.password.data

        existing_email = Vendor.query.filter_by(email=email).first()
        if existing_email:
            flash("This email is already registered.", "error")
            return redirect(url_for("auth.signup"))

        existing_username = Vendor.query.filter_by(userName=userName).first()
        if existing_username:
            flash("This username is already taken.", "error")
            return redirect(url_for("auth.signup"))

        new_user = Vendor(
            fullName=fullName,
            userName=userName,
            email=email,
            password=generate_password_hash(password, method="pbkdf2:sha256"),
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash("Account created successfully!", "success")
        return redirect(url_for("vendor.dashboard"))
    return render_template("sign_up.html", title="Sign Up", form=form)


@auth.route("/sign-in", methods=["POST", "GET"])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for("vendor.dashboard"))

    form = Signin()

    if form.validate_on_submit():
        identifier = form.identifier.data
        password = form.password.data
        rememberMe = form.rememberMe.data

        vendor = Vendor.query.filter(
            (Vendor.userName == identifier) | (Vendor.email == identifier)
        ).first()

        if vendor:
            if check_password_hash(vendor.password, password):

                login_user(vendor, remember=rememberMe)
                flash("Logged in successfully!", "success")
                return redirect(url_for("vendor.dashboard"))
            else:
                flash("Incorrect password, try again.", "error")
        else:
            flash("User not found.", "error")

        return redirect(url_for("auth.signin"))

    return render_template("sign_in.html", title="Sign In", form=form)


@login_manager.user_loader
def load_user(user_id):
    return Vendor.query.get(int(user_id))


@auth.route("/sign-out")
@login_required
def signout():
    logout_user()
    return redirect(url_for("auth.signin"))
