from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
import mysql.connector
import mysql.connector as mysql



def bases():
    conexion = mysql.connect(host='localhost', user ='root',password = '')

    cursor = conexion.cursor()

    cursor.execute("SHOW DATABASES")

    database = cursor.fetchall()

    print(database)

    for database in database:
        print(database)
print(bases())
print('***********************************************************')
print('tablas')

conexion2 = mysql.connect(host='localhost', user ='root',password = '', database = "escuela")
cursor2 = conexion2.cursor()
cursor2.execute("SHOW TABLES")
tables = cursor2.fetchall()

for table in tables:
    print(table)

print('*********************************')
db = mysql.connect(host='localhost', user ='root',password = '')
cursor = db.cursor()

cursor.execute("CREATE DATABASE nuevabd")