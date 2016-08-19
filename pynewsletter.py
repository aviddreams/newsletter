import tweepy, datetime, time
from authentication import *
from get_tweets import get_tweets
from twitter_users import *
from emailalert import email_user_alert
import pdb
from html_template import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

send_file = 'twitter_html.html'
with open(send_file, 'w+') as f_html:
    f_html.write(head_data)
    f_html.write(calendar)

    for twitter_user_name in iter_twitter_names:
        get_tweets(api, twitter_user_name,f_html)

    f_html.write(ending_html)
    f_html.truncate()

message = "Twitter Data Completed."
subject_line = 'Twitter News For The Day'
email_user_alert(message,subject_line,send_file)
