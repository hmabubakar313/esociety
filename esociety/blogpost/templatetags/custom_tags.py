from django import template
from django.template.loader import get_template
from textblob import TextBlob
import tweepy
import requests
# from blogpost.views import extended_feed
# need to import views

# from blogpost.views import public_tweets
consumer_key= '6g8yTtFKtdzdd5Y8O0CkZk7d0'
consumer_secret= 'FrzeRqhf8b1fRo5MD5xJ6mWZAL25BFFMDrOWsnQrrESIWaq97q' 

access_token='930155901666971648-cM8KS94m8UpDgCmYJ0Kl9HYuLBEaqkX'
access_token_secret='P6G4GUXLpTAdDLjKEyQd2rb7fMSRRG7cQhquymI0fjhOz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)







register = template.Library()








@register.simple_tag()
def get_expressions(format_string,):
    a = 'asd'
    print("inside function")
    return a
    
#             return negative
        # avg_pol = total_pol/len(arr1)
        # now i need to do analysis on 'x'
        # return x
    # return x
    # return public_tweets


