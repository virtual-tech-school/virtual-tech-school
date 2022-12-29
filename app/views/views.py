from flask import Blueprint, render_template

from app.utils.counter_functions import *

import os

views = Blueprint('views', __name__, url_prefix="/")

@views.route("/")
def home():
    stats_list = [
        {
            "name": "YouTube",
            "icon": "youtube.svg",
            "link": os.environ.get("YOUTUBE_LINK"),
            "value": get_youtube_stat()
        },
        {
            "name": "Discord",
            "icon": "discord.svg",
            "link": os.environ.get("DISCORD_LINK"),
            "value": get_discord_stat()
        },
        {
            "name": "Twitter",
            "icon": "twitter.svg",
            "link": os.environ.get("TWITTER_LINK"),
            "value": get_twitter_stat()
        },
        {
            "name": "Hashnode",
            "icon": "hashnode.svg",
            "link": os.environ.get("HASHNODE_LINK"),
            "value": get_hashnode_stat()
        }
    ]
    return render_template(
        "home/home.html",
        stats=stats_list
    )

@views.route("/about-us")
def about_us():
    return render_template(
        "about/about.html"
    )

@views.route("/bootcamp")
def bootcamp():
    return render_template(
        "bootcamp/bootcamp.html"
    )

@views.route("/courses")
def courses():
    return render_template(
        "courses/courses.html"
    )