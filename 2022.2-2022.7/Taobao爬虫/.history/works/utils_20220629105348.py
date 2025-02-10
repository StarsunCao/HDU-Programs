import time
import pymysql
import pandas as pd
import numpy as np

data1 = pd.read_csv("data.csv",sep=',',encoding='gbk')
data = data1.values.tolist()
title = ['商品名称','价格','地区','销量','评论数','商品链接','图片']
print(title)
def get_time():
    time_str = time.strftime("%Y{}%m{}%d %X")
    return time_str.format("年","月","日")
def get_map_data():

    return data1.地区.value_counts()
right1 = [data[1][1],data[2][1],data[3][1],data[4][1],data[5][1]]
right2 = [data[1][3],data[2][3],data[3][3],data[4][3],data[5][3]]
left = [data[1][4],data[2][4],data[3][4],data[4][4],data[5][4],data[6][4],data[7][4],data[8][4]]
print(data1.地区.value_counts())
data1 = ["1","Intel/至强E5-2680V2 2650v2 2690 2670 2660 2696v2处理器CPUX79","43","400","https://g-search2.alicdn.com/img/bao/uploaded/i4/i4/837413297/O1CN01GlpLy11aE4Q8SNGw6_!!837413297.jpg"]
if __name__ == "__main__":
    print(get_time())
print(data1)