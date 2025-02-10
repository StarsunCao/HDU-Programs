# -*- coding: utf-8 -*-
from flask import Flask, redirect
from flask import request
from flask.templating import render_template
from flask.helpers import url_for
import datetime
import urllib
import json

f = open(r"C:\Users\a\OneDrive\Learning Materials\2022.2-2022.7\短学期\淘宝爬虫\Login\data.txt","r")
line = f.readlines() 
app = Flask(__name__)

'''
登录界面的路由设置，包括页面内的登录，注册，以及忘记密码的页面跳转
'''


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/static/login/<number>', methods=['POST'])
def login_post(number):
    if number == "1":
        username = request.form['username']
        password = request.form['password']

        for i in line:
            username0 = i.split(0)
            password0 = i.split(1)
            if username == username0 and password == password0:
                results = True
            else:
                results = False
        if results:
            print('登录成功')
            return render_template('index.html')
        else:
            return render_template('registration.html')
    if number == "2":
        return render_template('reset-password.html')
    elif number == "3":
        return render_template('registration.html')
    else:
        return render_template('error-500.html')

@app.route('/zhuce', methods=['Get'])
def zhuce1():
    return render_template('registration.html')

@app.route('/zhuce', methods=['POST'])
def zhuce():
    nickname = request.form['name1']
    password = request.form['password1']
    f.write('\n'+nickname+" "+password)
    return render_template('login.html')
f.close

if __name__ == '__main__':
    app.run(port=5000, debug=True)