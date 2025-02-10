from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    os.system(r'C:\Users\a\OneDrive\Learning Materials\2022.2-2022.7\短学期\淘宝爬虫\App.py')
    return 'hello_world'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form.get('username'))
        print(request.form.get('password'))
        print(request.form.get('repassword'))
 
        return '注册成功'
 
    return render_template('register.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)