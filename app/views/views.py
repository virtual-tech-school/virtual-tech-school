from flask import Blueprint, render_template

views = Blueprint('views', __name__, url_prefix="/")

@views.route("/")
def home():
    return render_template(
        "home/home.html"
    )