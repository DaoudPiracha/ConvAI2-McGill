import csv
import time
from twython import Twython, TwythonError
CONSUMER_KEY = "uEb6mkV5x9bTe9O8nQMTCk3Ej"
CONSUMER_SECRET =  "Qduw8AunPUn3KxFHQsegY6KW0yV3503HjCgFMYpNlcSRy0PdDS"
OAUTH_TOKEN =  "4694088007-0rcjZzbxP7p3y53QrJHzrhibqVhBN7xzbps39mm"
OAUTH_TOKEN_SECRET = "E9ZeVltbKEtgAf2pN3r09FSvCmc5GpjWdarMp5iTP60EL"
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


with open('TweetIDs_Test.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    raw = list(reader)

tweetss = []

for k in range(len(raw)):
    if k%1000 == 0:
        print ("progress: %d/10000" %(k))
        with open("tweets_test.csv", "w") as f:
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
                with open("tweets_test.csv", "w") as f:
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

