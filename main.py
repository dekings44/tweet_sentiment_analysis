import snscrape.modules.twitter as snt
import pandas as pd

query = "UK Economy"
tweets = []
limit = 5000

for tweet in snt.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.likeCount, tweet.sourceLabel,  tweet.content])

tweet_data = pd.DataFrame(tweets, columns=["Date", "User", "Number of likes", "Tweeted from", "Tweets"])
print(tweet_data.head())

tweet_data.to_csv('uk_economy.csv', index = None)




