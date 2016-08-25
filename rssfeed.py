import feedparser,pdb

def parse_feeds(feed,f_html):
    rss_feed = feedparser.parse(feed)
    for story in rss_feed['entries']:
        news_post_data = """
            <div class="postWrapper">
                <p class="postBody">
                  <span class="postAuthor">{0}</span> -
                  <span class="postTime">{1}</span>:
                  {2}
                </p>
                <div>
                  <a href="{3}">Link to Original</a>
                </div>
                <hr style="border-top: dotted 1px;"/>
            </div>
            """.format(story['title'],story['published'],story['summary_detail']['value'],story['links'][0]['href'])
        f_html.write(news_post_data)
