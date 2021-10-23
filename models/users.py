import mysql.connector
from flask import Flask, render_template, request, redirect, flash


DB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='',
    port=3306
)

def getAllUsers():
    
    cursor = DB.cursor(dictionary=True)

    cursor.execute('SHOW DATABASES')

    return cursor.fetchall()

def addDB():

    cursor = DB.cursor(dictionary=True)

    cursor.execute('CREATE DATABASE gomenasai;')

    DB.commit()
    cursor.close()