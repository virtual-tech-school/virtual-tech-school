from flask import Blueprint, render_template

from app.utils.counter_functions import *
from app.utils.metadata_helper import *

import os

views = Blueprint('views', __name__, url_prefix="/")

@views.route("/")
def home():
    stats_list = [
        {
            "name": "YouTube",
            "icon": "youtube.svg",
            "link": "https://www.youtube.com/c/ApoorvGoyalMain",
            "value": get_youtube_stat()
        },
        {
            "name": "Discord",
            "icon": "discord.svg",
            "link": "https://discord.gg/EYB8tQxjxH",
            "value": get_discord_stat()
        },
        {
            "name": "Twitter",
            "icon": "twitter.svg",
            "link": "https://twitter.com/virtechschool",
            "value": get_twitter_stat()
        },
        {
            "name": "Hashnode",
            "icon": "hashnode.svg",
            "link": "https://rb.gy/awe3n"
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
    courses = fetch_metadata()
    return render_template(
        "courses/courses.html",
        courses=courses
    )

@views.route("/courses/<code>")
def course(code):
    try:
        course = fetch_course_data(code)
        template = "course/course.html"
    except ValueError:
        template = "404/404.html"
    
    return render_template(template, course=course, code=code)

