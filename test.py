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
            with open('test_data.json', 'a') as my_file:
                json.dump(tweet, my_file)
                print(data)

        except BaseException:
            print('Error')
            pass

    def on_status(self, status):
        print
        status.text
        if status.coordinates:
            print
            'coords:', status.coordinates
        if status.place:
            print
            'place:', status.place.full_name

        return True

    on_event = on_status

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
