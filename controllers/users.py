from flask import flash
from models import users
import hashlib

def listarDB():
    dataDB = users.listarDB()
    
    return dataDB

def guardarDB():
    guardarDB=users.guardarDB()

    return guardarDB





