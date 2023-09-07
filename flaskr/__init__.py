# import aplikasi flask, os, flash, jsonify, redirect, dan render_template untuk dipakai di web kita
import os

# import SQL utk akses database
from cs50 import SQL
# import flash utk notifikasi pada web
# import jsonify utk memformat data
# import redirect dan render_template untuk berpindah halaman web
# import request dan session untuk mengakses data
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# mengatur nama aplikasi
app = Flask(__name__)

# mengatur URI (universal resource identifier), dan apa yg ditampilkan jika URI tersebut diakses
@app.route('/') # ketika alamat http://127.0.0.1:5000/ dipanggil, maka server akan mengeksekusi fungsi hello()
def hello(): # function dengan nama hello
    return 'Hello, World!'

# mengatur URI ke http://127.0.0.1:5000/login, dan mengeksekusi fungsi login() jika diakses di alamat URI http://127.0.0.1:5000/login 
@app.route("/login")
def login():
    return 'halaman login'