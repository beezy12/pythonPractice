#!/usr/bin/env python3

# very good tutorial on this here: https://praw.readthedocs.io/en/latest/tutorials/comments.html


import praw
import time

def authenticate():
    user_agent = ("karmabot by /u/botter_one")
    reddit = praw.Reddit('topBot', user_agent=user_agent)
    print('logged in as: {}'.format(reddit.user.me()))
    return reddit


def main():
    reddit = authenticate()
    while True:
        run_bot(reddit)


def run_bot(reddit):
    #submission = reddit.submission(url='https://www.reddit.com/r/funny/comments/6ioyus/megapunching_your_sparring_partner_through_the/')
     
    subreddit = reddit.subreddit('askreddit')
    for submission in subreddit.top(limit=5):
        print(submission.title)
        print(submission.score)
        print(submission.id)
        print(submission.url)
        print('******************')
    
    time.sleep(30)


print('prior to import: {}'.format(__name__)) 

if __name__ == '__main__':
    main()
