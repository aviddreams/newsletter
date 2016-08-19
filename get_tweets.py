import pytz,datetime, time

gmt = pytz.timezone('GMT')
pacific = pytz.timezone('US/Pacific')

def get_tweets(api, username,f_html):
    tweets = api.user_timeline(username)

    for tweet in tweets:
        gmt_date_tweet = gmt.localize(tweet.created_at)
        pacific_date  = gmt_date_tweet.astimezone(pacific)
        if (datetime.datetime.now().date() == pacific_date.date()):
            print(tweet.text.encode("utf-8"))
            tweet_data = """
              <div class="postWrapper">
                <p class="postBody">
                  <span class="postAuthor">Kevin Chen</span> -
                  <span class="postTime">08/16/2016</span>:
                  {}
                </p>
                <div>
                  <a href="">Link to Original</a>
                </div>
              </div>
                """.format(tweet.text.encode("utf-8"))
            f_html.write(tweet_data)
