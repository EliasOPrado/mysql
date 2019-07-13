import os
import pymysql

#Get username from cloud9 workspace
#(modify this variable if running in another environment).
username = os.getenv('C9_USER')

#connect to the database
connection = pymysql.connect('localhost',
                             user = username,
                             password ='',
                             db = 'Chinook')
                             
try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #close the connection, regardeless of whther the above was sucessful
    connection.close()