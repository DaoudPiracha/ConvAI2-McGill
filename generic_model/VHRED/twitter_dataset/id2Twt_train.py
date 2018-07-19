import csv
import time
from twython import Twython, TwythonError


CONSUMER_KEY = "FQvBqPUa0wey9XSakVnsXjK9O"
CONSUMER_SECRET =  "KrucRzBHxR2bH3U9zQpx2yQLh5B8anZkUBDVcYmUV4HsJJ6kVC"
OAUTH_TOKEN =  "4694088007-OY5tAN7em8Kq4RzyZA0Re7So7MHIfK002T3Tl0h"
OAUTH_TOKEN_SECRET = "hrVNXAEMwyxzd3ZZaN4yFZ4HiL12KXv9nih9uud56cYXn"
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


with open('TweetIDs_Train.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    raw = list(reader)

tweetss = []

for k in range(len(raw)):
    if k%1000 == 0:
        print ("progress: %d/10000" %(k))
        with open("tweets_train.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(tweetss)
    print (k)
    ids = raw[k]
    tweets = []
    i = 0
    while i < len(ids):
        id = int(ids[i])
        try:
            tweet = twitter.show_status(id=id)
            tweets.append(tweet['text'])
            print (tweets)
            i += 1
        except TwythonError as e:
            if e.error_code == 429:
                print (e)
                with open("tweets_train.csv", "w") as f:
                    writer = csv.writer(f)
                    writer.writerows(tweetss)
                time.sleep(15*60) 
                continue
            else:
                print (e)
                tweets = []
                i += 1
                break
    tweetss.append(tweets)

