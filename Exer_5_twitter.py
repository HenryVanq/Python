# Exercise 5

import twitter
from collections import Counter

x = raw_input("username:  ")

# keys form twitter application

api = twitter.Api(consumer_key = 'XNKotSZrwQqY62rcwlVZxApFl',
  consumer_secret = 'pxQwKiP4AitLPCWL4yW14zL7eUaQET0jY2DjAg2oGwnginYgHB',
  access_token_key = '494256390-7cmIiCKzKAHb07suOpgj7iGxCJ6CsNegzxZtmg4T',
  access_token_secret = 'VMtmRoUIzL0P729600YZpXDV2QCCoqqrhGvmAncWZegTV')

# Function collects the last 10 tweets
t = api.GetUserTimeline(screen_name= x , count=10)

# converting tweets to list
tweets = [i.text for i in t]

# function splits words
words = ''.join(tweets).split()

for w in words:
    print(w)

# counter the words
for i in tweets:
    counter = Counter(words)

max_word = counter.most_common(1)
print("\n\n")
print("The word " + str(max_word[0][0]) + " showed up " + str(max_word[0][1]) + " times")