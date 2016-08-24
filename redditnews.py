import praw,pdb,datetime
r = praw.Reddit(user_agent='my_cool_newsletter_application')

def get_reddit_news(subreddit_name,f_html):
    submissions = r.get_subreddit(subreddit_name).get_hot(limit=20)
    for reddit_post in submissions:
        reddit_post_data = """
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
            """.format(reddit_post.author,datetime.datetime.fromtimestamp(reddit_post.created).strftime('%Y-%m-%d'),reddit_post.title,reddit_post.url)
        f_html.write(reddit_post_data)
