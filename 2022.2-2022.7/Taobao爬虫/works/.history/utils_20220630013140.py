import time
import pymysql
import pandas as pd
import numpy as np

import app


data1 = pd.read_csv("data.csv",sep=',',encoding='gbk')
data = data1.values.tolist()
def get_time():
    time_str = time.strftime("%Y{}%m{}%d %X")
    return time_str.format("年","月","日")
def right1():
    data1 = pd.read_csv("data.csv", sep=',', encoding='gbk')
    data = data1.values.tolist()
    right1 = [data[1][1] + 1000, data[2][1], data[3][1], data[4][1], data[5][1]]
    return right1
def right2():
    data1 = pd.read_csv("data.csv", sep=',', encoding='gbk')
    data = data1.values.tolist()
    right2 = [data[1][3],data[2][3],data[3][3],data[4][3],data[5][3]]
    return right2
def left():
    data1 = pd.read_csv("data.csv", sep=',', encoding='gbk')
    data = data1.values.tolist()
    left = [data[1][4], data[2][4], data[3][4], data[4][4], data[5][4], data[6][4], data[7][4], data[8][4]]
    return left
def left():
    data1 = pd.read_csv("data.csv", sep=',', encoding='gbk')
    data = data1.values.tolist()
    left = [data[1][4], data[2][4], data[3][4], data[4][4], data[5][4], data[6][4], data[7][4], data[8][4]]
    return left
def map():
    data1 = pd.read_csv("data.csv", sep=',', encoding='gbk')
    data = data1.values.tolist()
    location = data1.地区.value_counts(ascending=True).sort_index(ascending=True)
    map = [None] * 34
    place = ['上海', '北京', '吉林', '黑龙江', '四川', '安徽', '山东', '广东', '江苏', '河南', '浙江', '湖北', '湖南', '重庆', '福建', '陕西',
             '山西', '内蒙古', '新疆', '贵州', '台湾', '海南', '天津', '青海', '甘肃', '辽宁', '河北', '香港', '澳门', '广西', '宁夏', '云南', '江西',
             '西藏']
    for i in range(34):
        if place[i] in location:
            map[i] = location[place[i]]
        else:
            map[i] = 0
    return map


if __name__ == "__main__":
    print(get_time())
