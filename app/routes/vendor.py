from flask import Blueprint

vendor = Blueprint("vendor", __name__)


@vendor.route("/dashboard")
def dashboard():
    return "Welcome"
