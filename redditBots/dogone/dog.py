import praw
import config
import time

def botLogin():
    print('logging in....')
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = 'beezyTester:dog comment responder:v0.1')

    #print('logged in as ' + r.user.me())
    return r

def runBot(r, comments_replied_to):
    print('getting 25 comments')


    for comment in r.subreddit('test').comments(limit=25):
        if "dog" in comment.body and comment.id not in comments_replied_to:
            print('Found a doggy')
            comment.reply('I like degs too')
            print('replied to comment: ' + comment.id)

            comments_replied_to.append(comment.id)
    
    print('sleeping for 10 seconds')
    time.sleep(10)

r = botLogin()

#print(r)

comments_replied_to = []
while True:
    runBot(r, comments_replied_to)


