import mysql.connector
from flask import Flask, render_template, request, redirect, flash




def listarDB():
    
    direccion = request.form['ip']
    usuario = request.form['user']
    contrasena = request.form['pass']
    puerto = request.form['port']

    DB = mysql.connector.connect(
    host=f'{direccion}',
    user=f'{usuario}',
    password=f'{contrasena}',
    database='',
    port=f'{puerto}'
    )
    cursor = DB.cursor(dictionary=True)

    cursor.execute('SHOW DATABASES')

    return cursor.fetchall()

def guardarDB():
    
    nombre = request.form['namedb']
    direccion = request.form['ip']
    usuario = request.form['user']
    contrasena = request.form['pass']

    
    DB = mysql.connector.connect(
    host=f'{direccion}',
    user=f'{usuario}',
    password=f'{contrasena}',
    database='',
    port=3306
    )

    cursor=DB.cursor(dictionary=True)

    cursor.execute(f"CREATE DATABASE {nombre}")
    DB.commit()
    cursor.close()
    return redirect('/crear')