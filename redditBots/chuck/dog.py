import praw
import time
import os


def authenticate():
    print('authenticating....')
    # did have all the credentials below when I had a config, but changed to praw.ini and just have to pass in the name of the ini
    reddit = praw.Reddit('dogbot', user_agent = 'beezyTester:dog comment responder:v0.1')
    print('authenticated as: {}'.format(reddit.user.me()))
    return reddit


def get_saved_comments():
    # this means if the file doesn't exist, make a new list
    if not os.path.isfile('comments_replied_to.txt'):
        comments_replied_to = []
    else:
    # the 'r' here means 'read'
        with open('comments_replied_to.txt', 'r') as file:
            comments_replied_to = file.read()
            # the split here adds each comment as a new element in the list
            comments_replied_to = comments_replied_to.split('\n')
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to


def main():
    reddit = authenticate()
    comments_replied_to = get_saved_comments()
    print(comments_replied_to)
    while True:
        runBot(reddit, comments_replied_to)


def runBot(reddit, comments_replied_to):
    limit = 12
    print('getting ' + str(limit) + ' comments')
    for comment in reddit.subreddit('test').comments(limit = limit):
        if "dog" in comment.body and comment.id not in comments_replied_to and not comment.author == format(reddit.user.me()):
            print('Found a doggy')
            comment.reply('I like degs too')
            print('replied to comment: ' + comment.id)

            comments_replied_to.append(comment.id)

            with open('comments_replied_to.txt', 'a') as file:
                file.write(comment.id + '\n')
    
    print('sleeping for 10 seconds')
    time.sleep(10)




print('prior to import: {}'.format(__name__))

if __name__ == '__main__':
    main()




