import mysql.connector as sql
con = sql.connector(host='localhost',database='esociety',user='root',password='admin123')

if con.is_connected()==False:
    print("Not connected")

con.close