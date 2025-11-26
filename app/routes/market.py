from flask import Blueprint, render_template, redirect, url_for

routes = Blueprint("routes", __name__)


@routes.route("/")
def home():
    return "Welcome to the Home Page"
