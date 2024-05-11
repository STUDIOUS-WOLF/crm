import mysql.connector
database =mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Amit@123'
)

cursorObject=database.cursor()
cursorObject.execute("CREATE DATABASE firstdb")
print('sll done')