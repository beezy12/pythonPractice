import praw
import config
import time


def botLogin():
    print('logging in....')
    reddit = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = 'beezyTester:dog comment responder:v0.1')
    #print('logged in as ' + reddit.user.me())
    return reddit



def runBot(reddit, comments_replied_to):
    print('getting 25 comments')


    for comment in reddit.subreddit('test').comments(limit=25):
        if "dog" in comment.body and comment.id not in comments_replied_to and not comment.author == reddit.user.me():
            print('Found a doggy')
            comment.reply('I like degs too')
            print('replied to comment: ' + comment.id)

            comments_replied_to.append(comment.id)
    
    print('sleeping for 10 seconds')
    time.sleep(10)



def get_saved_comments():
    if not os.path.isfile('comments_replied.txt'):
    # the 'r' here means 'read'
    	with open('comments_replied.txt', 'r') as file:
	    comments_replied_to = file.read()
	    # the split here adds each comment as a new element in the list
	    comments_replied_to = comment_replied_to.split('\n')

    return comments_replied_to



reddit = botLogin()

#print(reddit)

#comments_replied_to = []
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
    runBot(reddit, comments_replied_to)


