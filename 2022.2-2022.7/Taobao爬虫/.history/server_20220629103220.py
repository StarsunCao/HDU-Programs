import os
from flask import Flask, redirect, render_template, request
import App
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = []
    if request.method == 'POST':
        input = request.form.get("input")
        App.run(input)
        
       ''' if request.files:
            uploaded_file = request.files['filename'] # This line uses the same variable and worked fine
            filepath = os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename)
            uploaded_file.save(filepath)
            with open(filepath) as file:
                csv_file = csv.reader(file)
                for row in csv_file:
                    data.append(row)
            return redirect(request.url)
    return render_template('index.html', data=data)'''

if __name__ == '__main__':
    app.run(port=5000, debug=True)