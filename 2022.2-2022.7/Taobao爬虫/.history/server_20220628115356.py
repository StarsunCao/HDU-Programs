from flask import Flask, render_template, request
import App

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello_world'

@app.route('/search', methods=['GET', 'POST'])
    if request.method == "POST":
        input = request.form.get("input")
        App.run(input)
        return 

if __name__ == '__main__':
    app.run(port=5000, debug=True)