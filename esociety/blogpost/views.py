from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls.static import static
import mysql.connector as mysql
from django.shortcuts import redirect, render
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# Create your views here.
def post(request):
    return render(request,"blogpost.html")

def profile(request):
    return render(request,"profile.html")


def save_post(request):
    if request.method == 'POST':
        slug = request.POST['slug']
        title = request.POST['title']
        description = request.POST['description']
       
        try:
            connection = mysql.connector.connect(host='localhost',
                                            database='esociety',
                                            user='root',
                                            password='admin123')
            insertQuery = """INSERT  INTO post_details  (post_title,post,user_id)
            VALUES
            ('{}', '{}',2)""".format(title,description)
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
                return render(request, "post.html", {'title': title,'description':description})
                print("Hello")
            else:
                print("MYSQL is not closed")
    else:
        return HttpResponse('<h1>Page Not found</h1>')
