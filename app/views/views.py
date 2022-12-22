from flask import Blueprint, render_template

views = Blueprint('views', __name__, url_prefix="/")

@views.route("/")
def home():
    stats_list = [
        {
            "name": "YouTube",
            "icon": "youtube.svg",
            "link": "https://www.youtube.com/c/ApoorvGoyalMain",
            "value": 4950
        },
        {
            "name": "Discord",
            "icon": "discord.svg",
            "link": "https://discord.com/invite/EYB8tQxjxH",
            "value": 1500
        },
        {
            "name": "Twitter",
            "icon": "twitter.svg",
            "link": "https://twitter.com/virtechschool",
            "value": 250
        },
        {
            "name": "Hashnode",
            "icon": "hashnode.svg",
            "link": "https://virtualtechschool.hashnode.dev/",
            "value": 70
        }
    ]
    return render_template(
        "home/home.html",
        stats=stats_list
    )