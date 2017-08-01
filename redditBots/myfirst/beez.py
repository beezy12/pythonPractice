
import praw
import time

def authenticate():                                                                                                                                                          
    user_agent = ("karmabot by /u/botter_one")                                                                                                                               
    reddit = praw.Reddit('karmabotter', user_agent=user_agent)                                                                                                               
    print('logged in as: {}'.format(reddit.user.me()))                                                                                                                       

    return reddit 


def main():
    print('logging in.....')
    reddit = authenticate()
    while True:
        run_bot(reddit)


def run_bot(bot):
    limit = 25
    print('logged in and starting app.....')
    subreddit = bot.subreddit('test')
    comments = subreddit.comments(limit)

    for comment in comments:
        text = comment.body
        author = comment.author

        if 'mars' in text.lower():
            message = 'wasssup mars person, {}'.format(author)
            comment.reply(message)

    print('sleeping for 10....')
    time.sleep(10)


if __name__ == '__main__':
    main()
