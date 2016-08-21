import itertools

with open('TextFiles/holding_data.txt') as f:
    names = f.read()
    iter_twitter_names = iter(names.split('\n'))
    del names
