from flask import Flask, request, render_template,jsonify
import utils

app = Flask(__name__)

@app.route('/time')
def get_time():  # put application's code here
    return utils.get_time()
@app.route('/data')
def get_data():  # put application's code here
    data = utils.data1
    return jsonify({"num": data[0], "name": data[1], "volume": data[2], "prise": data[3], "picture": data[4]})
@app.route('/c2')
def get_right_data():  # put application's code here
    right = utils.right1
    return jsonify({"y1":right[0],"y2":right[1],"y3":right[2],"y4":right[3],"y5":right[4]})
@app.route('/')
def hello_world():  # put application's code here
    return render_template("淘宝商品分析.html")

if __name__ == '__main__':
    app.run()
