import pytz,datetime, time,pdb

gmt = pytz.timezone('GMT')
pacific = pytz.timezone('US/Pacific')

def get_tweets(api, username,f_html):
    try:
        tweets = api.user_timeline(username)
        time.sleep(2)
        for tweet in tweets:
            gmt_date_tweet = gmt.localize(tweet.created_at)
            pacific_date  = gmt_date_tweet.astimezone(pacific)
            if (datetime.datetime.now().date() - datetime.timedelta(1) == pacific_date.date()):
                tweet_text = tweet.text.encode('ascii','ignore')
                try:
                    links_begin = tweet.text.find('https')
                    links = tweet.text[links_begin:].split(' ')
                except:
                    pass

                print(tweet_text)
                tweet_data = """
                  <div class="postWrapper">
                    <p class="postBody">
                      <span class="postAuthor">{0}</span> -
                      <span class="postTime">{1}</span>:
                      {2}
                    </p>
                    <div>
                      <a href="https://twitter.com/{3}/status/{4}">Link to Original</a>
                    </div>
                    """.format(tweet.user.name,pacific_date,tweet_text[:links_begin].decode("ascii", "ignore"),username,tweet.id)
                f_html.write(tweet_data)
                # pdb.set_trace()
                links_html = ['<a href="{}">Links from tweet</a><br>'.format(link) for link in links]
                try:
                    f_html.write('<div>')
                    for link_url in links_html:
                        f_html.write(link_url)
                    f_html.write('<hr style="border-top: dotted 1px;"/></div></div>')
                except:
                    f_html.write('<hr style="border-top: dotted 1px;"/></div>')
    except:
        time.sleep(10)
        pass
