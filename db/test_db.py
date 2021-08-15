import mysql.connector

esociety = mysql.connector.connect(
    host="localhost",
    user="root",
    ="admin123",
    database="esociety"
)

mycursor = esociety.cursor()
mycursor.execute("DROP TABLE IF EXISTS students")
mycursor.execute("CREATE TABLE students(username VARCHAR(255),email  VARCHAR(255),  VARCHAR(255),reg_no  VARCHAR(255))")
mycursor = esociety.cursor()
mycursor.execute("ALTER TABLE students ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x) 