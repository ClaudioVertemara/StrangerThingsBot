import os
import tweepy
from datetime import datetime

def tweet(tweet_text):
    API = tweepy.Client(
        consumer_key = os.environ['API_KEY'],
        consumer_secret = os.environ['API_KEY_SECRET'],
        access_token = os.environ['ACCESS_TOKEN'],
        access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
    )

    API.create_tweet(text=tweet_text)

def create_tweet():
    now = datetime.utcnow()
    st4_vol1 = datetime(2022, 5, 27, 7)
    st4_vol2 = datetime(2022, 7, 1, 7)
    
    if ((st4_vol1 - now).days >= -1): 
        premiere_date = st4_vol1
        premiere_date_str = "May 27, 2022"
        volume = 1
    else:
        premiere_date = st4_vol2
        premiere_date_str = "July 1, 2022"
        volume = 2
    
    days_left = (premiere_date - now).days
    time_left = str(premiere_date - now).split(":")
    
    if days_left > 0:
        return f"{days_left} days left until Stranger Things 4 Volume {volume} premieres on {premiere_date_str}"
    elif days_left == 0:
        return f"{time_left[0]} hours and {time_left[1]} minutes left until Stranger Things 4 Volume {volume} premieres on {premiere_date_str}"
    elif days_left == -1:
        return f"Stranger Things 4 Volume {volume} is Out Now!"
    
    return None

text = create_tweet()
if text:
    tweet(text)