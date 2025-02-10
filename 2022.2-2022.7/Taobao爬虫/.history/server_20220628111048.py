from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    os.system(r'C:\Users\a\OneDrive\Learning Materials\2022.2-2022.7\短学期\淘宝爬虫\App.py')
    return 'hello_world'
  
@app.route('/register', methods=['POST'])
def register():
    print(request.headers)
    #print(request.stream.read())
    return 'welcome'

if __name__ == '__main__':
    app.run(port=5000, debug=True)