# Stranger Things Bot
Twitter Bot written in Python 🐍 that counts down the days left until the premiere of Stranger Things 4 Volume 1 &amp; 2.

Follow the bot [@STCDBot](https://twitter.com/STCDBot) on Twitter.

## How does it work?
The Python script gets the current date and calculates the difference in days between today and the volume 1 premiere date. Once volume 1 has premiered, the premiere date of volume 2 will be used instead.

The [Tweepy](https://www.tweepy.org) Python Library is then used to communicate with the [Twitter API](https://developer.twitter.com/en/docs/twitter-api) and post a tweet. 

The script is ran using [Github Actions](https://github.com/features/actions) and is scheduled to run on a daily basis at 7 AM UTC. 
