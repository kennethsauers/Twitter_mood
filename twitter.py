from textblob import TextBlob
import tweepy
import time
import numpy as np
from openpyxl import Workbook

consumer_key = "f7lRrDHCgmiUiC4xPlXpnpE4v"
consumer_secret = "GYK7NpkSTSNsHlFytFLR6HvQjzjdg9h1fMJdVXCoo1JWvXQo1D"

access_token = "866444549106929664-v5fAOIYl4d6eGGjVWtSZemxchNbQzHf"
access_secret = "DXjnNavFGarO44luoP4EMYesx1Pqsrj17sRc6rL8mdiV5"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

wb = Workbook(write_only=True)
ws = wb.create_sheet()
def search_tweeter(query):
    try:
        public_tweets = api.search(query, count = 1000)
        avg_polatity = 0
        i = 0

        for tweet in public_tweets:

            #print(tweet.text)
            analysis = TextBlob(tweet.text)
            #print("---" ,analysis.sentiment.polarity)
            #print()
            if(analysis.sentiment.polarity != 0.0):
                avg_polatity = avg_polatity + analysis.sentiment.polarity
                i = i + 1
        #print("happyness:", avg_polatity/ i)
        return avg_polatity/ i
    except tweepy.TweepError:
        print('fuck')
        time.sleep(1)

def show_data(xxx):
    i = 0
    for thing in things:
        print(xxx[0][i],":", xxx[1][i])
        i = i + 1
def search():
    i = 0
    print("precent complete:")
    for thing in things:
        x = search_tweeter(thing)
        np.put(scores, [i] , x)
        i = i + 1
        print("     ", i*2 / scores.size)
def wwrite():


    # now we'll fill it with 100 rows x 200 columns
    i = 0
    ws.append(['%f' % scores[i] for i in range(10)])
def main():
    search()
    qq = np.array([things, scores])
    print()
    show_data(qq)
    wwrite()
things = np.array(['Blue', 'Green','Red', 'Black', 'White', 'Grey', 'Yellow', 'Purple', 'Orange', 'Brown', 'Pink'])
scores = np.arange(0,things.size,.5)
i = 0
print(things.size)

#ws.append('%s' % things[i] for i in range(10))
for i in range(100):
    main()
    time.sleep(60)
    
wb.save('new_big_file.xlsx') 