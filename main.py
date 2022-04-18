import os
import tweepy
from datetime import date

def tweet(tweet_text):
    API = tweepy.Client(
        consumer_key = os.environ['API_KEY'],
        consumer_secret = os.environ['API_KEY_SECRET'],
        access_token = os.environ['ACCESS_TOKEN'],
        access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
    )

    API.create_tweet(text=tweet_text)

def create_tweet():
    today = date.today()
    st4_vol1 = date(2022, 5, 27)
    st4_vol2 = date(2022, 7, 1)
    
    days_left = (st4_vol1 - today).days
    
    if days_left > 0:
        return f"{days_left} days left until Stranger Things 4 Volume 1 premieres on May 27, 2022"
    elif days_left == 0:
        return f"Stranger Things 4 Volume 1 is Out Now!"
    
    days_left = (st4_vol2 - today).days
    
    if days_left > 0:
        return f"{days_left} days left until Stranger Things 4 Volume 2 premieres on July 1, 2022"
    elif days_left == 0:
        return f"Stranger Things 4 Volume 2 is Out Now!"
    
    return None

text = create_tweet()
if text:
    tweet(text)