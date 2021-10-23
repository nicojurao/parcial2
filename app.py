import mysql.connector
from flask import Flask, render_template, request, redirect, flash
from controllers import users
from models import users

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

###############################################################

@app.get('/')
def inicio():
    
    return render_template('index.html')

###############################################################

@app.route('/listar',methods=['POST'])
def mostrarDB():
    dataDB = users.listarDB()
    
    return render_template('index.html', users = dataDB)

###############################################################

@app.get('/crear')
def crearDB():
    return render_template('crearDB.html')

###############################################################

@app.route('/guardar',methods=['POST'])
def guardarDB():
    users.guardarDB()

    return render_template('index.html')


app.run(debug=True)