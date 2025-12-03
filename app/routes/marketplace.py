from flask import Blueprint, render_template

marketplace = Blueprint("marketplace", __name__)


@marketplace.route("/")
@marketplace.route("/marketplace")
def market_home():
    return render_template("marketplace.html", title="Marketplace")
