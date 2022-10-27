import snscrape.modules.twitter as snt
import pandas as pd

query = "obidient"
tweets = []
limit = 5000

for tweet in snt.TwitterSearchScraper(query).get_items():
    
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

tweet_data = pd.DataFrame(tweets, columns=["Date", "User", "Tweet"])

tweet_data.to_csv('obidient.csv', index = None)

