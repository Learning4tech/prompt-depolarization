import tweepy

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Collect tweets
tweets = api.search_tweets(q="your_keyword", count=100)
for tweet in tweets:
    print(tweet.text)
