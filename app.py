import mysql.connector
from flask import Flask, render_template, request, redirect, flash
from controllers import users
from models import users

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.get('/')
def mostrarDB():
    dataUsers = users.getAllUsers()
    
    return render_template('index.html', users = dataUsers)




@app.get('/crear')
def crearDB():
    return render_template('crearDB.html')




@app.route('/guardar',methods=['POST'])
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


app.run(debug=True)