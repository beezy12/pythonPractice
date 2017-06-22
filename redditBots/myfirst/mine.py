'''
Change your client's User-Agent string to something unique and descriptive, including the target platform, a unique application identifier, a version string, and your username as contact information, in the following format:
    <platform>:<app ID>:<version string> (by /u/<reddit username>)
    Example: User-Agent: android:com.example.myredditapp:v1.2.3 (by /u/kemitche)
    Many default User-Agents (like "Python/urllib" or "Java") are drastically limited to encourage unique and descriptive user-agent strings.
    Including the version number and updating it as you build your application allows us to safely block old buggy/broken versions of your app.
    NEVER lie about your user-agent. This includes spoofing popular browsers and spoofing other bots. We will ban liars with extreme prejudice.
'''
#!/usr/bin/env python3

import praw
import time

def authenticate():
    user_agent = ("karmabot by /u/botter_one")
    reddit = praw.Reddit('karmabotter', user_agent=user_agent)
    print('logged in as: {}'.format(reddit.user.me()))
    return reddit


def main():
    reddit = authenticate()
    while True:
        run_bot(reddit)


def run_bot(reddit):
    for comment in reddit.subreddit('askreddit').comments(limit=25):
        print(comment.body)

    print('sleeping for 10 seconds')
    time.sleep(10)




print('prior to import: {}'.format(__name__)) 

if __name__ == '__main__':
    main()
