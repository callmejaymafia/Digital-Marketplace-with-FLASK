from flask import Blueprint, render_template

market = Blueprint("market", __name__)


@market.route("/")
@market.route("/market")
def market_home():
    return render_template("market.html", title="Market")
