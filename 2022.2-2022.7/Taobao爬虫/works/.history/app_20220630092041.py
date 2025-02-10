from flask import Flask, request, render_template,jsonify

import creeper
import utils

app = Flask(__name__)

@app.route('/time')
def get_time():  # put application's code here
    return utils.get_time()
@app.route('/data')
def get_data():  # put application's code here
    i = request.values['text']
    data = utils.data(int(i))
    return jsonify({"num": int(i)+1,"name": data[0], "volume": data[3], "prise": data[1], "html":data[5],"picture": data[6]})
@app.route('/r1')
def get_right1_data():  # put application's code here
    right1 = utils.right1()
    return jsonify({"y1":int(right1[0]),"y2":int(right1[1]),"y3":int(right1[2]),"y4":int(right1[3]),"y5":int(right1[4])})
@app.route('/r2')
def get_right2_data():  # put application's code here
    right2 = utils.right2()
    return jsonify({"y1":int(right2[0]),"y2":int(right2[1]),"y3":int(right2[2]),"y4":int(right2[3]),"y5":int(right2[4])})
@app.route('/l')
def get_left_data():  # put application's code here
    left = utils.left()
    return jsonify({"y1":int(left[0]),"y2":int(left[1]),"y3":int(left[2]),"y4":int(left[3]),"y5":int(left[4]),"y6":int(left[5]),"y7":int(left[6]),"y8":int(left[7])})

@app.route('/map')
def get_map_data():  # put application's code here
    map = utils.map()
    return jsonify({"上海":int(map[0]),'北京':int(map[1]),'吉林':int(map[2]),'黑龙江':int(map[3]),'四川':int(map[4]),'安徽':int(map[5]),
                    '山东':int(map[6]),'广东':int(map[7]),'江苏':int(map[8]),'河南':int(map[9]),'浙江':int(map[10]),'湖北':int(map[11]),
                    '湖南':int(map[12]),'重庆':int(map[13]),'福建':int(map[14]),'陕西':int(map[15]),'山西':int(map[16]),'内蒙古':int(map[17]),'新疆':int(map[18]),
                    '贵州':int(map[19]),'台湾':int(map[20]),'海南':int(map[21]),'天津':int(map[22]),'青海':int(map[23]),'甘肃':int(map[24]),'辽宁':int(map[25]),
                    '河北':int(map[26]),'香港':int(map[27]),'澳门':int(map[28]),'广西':int(map[29]),'宁夏':int(map[30]),'云南':int(map[31]),'江西':int(map[32]),'西藏':int(map[33])})

@app.route('/')
def hello_world():  # put application's code here
    return render_template("淘宝商品分析.html")
@app.route('/js_get', methods=['GET'])
def js_get():
    staff = request.values['text']
    creeper.run(staff)
    return "完成"
if __name__ == '__main__':
    app.run()
