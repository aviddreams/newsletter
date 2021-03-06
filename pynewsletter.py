import tweepy, datetime, time
from authentication import *
from get_tweets import get_tweets
from twitter_users import *
from emailalert import email_user_alert
from redditnews import *
import pdb
from html_template import *
from rssfeed import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

send_file = 'News_For_{}.html'.format(datetime.datetime.today().date())
with open(send_file, 'w+') as f_html:
    f_html.write(head_data)
    f_html.write(calendar)

    category = None
    counter = 0
    for twitter_user_name in iter_twitter_names:
        if twitter_user_name.startswith("!"):
            if counter > 0:
                f_html.write("</div>")

            category = twitter_user_name.strip("!")
            section_div = """
                <button class="accordion">{}</button>
                <div class="panel">
                """.format(category)
            f_html.write(section_div)
            counter += 1
        else:
            get_tweets(api, twitter_user_name,f_html)
    f_html.write('</div>')

    list_of_subreddits = ['News','Worldnews','All','Learnprogramming']
    for subreddit_name in list_of_subreddits:
        reddit_section_div = """
            <button class="accordion">{}</button>
            <div class="panel">
            """.format(subreddit_name)
        f_html.write(reddit_section_div)
        get_reddit_news(subreddit_name,f_html)
        f_html.write('</div>')

    bbc_links = [('http://feeds.bbci.co.uk/news/rss.xml','BBC News'),('http://feeds.bbci.co.uk/news/world/rss.xml','BBC WorldNews'),('http://feeds.bbci.co.uk/news/business/rss.xml','BBC Business'),('http://feeds.bbci.co.uk/news/technology/rss.xml','BBC Technology')]
    for feed in bbc_links:
        news_section_div = """
            <button class="accordion">{}</button>
            <div class="panel">
            """.format(feed[1])
        f_html.write(news_section_div)
        parse_feeds(feed[0],f_html)
        f_html.write('</div>')

    f_html.write(ending_html)
    f_html.truncate()

message = "News Letter Completed."
subject_line = 'News For The Day'
email_user_alert(message,subject_line,send_file)
