from django import template
from django.template.loader import get_template
from textblob import TextBlob
import tweepy
import requests
# from blogpost.views import extended_feed
# need to import views

# from blogpost.views import public_tweets
consumer_key= 'consumer_key'
consumer_secret= 'consumer_secret' 

access_token='access_token'
access_token_secret='access_token'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)







register = template.Library()








# @register.simple_tag()
# def get_expressions(format_string):
#     a = 'asd'
#     print("inside function")
#     return a
    
#             return negative
        # avg_pol = total_pol/len(arr1)
        # now i need to do analysis on 'x'
        # return x
    # return x
    # return public_tweets


