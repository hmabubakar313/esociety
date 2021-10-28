import mysql.connector as mysql
#establishing the connection
conn = mysql.connect(
   user='root', password='admin', host='localhost', database='esociety'
)

print(conn)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# *Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS students")


# Creating table as per requirement
# #Closing the connection
conn.close()
#* insering into database
# conn = mysql.connector.connect(
   # user='root', password='admin', host='localhost', database='esociety')

# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# # Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO students(
   USERNAME,E_MAIL , PASSWORD, REG_NO,)
   VALUES ('admin','admin@.com', 123,123 )"""

try:
   # Executing the SQL command
   cursor.execute(sql)
    #  Commit your changes in the database
   conn.commit()

except: 
     conn.rollback()
#    # Rolling back in case of error
  

# # Closing the connection
# conn.close()