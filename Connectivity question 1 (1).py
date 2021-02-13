import mysql.connector

mydb=mysql.connector.connect (
    host='localhost',
    user='root',
    passwd='1234')

mycursor=mydb.cursor()

def dataret():
    mycursor.execute('SELECT * FROM city WHERE empid < 10')
    out=mycursor.fetchall()
    for i in out :
        print(i)

dataret()
