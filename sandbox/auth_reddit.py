import praw

client_id = "wAtCD5Th6YIyd8kzpI6Mww"
client_secret = "4GMLAzkDmLXhSAOa8Kr-EOumniFY6w"
redirect_uri = "https://localhost:8080"
username = "minthousenfts"
password = "qaMbaq-2sudji-wucpuk"

reddit = praw.Reddit(client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    username=username,
    password=password,
    user_agent="testing/0.0.1"
)

subreddit = reddit.subreddit("oreo")
keyword = "oreo"

for post in subreddit.search(keyword, sort="new", limit=10):
    print(post.title)
    print(post.selftext)
    
    for comment in post.comments:
        print(comment.body)

