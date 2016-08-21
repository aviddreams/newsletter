# newsletter

## Description

A newsletter I email myself every morning to get caught up with what happened the day before. You'll need to sign up to use the Twitter API. You can download the HTML file for an example as to what this project looks like.

##Setup Instructions

Create a authentication.py file with:
* consumer_key=
* consumer_secret=
* access_token_key=
* access_token_secret=
* EMAIL_ACCOUNT = FROM.at.gmail.com
* EMAIL_PASSWORD = FROM_EMAIL_PASSWORD
* EMAIL_ACCOUNT_MAIN = TO.at.gmail.com

##Other Notes

Customize your own Twitter Users. Under the twitter_user.py file, you will link to the text file that has the twitter user handles you want to get data from. I just found a list online, but you can change it to whatever you want.
-----------
##To Run:
```
$ py -3.4 pynewsletter.py
```
This is for windows


## Future Additions
News Articles (Summarized)
Top Reddit Posts for the previous day
