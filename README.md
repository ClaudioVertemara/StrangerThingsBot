# Stranger Things Bot
Twitter Bot written in Python 🐍 that counts down to the premiere of Stranger Things 4 Volume 1 &amp; 2.

Follow [@STCDBot](https://twitter.com/STCDBot) on Twitter.

Inspired by the [End of Year Countdown Bot](https://github.com/amadejpapez/EndOfYearCountdown) by [amadejpapez](https://github.com/amadejpapez).

## How does it work?
The Python script starts by creating the tweet text. It gets the current date and calculates the difference between today and the volume 1 premiere date. 

If the difference is more than 24 hours, the tweet will display the number of days left. If less than 24 hours remain, the tweet will display the number of hours and minutes left. Once volume 1 has premiered, the premiere date of volume 2 will be used instead.

The [Tweepy](https://www.tweepy.org) Python Library is then used to communicate with the [Twitter API](https://developer.twitter.com/en/docs/twitter-api) and post the tweet. 

The script is ran using [Github Actions](https://github.com/features/actions) and is scheduled to run on a daily basis at 6 AM UTC and on an hourly basis starting 24 hours before each premiere.
