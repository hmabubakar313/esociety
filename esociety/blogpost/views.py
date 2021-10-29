from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls.static import static
import mysql.connector as mysql
from django.shortcuts import redirect, render
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import datetime
import sqlite3
import tweepy
import time
import sqlite3
from sqlite3 import Error
from textblob import TextBlob
# from .templatetags import custom_tags
import requests
#  Twitter API
consumer_key= '6g8yTtFKtdzdd5Y8O0CkZk7d0'
consumer_secret= 'FrzeRqhf8b1fRo5MD5xJ6mWZAL25BFFMDrOWsnQrrESIWaq97q' 

access_token='930155901666971648-cM8KS94m8UpDgCmYJ0Kl9HYuLBEaqkX'
access_token_secret='P6G4GUXLpTAdDLjKEyQd2rb7fMSRRG7cQhquymI0fjhOz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Create your views here.
def post(request):
    return render(request,"html/blogpost.html")

def profile(request):
    return render(request,"html/profile.html")

    
def save_post(request):
    if request.method == 'POST':
        slug = request.POST['slug']
        title = request.POST['title']
        description = request.POST['description']
        date_time=datetime.datetime.now()
       
        try:
            connection = mysql.connector.connect(host='localhost',
                                            database='esociety',
                                            user='root',
                                            password='admin123')
            insertQuery = """INSERT  INTO post_details  (post_title,post,date_time,user_id)
            VALUES
            ('{}', '{}','{}',2)""".format(title,description,date_time)
            print("Hello")
            print(insertQuery)
            print(description)
            cursor = connection.cursor()
            cursor.execute(insertQuery)
            connection.commit()
            cursor.close()
            print(cursor.rowcount, "Record inserted successfully into students table")
            print("Hello")
           
        except mysql.connector.Error as error:
                print("Failed to insert record from students table {}".format(error))

        finally:
            if (connection.is_connected()):
                print("MySQL connection is closed")
                return render(request, "html/post.html", {'title': title,'description':description})
                
            else:
                print("MYSQL is not closed")
    else:
        return HttpResponse('<h1>Page Not found</h1>')


def feed(request):
        public_tweets = api.user_timeline(screen_name = 'masif3110',count=1, tweet_mode="extended")
        try:
            connection = mysql.connector.connect(host='localhost',
                                            database='esociety',
                                            user='root',
                                            password='admin123')
            getQuery = """select * from post_details"""
            cursor = connection.cursor()
            cursor.execute(getQuery)
            result=cursor.fetchall()
            print(result)
            print("result runs")
            cursor.close()
            print(cursor.rowcount, "Record get successfully from post_details table")
          
           
        except mysql.connector.Error as error:
                print("Failed to get record from post_details table {}".format(error))

        finally:
            if (connection.is_connected()):
                print("MySQL connection is closed")
                
                return render(request, "html/feed.html",{'result':result,'public_tweets':public_tweets})
            else:
                print("MYSQL is not closed")


def extended_feed(request,id):
    public_tweets = api.get_status(id=id)
    text = public_tweets.text
    print(text)
    def get_tweet_sentiment(self, text):
        print('inside analysis function')
        analysis = TextBlob(self.text)
        print(analysis)
        print('textblob')
        # set sentiment
        if analysis.sentiment.polarity > 0:
            print('positive')   
        elif analysis.sentiment.polarity == 0:
            print('neutral')
        else:
            print('negative')
    print('rendering') 
    return render(request, 'html/extend_feed.html',{'public_tweets':public_tweets, 'name':'Asif'})


# get tweets json via id 









    









