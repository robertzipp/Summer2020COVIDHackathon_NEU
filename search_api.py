import json
from datetime import datetime

import tweepy
from tweepy import OAuthHandler

if __name__ == '__main__':

    access_token = "488650850-SdUNecgQyDGo7n5Rl85hlFKb51znw6fQZD8LH1nV"
    access_token_secret = "wyShJScbtuDjfAeKQ6MCOufuEEhvxPYGPeLBGs6olRlbk"
    consumer_key = "YV34hSKe6wXoKp3qSekqtGtMR"
    consumer_secret = "QIbpHiRTmAAO2sfNsz49YeCz4a311QY8UY2yTpM75K8BEkELn3"
    file_name = int(datetime.utcnow().timestamp() * 1e3)

    ## set API connection
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth,
                     wait_on_rate_limit=True)  # set wait_on_rate_limit =True; as twitter may block you from querying if it finds you exceeding some limits

    tweets = tweepy.Cursor(api.search_30_day, "dev", "#covid19 place_country:US").items(10000)

    convertedTweetList = []

    for tweet in tweets:
        print(tweet)
        convertedTweet = {}
        convertedTweet['created_at'] = tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")
        convertedTweet['text'] = tweet.text.lower()
        convertedTweet['geo'] = tweet.geo
        convertedTweet['coordinates'] = tweet.coordinates
        convertedTweet['place'] = {}
        if tweet.place is None:
            convertedTweet['place']['full_name'] = tweet.author.location
        else:
            convertedTweet['place']['place_type'] = tweet.place.place_type
            convertedTweet['place']['name'] = tweet.place.name
            convertedTweet['place']['full_name'] = tweet.place.full_name
            convertedTweet['place']['country'] = tweet.place.country
            convertedTweet['place']['bounding_box'] = {}
            convertedTweet['place']['bounding_box']["type"] = tweet.place.bounding_box.type
            convertedTweet['place']['bounding_box']["coordinates"] = tweet.place.bounding_box.coordinates
        convertedTweet['reply_count'] = tweet.reply_count
        convertedTweet['retweet_count'] = tweet.retweet_count
        hasttagArray = []
        if tweet.entities is not None:
            if tweet.entities.get("hashtags") is not None:
                for item in tweet.entities.get("hashtags"):
                    hasttagArray.append(item['text'])
        convertedTweet['hashtags'] = hasttagArray
        convertedTweetList.append(convertedTweet)

    with open(f'covid_searchApi-{file_name}.json', 'a') as my_file:
        json.dump(convertedTweetList, my_file, indent=4)
    print(json.dumps(convertedTweet))
    # print("created_at: {}\nuser: {}\ntweet text: {}\ngeo_location: {}".
    #       format(tweet.created_at, tweet.user.screen_name, tweet.text, tweet.user.location))
    # print("\n")
