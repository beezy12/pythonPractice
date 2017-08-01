
import praw
import pprint


def authenticate():
    user_agent = ('just a test bot to learn by /u/botter_one')
    reddit = praw.Reddit('testesbot', user_agent=user_agent)
    
    print('authed')
    return reddit


def main():
    print('hello')
    r = authenticate()
    print('about to run_bot')
    while True:
        run_bot(r)


def run_bot(r):
    limit = 25
    
    for comment in r.subreddit('test').comments(limit):
        print(comment)

    print('sleeping for 10....')
    time.sleep(10)

if __name__ == '__main__':
    main()
