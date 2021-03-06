
import praw
import time
print(praw.__path__)

r = praw.Reddit(user_agent = 'reddit bot by /u/Defintitely_Corrector')
r.login()


words_to_match = ['definataly', 'definately', 'definantly', 'definetly', 'definatly']
cache = []

def run_bot():
    subreddit = r.get_subreddit('test')
    comments = subreddit.get_comments(limit=50)
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if comment.id not in cache and isMatch:
            comment.reply('I think you meant to say "definitely"')
            cache.append(comment.id)

while True:
    run_bot()
    time.sleep(10)
