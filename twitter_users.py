import itertools

with open('TextFiles/twitter_users.txt') as f:
    names = f.read()
    iter_twitter_names = iter(names.split('\n'))
    del names
