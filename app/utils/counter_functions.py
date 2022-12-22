import requests
import tweepy

from bs4 import BeautifulSoup

import os

def get_youtube_stat():
    channel_id = os.environ.get('CHANNEL_ID')
    key = os.environ.get('YT_API_KEY')
    res = requests.get(f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={key}")
    if res.status_code == 200:
        return res.json().get('items')[0].get('statistics').get('subscriberCount')
    else:
        return 5000

def get_discord_stat():
    server_id = os.environ.get("DISCORD_SERVER_ID")
    res = requests.get(f"https://discord.com/api/v9/invites/{server_id}?with_counts=true&with_expiration=true")
    if res.status_code == 200:
        return res.json().get("approximate_member_count")
    else:
        return 1500

def get_twitter_stat():
    try:
        token = os.environ.get("TWITTER_TOKEN")
        username = os.environ.get("TWT_USERNAME")

        twitter = tweepy.Client(bearer_token=token)

        return twitter.get_user(username=username, user_fields=["public_metrics"]).data.public_metrics['followers_count']
    except Exception as e:
        return 500

def get_hashnode_stat():
    try:
        URL = os.environ.get("HASHNODE_PROFILE")
        res = requests.get(URL)

        soup = BeautifulSoup(res.content, "html.parser")

        count = soup.find_all(class_='css-1j389vi')[0].string

        if "K" in count:
            return float(count.replace("K", "")) * 1000
        else:
            return float(count)
    except Exception as e:
        return 100