import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Enter Twitter API Keys
access_token = "488650850-SdUNecgQyDGo7n5Rl85hlFKb51znw6fQZD8LH1nV"
access_token_secret = "wyShJScbtuDjfAeKQ6MCOufuEEhvxPYGPeLBGs6olRlbk"
consumer_key = "YV34hSKe6wXoKp3qSekqtGtMR"
consumer_secret = "QIbpHiRTmAAO2sfNsz49YeCz4a311QY8UY2yTpM75K8BEkELn3"


# Create the class that will handle the tweet stream
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


class listener(StreamListener):
    def on_data(self, data):
        try:
            tweet = json.loads(data)

            convertedTweet = {}
            convertedTweet['created_at'] = tweet['created_at']
            convertedTweet['text'] = tweet['text']
            convertedTweet['user'] = {}
            convertedTweet['user']['location'] = tweet['user']['location']
            convertedTweet['geo'] = tweet['geo']
            convertedTweet['coordinates'] = tweet['coordinates']
            if tweet.get('place'):
                convertedTweet['place'] = {}
                convertedTweet['place']['place_type'] = tweet['place']['place_type']
                convertedTweet['place']['name'] = tweet['place']['name']
                convertedTweet['place']['full_name'] = tweet['place']['full_name']
                convertedTweet['place']['country'] = tweet['place']['country']
            convertedTweet['reply_count'] = tweet['reply_count']
            convertedTweet['retweet_count'] = tweet['retweet_count']
            hasttagArray = []
            if tweet.get('entities'):
                if tweet['entities'].get('hashtags'):
                    for item in tweet['entities']['hashtags']:
                        hasttagArray.append(item['text'])
            convertedTweet['hashtags'] = hasttagArray

            with open('test_data.json', 'a') as my_file:
                json.dump(convertedTweet, my_file, indent=4)
                # print("data:")
                # print(data)
                print("convertedTweet:")
                print(json.dumps(convertedTweet))

        except BaseException:
            print('Error')
            pass

    # def on_status(self, status):
    #     print
    #     status.text
    #     if status.coordinates:
    #         print
    #         'coords:', status.coordinates
    #     if status.place:
    #         print
    #         'place:', status.place.full_name
    #
    #     return True
    #
    # on_event = on_status

    def on_error(self, status):
        print(status)


my_listener = listener()

if __name__ == '__main__':
    # Handle Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    json_listener = listener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, json_listener)
    stream.filter(track=['#COVID-19', '#USA'], locations=[-125.3, 24.8, -63.7, 49.1])
