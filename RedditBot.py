import praw

reddit = praw.Reddit(
    client_id="B27kiRmd3TyxMxFlC2IrYw",
    client_secret="Zfv3P1FIxISLOZ3h4rIA111TZZMRuA",
    user_agent="<console:HAPPY:1.00009>"
)

subreddit = reddit.subreddit("television")

for post in subreddit.hot(limit=10):
    print("*****************")
    print(post.title)