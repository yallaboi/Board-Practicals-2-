import sys
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='isgsql')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists employee")
mycursor.execute("use employee")
mycursor.execute("create table if not exists emp(empno int(11),name varchar(23),dept varchar(23),salary int(11))")
for i in range(0,3):
    eid=input("Enter id:")
    names=input("Enter name:")
    dep=input("Enter department:")
    sal=input("Enter salary:")
    command='insert into emp values(%s,%s,%s,%s)'
    details=(eid,names,dep,sal)
    mycursor.execute(command,details)
    mydb.commit()

print('1.ALL EMPLOYEE DETAILS')
print('2.DETAIL OF EMPLOYEE HAVING SALARY GREATER THAN 10000')
print('3.EXIT FROM PROGRAM')
x=int(input("Choose your option:"))

if x==1:
    mycursor.execute("select* from emp;")
    myrecord=mycursor.fetchall()
    for x in myrecord:
        print(x)

elif x==2:
    mycursor.execute("select * from emp where salary>10000;")
    myrecord=mycursor.fetchall()
    for x in myrecord:
        print(x)
else:
    print("end of program")
    sys.exit()
