from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello_world'

@app.route('/search', methods=['GET', 'POST'])
    if request.method == "POST":
        os.system(r'C:\Users\a\OneDrive\Learning Materials\2022.2-2022.7\短学期\淘宝爬虫\App.py')

if __name__ == '__main__':
    app.run(port=5000, debug=True)