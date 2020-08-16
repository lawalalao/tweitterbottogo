import tweepy
import time

auth = tweepy.OAuthHandler('vj2NKCzDX2t6nzqmVh9t3J2SX','f8XkUBc3b5qfiIVmq3jNpyL2oT5CpsWa3adEtH0gLI9rtA78gw')

auth.set_access_token('1292015343196667904-AUWP8enbHjIBSktkgxsIvCXBN9cfnB','U0PGltUUHGQH1nzqag1HPuKvjDJg6fnzueTp4zorHvItP')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = '#Tgtwittos'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('tweet retweeted')
        tweet.retweet()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
