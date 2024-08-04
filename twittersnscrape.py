import snscrape.modules.twitter as sntwitter

# Collect tweets
tweets = sntwitter.TwitterSearchScraper('your_keyword').get_items()
for tweet in tweets:
    print(tweet.content)
