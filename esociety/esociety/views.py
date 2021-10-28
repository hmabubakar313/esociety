from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls.static import static
import mysql.connector as mysql
from django.shortcuts import redirect, render
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# from .models import students


def login(request):
    return render(request, "login.html")

    # return render(request,"login.html")


def signup(request):
    # x=(request.GET.username)
    return render(request, "signup.html")


def save(request):
    if request.method == 'POST':
        username = request.POST['username']
        password         = request.POST['password']
        e_mail = request.POST['email']
        birthday = request.POST['birthday']
        reg_no = request.POST['reg_no']
        person = {
            'username': username,
            'password': password,
            'email': e_mail,
            'birthday': birthday,
            'reg_no': reg_no,
        }
        print(username)
        conn = mysql.connector.connect(
                user='root', password='admin123', host='localhost', database='esociety')
        cursor = conn.cursor()
        getQuery = """ FROM students WHERE username='username' and password='password'""" 
        cursor = conn.cursor()
        cursor.execute(getQuery)
        print("students Table record get successfully ")
        conn.close()
        print(username)
        print(password)  
    if (username == username): 
        try:
            conn = mysql.connector.connect(
                user='root', password='admin123', host='localhost', database='esociety')
            cursor = conn.cursor()
            # Dropping EMPLOYEE table if already exists.
            cursor.execute("DROP TABLE IF EXISTS students")
            # Creating table as per requirement
            tableQuery = """CREATE TABLE students (
                                user_id int(11) NOT NULL AUTO_INCREMENT,
                                username varchar(250) NOT NULL,
                                e_mail varchar(255) NOT NULL,
                                password varchar(20) NOT NULL,
                                birthday DATE NOT NULL,
                                reg_no varchar(255) NOT NULL """
            cursor = conn.cursor()
            cursor.execute(tableQuery)
            print("students Table created successfully ")
            conn.close()
            conn = mysql.connector.connect(host='localhost',
                                                database='esociety',
                                                user='root',
                                                password='admin123')
            cursor = conn.cursor()
        except mysql.connector.Error as error:
                    print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (conn.is_connected()):
                cursor.close()
                conn.close()
                print("MySQL connection is closed")
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='esociety',
                                         user='root',
                                         password='admin123')
            insertQuery = """INSERT INTO students (username,e_mail ,password, birthday, reg_no)
            VALUES
            ('{}','{}', '{}', '{}','{}') """.format(username, e_mail, password, birthday, reg_no) 
            print(insertQuery)
            cursor = connection.cursor()
            cursor.execute(insertQuery)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into students table")
            cursor.close()

        except mysql.connector.Error as error:
             print("Failed to insert record into students table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
                
            return render(request, "test.html", {'person': person})

    else:
    # print(request.POST.get)
            return HttpResponse('<h1>Page NOT found</h1>')

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        e_mail = request.POST['e_mail']
        reg_no = request.POST['reg_no']
        person = {
            'username': username,
            'password': password,
            'e_mail': e_mail,
            'reg_no': reg_no,
        }
        print("H")
        try:
            connection = mysql.connector.connect(host='localhost',
                                            database='esociety',
                                            user='root',
                                            password='admin123')
            getQuery = """SELECT students FROM esociety WHERE (username,e_mail ,password, reg_no)
            VALUES
            ('{}', '{}', '{}','{}')""".format(username, e_mail, password, reg_no)
            print(getQuery)
            print(username,e_mail,password,reg_no)
            if (username==username and password==password):
                return render(request, "index.html", {'person': person})
            else:
                return HttpResponse('<h1>Page Not found</h1>')
            cursor = connection.cursor()
            cursor.execute(getQuery)
            connection.commit()
            cursor.close()
            print(cursor.rowcount, "Record get successfully from students table")
            
            
            print("before except")
        except mysql.connector.Error as error:
                print("Failed to get record from students table {}".format(error))

        finally:
            if (connection.is_connected()):
                print("connection if")
                connection.close()
                print("MySQL connection is closed")
            else:
                print("MYSQL is not closed")
    else:
        return HttpResponse('<h1>Page Not found</h1>')


def list(request):
    try:
            connection = mysql.connector.connect(host='localhost',
                                            database='esociety',
                                            user='root',
                                            password='admin123')
            getQuery = """SELECT * From students """
            print(getQuery)
            cursor = connection.cursor()
            cursor.execute(getQuery)
            result=cursor.fetchall()
            connection.commit()
            cursor.close()
            # print(cursor)
            return render(request, "list.html", {'person': result,'id':id})
            print(cursor.rowcount, "Record get successfully from students table")
    except mysql.connector.Error as error:
        print("Failed to get record from students table {}".format(error))

    finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
            else:
                print("MYSQL is not closed")

def add_user(request):
    return render(request, "add_user.html")


def save_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        e_mail = request.POST['email']
        birthday = request.POST['birthday']
        reg_no = request.POST['reg_no']
        person = {
            'username': username,
            'password': password,
            'email': e_mail,
            'birthday': birthday,
            'reg_no': reg_no,
        }
        print(username)
        conn = mysql.connector.connect(
                user='root', password='admin123', host='localhost', database='esociety')
        cursor = conn.cursor()
        getQuery = """ FROM students WHERE username='username' and password='password'""" 
        cursor = conn.cursor()
        cursor.execute(getQuery)
        print("students Table record get successfully ")
        conn.close()
        print(username)
        print(password)  
    if (username == username): 
        try:
            conn = mysql.connector.connect(
                user='root', password='admin123', host='localhost', database='esociety')
            cursor = conn.cursor()
            # Dropping EMPLOYEE table if already exists.
            cursor.execute("DROP TABLE IF EXISTS students")
            # Creating table as per requirement
            tableQuery = """CREATE TABLE students (
                                user_id int(11) NOT NULL AUTO_INCREMENT,
                                username varchar(250) NOT NULL,
                                e_mail varchar(255) NOT NULL,
                                password varchar(20) NOT NULL,
                                birthday DATE NOT NULL,
                                reg_no varchar(255) NOT NULL """
            cursor = conn.cursor()
            cursor.execute(tableQuery)
            print("students Table created successfully ")
            conn.close()
            conn = mysql.connector.connect(host='localhost',
                                                database='esociety',
                                                user='root',
                                                password='admin123')
            cursor = conn.cursor()
        except mysql.connector.Error as error:
                    print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (conn.is_connected()):
                cursor.close()
                conn.close()
                print("MySQL connection is closed")
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='esociety',
                                         user='root',
                                         password='admin123')
            insertQuery = """INSERT INTO students (username,e_mail ,password, birthday, reg_no)
            VALUES
            ('{}','{}', '{}', '{}','{}') """.format(username, e_mail, password, birthday, reg_no) 
            print(insertQuery)
            cursor = connection.cursor()
            cursor.execute(insertQuery)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into students table")
            cursor.close()

        except mysql.connector.Error as error:
             print("Failed to insert record into students table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
                
            return render(request, "test.html", {'person': person})

    else:
    # print(request.POST.get)
             return HttpResponse('<h1>Page NOT found</h1>')
           
def delete_user(request,id):
    try:
            connection = mysql.connector.connect(host='localhost',
                                            database='esociety',
                                            user='root',
                                            password='admin123')
            deleteQuery =  "DELETE FROM students WHERE user_id=%s"
            
            print(deleteQuery)
            cursor = connection.cursor()
            cursor.execute(deleteQuery,(id,))
            connection.commit()
            cursor.close()
            return redirect("users-list")
            print(cursor.rowcount, "Record deleted successfully from students table")
    except mysql.connector.Error as error:
        print("Failed to get record from students table {}".format(error))

    finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
            else:
                print("MYSQL is not closed")
    




