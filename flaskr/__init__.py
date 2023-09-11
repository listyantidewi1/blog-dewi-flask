# # import aplikasi flask, os, flash, jsonify, redirect, dan render_template untuk dipakai di web kita
# import os

# # import SQL utk akses database
# from cs50 import SQL
# # import flash utk notifikasi pada web
# # import jsonify utk memformat data
# # import redirect dan render_template untuk berpindah halaman web
# # import request dan session untuk mengakses data
# from flask import Flask, flash, jsonify, redirect, render_template, request, session

# # mengatur nama aplikasi
# app = Flask(__name__)

# db = SQL("sqlite:///flaskr/birthdays.db")

# # mengatur URI (universal resource identifier), dan apa yg ditampilkan jika URI tersebut diakses
# @app.route('/') # ketika alamat http://127.0.0.1:5000/ dipanggil, maka server akan mengeksekusi fungsi hello()
# def hello(): # function dengan nama hello
#     return 'Hello, World!'

# # mengatur URI ke http://127.0.0.1:5000/login, dan mengeksekusi fungsi login() jika diakses di alamat URI http://127.0.0.1:5000/login 
# @app.route('/login')
# def login():
#     return 'halaman login'

# # menampilkan isi tabel birthdays dari birthdays.db
# @app.route('/bday')
# def bday():
#     # Query utk select semua data, lalu simpan di variabel birthdays
#     birthdays = db.execute("SELECT * FROM birthdays")
#     # Render data dari variabel birthdays ke birthdays.html, yang akan ditangkap oleh variabel birthdays di birthdays.html
#     return render_template("birthdays.html", birthdays=birthdays)

import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it ecists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app