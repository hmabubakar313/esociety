import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='esociety',
                                         user='root',
                                         password='admin')
    cursor = connection.cursor()
    sql_Delete_query = """Delete from Laptop where id = %s"""
    laptopId = 6
    cursor.execute(sql_Delete_query, (laptopId,))
    connection.commit()
    print("Record Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to Delete record from table: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")