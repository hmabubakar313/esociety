from django import template
from textblob import TextBlob
import tweepy
from django.template.loader import get_template
# # Step 1 - Authenticate

#  Twitter API
consumer_key= '6g8yTtFKtdzdd5Y8O0CkZk7d0'
consumer_secret= 'FrzeRqhf8b1fRo5MD5xJ6mWZAL25BFFMDrOWsnQrrESIWaq97q' 

access_token='930155901666971648-cM8KS94m8UpDgCmYJ0Kl9HYuLBEaqkX'
access_token_secret='P6G4GUXLpTAdDLjKEyQd2rb7fMSRRG7cQhquymI0fjhOz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.user_timeline(screen_name = 'masif3110',count=5, tweet_mode="extended")

register = template.Library()
# from .models import TextBlob
# print(public_tweets)

arr1 = []
@register.simple_tag
def get_expressions(public_tweets):
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)    
        print(analysis.sentiment)
        if (analysis.sentiment.subjectivity>0):
            arr1.append(analysis.sentiment.polarity)
        
        print("polarity is ====")
        print(analysis.sentiment.polarity)
        length_arr1=len(arr1)    

        total_pol = sum(arr1)
        avg_pol = total_pol/len(arr1)

        print("=======Avg Pol=========")
        print (avg_pol)
        
        if (analysis.sentiment.polarity>0   and  analysis.sentiment.subjectivity>0):
            positive = analysis.sentiment.polarity
            print("positive"+positive)
            return positive
        else:
            negative = analysis.sentiment.subjectivity
            print("negative"+negative)
users_template = get_template('html/extend_feed.html')

# register.filter('modify_name', modify_name)
                

""" # if arg is first_name: return the first string before space

    if arg == "first_name":

        return value.split(" ")[0]

    # if arg is last_name: return the last string before space

    if arg == "last_name":

        return value.split(" ")[-1]

    # if arg is title_case: return the title case of the string

    if arg == "title_case":

        return value.title()

    return value

    

register.filter('modify_name', modify_name) """