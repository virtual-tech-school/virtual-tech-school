from flask import Blueprint

views = Blueprint('views', __name__, url_prefix="/")

@views.route("/")
def home():
    return "<h1 style='margin-top: 20px; display: flex; justify-content: center;'>Virtual Tech School in Under Construction!</h1>"

