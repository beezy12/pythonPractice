import praw
import config
import time
import os


def botLogin():
    print('logging in....')
    reddit = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = 'beezyTester:dog comment responder:v0.1')
    return reddit



def get_saved_comments():
    if not os.path.isfile('comments_replied_to.txt'):
        comments_replied_to = []
    else:
    	with open('comments_replied_to.txt', 'r') as file:
            comments_replied_to = file.read()
	    # so we read each line of the file, and when there's a new line, split creates a list, splitting on each new line
            comments_replied_to = comments_replied_to.split('\n')
	    # the filter here filters out the first argument from the second argument (comme...). had to wrap in list to show items because Python3
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to



def runBot(reddit, comments_replied_to):
    print('getting 25 comments')


    for comment in reddit.subreddit('test').comments(limit=15):
	    # BUG: not replying to comments when the user is me  ***********
        if "dog" in comment.body and comment.id not in comments_replied_to and comment.author != reddit.user.me():
            print('Found a doggy')
            comment.reply('I like degs too')
            print('replied to comment: ' + comment.id)

            comments_replied_to.append(comment.id)

            with open('comments_replied_to.txt', 'a') as file:
                file.write(comment.id + '\n')
    
    print('sleeping for 10 seconds')
    time.sleep(10)




reddit = botLogin()

comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
    runBot(reddit, comments_replied_to)


