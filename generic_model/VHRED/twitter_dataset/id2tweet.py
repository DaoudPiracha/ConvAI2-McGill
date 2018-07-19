import csv
import time
from twython import Twython, TwythonError

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('id_file', type=str)
parser.add_argument('output_file', type=str)

args = parser.parse_args()


CONSUMER_KEY = #INSERT HERE#
CONSUMER_SECRET =  #INSERT HERE#
OAUTH_TOKEN =  #INSERT HERE#
OAUTH_TOKEN_SECRET = #INSERT HERE#

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


with open(args.id_file, 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    raw = list(reader)

tweetss = []

for k in range(len(raw)):
    if k%1000 == 0:
        print ("progress: %d/10000" %(k))
        with open(args.output_file, "w") as f:
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
                with open(args.output_file, "w") as f:
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

