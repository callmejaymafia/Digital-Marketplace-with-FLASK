from flask import Blueprint

market = Blueprint("market", __name__)


@market.route("/")
@market.route("/market")
def market_home():
    return "<h1>Welcome to the market</h1>"
