import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import io
import os



#consumer key, consumer secret, access token, access secret.
#ckey="Consumer key" # remove this before git push
#csecret="Consumer secret" # remove this before git push
#atoken="access-token" # remove this before git push
#asecret="access secret" # remove this before git push


ckey = 'p2ArgngYidQp1wfzhFrSOd8qu'# remove this before git push
consumer_secret = '8gUorAGkzV9xWUp3VPnK0Jl8Y0Tj242mjczpw6ZaQbZFkpsWVy' # remove this before git push
access_token_key = '25107624-jMrjYG2do0xY3eiJCTJSf9bvf8jtuOz93Zg5JepfK' # remove this before git push
access_token_secret = 'hj3vlMrmhkJZR9ii2A0bQ8rfFb9gIYvTZHZgRp6jsBXcO' # remove this before git push

start_time = time.time() #grabs the system time
keyword_list = ['election'] #track list

class listener(StreamListener):
 
	def __init__(self, start_time, time_limit=60):
 
		self.time = start_time
		self.limit = time_limit
		self.tweet_data = []
 
	def on_data(self, data):
 
		saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')
 
		while (time.time() - self.time) < self.limit:
 
			try:
 
				self.tweet_data.append(data)
 
				return True
 
 
			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass
 
		saveFile = io.open('raw_tweets.json', 'w', encoding='utf-8')
		saveFile.write(u'[\n')
		saveFile.write(','.join(self.tweet_data))
		saveFile.write(u'\n]')
		saveFile.close()
		exit()
 
	def on_error(self, status):
 
		print statuses

auth = OAuthHandler(ckey, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

twitterStream = Stream(auth, listener(start_time, time_limit = 20))
twitterStream.filter(track=keyword_list, languages = ['en'])
	

