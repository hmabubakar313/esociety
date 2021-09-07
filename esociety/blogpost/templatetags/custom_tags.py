from django import template
from django.template.loader import get_template
from textblob import TextBlob
import tweepy
consumer_key= '6g8yTtFKtdzdd5Y8O0CkZk7d0'
consumer_secret= 'FrzeRqhf8b1fRo5MD5xJ6mWZAL25BFFMDrOWsnQrrESIWaq97q' 

access_token='930155901666971648-cM8KS94m8UpDgCmYJ0Kl9HYuLBEaqkX'
access_token_secret='P6G4GUXLpTAdDLjKEyQd2rb7fMSRRG7cQhquymI0fjhOz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)




register = template.Library()



@register.simple_tag()
def get_expressions(format_string):
    arr1 = []
    print("inside function")
    public_tweets = api.user_timeline(screen_name = 'masif3110',count=3, tweet_mode="extended")
    for tweet in public_tweets:
        x=tweet.full_text
        print(x)
        analysis = TextBlob(tweet.full_text)
        print("analysis : ")
        print(analysis.sentiment)
        if (analysis.sentiment.subjectivity>0):
            print("if statement") 
            if (analysis.sentiment.subjectivity>0):
                arr1.append(analysis.sentiment.polarity)
                print(arr1)
                print("length of array : ")
                length_arr1=len(arr1)
                print(length_arr1)

                total_pol = sum(arr1)
                print("total polarity : ")
                print(total_pol)
                avg_pol = total_pol/len(arr1)
                print("=======Avg Pol=========")
                print (avg_pol)
        if (analysis.sentiment.polarity>0   and  analysis.sentiment.subjectivity>0):
            positive="positive"
            return positive
        else:
            negative='negative'
            return negative
        # avg_pol = total_pol/len(arr1)
        # now i need to do analysis on 'x'
        # return x
    # return x
    # return public_tweets



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