import praw

# Authenticate to Reddit
reddit = praw.Reddit(client_id='your_client_id', client_secret='your_client_secret', user_agent='your_user_agent')

# Collect comments
subreddit = reddit.subreddit('your_subreddit')
for comment in subreddit.comments(limit=100):
    print(comment.body)
