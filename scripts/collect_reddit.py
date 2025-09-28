# Install requests
!pip install requests
!pip install praw

import requests
import pandas as pd
import praw

brands = ["Crumbl Cookies", "Insomnia Cookies", "Levain Bakery"]

# Set up Reddit app credentials here
reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    user_agent="USERNAME"
)

def fetch_reddit(query, limit=100):
    posts = []
    for submission in reddit.subreddit("all").search(query, limit=limit):
        posts.append({
            "brand": query,
            "title": submission.title,
            "selftext": submission.selftext,
            "score": submission.score,
            "comments": submission.num_comments,
            "created_utc": submission.created_utc,
            "url": submission.url
        })
    return pd.DataFrame(posts)

reddit_df = pd.concat([fetch_reddit(b) for b in brands])
reddit_df['review'] = reddit_df['title'] + ' ' + reddit_df['selftext']
reddit_df.to_csv("reddit_mentions.csv", index=False)
reddit_df.head()
