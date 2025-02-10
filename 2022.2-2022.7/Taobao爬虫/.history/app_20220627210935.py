import time
import pandas as pd
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

input = "机箱"

chrome_options = Options()
chrome_options.debugger_address="127.0.0.1:9222"
chrome_driver = r"C:\Users\a\AppData\Local\Programs\Python\Python310\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver,chrome_options=chrome_options)

# 查找搜索框
send = driver.find_element(By.XPATH, r'//*[@id="q"]')
send.click()
time.sleep(0.5)
send.clear()
time.sleep(0.5)
send.send_keys(input)
# 点击搜索按钮进行搜索

try:
    search = driver.find_element(By.XPATH, r'//*[@id="J_TSearchForm"]/div[1]/button')
    time.sleep(0.5)
    search.click()
    time.sleep(0.5)
except:
    search = driver.find_element(By.XPATH, r'//*[@id="J_SearchForm"]/button')
    time.sleep(0.5)
    search.click()
    time.sleep(0.5)

'''# 转到新窗口
windows = driver.window_handles
driver.switch_to.window(windows[-1])
time.sleep(0.5)'''

# 切换销量排序
send = driver.find_element(By.XPATH, r'//*[@id="J_relative"]/div[1]/div/ul/li[2]/a')
send.click()
time.sleep(1)
# 切换列表模式
send = driver.find_element(By.XPATH, r'//*[@id="J_relative"]/div[1]/div/div[3]/ul/li[2]/a')
send.click()
time.sleep(1)

# 查询商品链接
links = []
names = []
prices = []
locations = []
comments = []
sales = []
links = []
pictures= []

# 读取第一页
name = driver.find_elements(By.XPATH, r'//div[@class="col col-2"]/p/a')
price = driver.find_elements(By.XPATH, r'//span[@class="price g_price g_price-highlight"]/strong')
location = driver.find_elements(By.XPATH, r'//div[@class="location"]')
comment = driver.find_elements(By.XPATH, r'//div[@class="col col-4"]/p/a')
sale = driver.find_elements(By.XPATH, r'//p[@class="deal-cnt"]')
picture = driver.find_elements(By.XPATH, r'//div[@class="pic J_MouseEneterLeave J_ThumbPopup"]')

for j in range(0,len(name)):
    names.append(name[j].text)
    prices.append(price[j].text)
    locations.append(location[j].text)
    comments.extend(re.findall(r"\d+", comment[j].text))
    sales.extend(re.findall(r"\d+",sale[j].text))
    links.append(name[j].get_attribute("href"))
    pictures.append("https:"+picture[j].get_attribute("data-pic"))

# 翻页并读取
for i in range(0, 10):
    send = driver.find_element(By.XPATH, r'//*[@id="J_relative"]/div[1]/div/div[2]/ul/li[3]/a')
    send.click()
    time.sleep(0.8)

    name = driver.find_elements(By.XPATH, r'//div[@class="col col-2"]/p/a')
    price = driver.find_elements(By.XPATH, r'//span[@class="price g_price g_price-highlight"]/strong')
    location = driver.find_elements(By.XPATH, r'//div[@class="location"]')
    comment = driver.find_elements(By.XPATH, r'//div[@class="col col-4"]/p/a')
    sale = driver.find_elements(By.XPATH, r'//p[@class="deal-cnt"]')
    picture = driver.find_elements(By.XPATH, r'//div[@class="pic J_MouseEneterLeave J_ThumbPopup"]')

    for j in range(0,len(name)):
        names.append(name[j].text)
        prices.append(price[j].text)
        locations.append(location[j].text)
        comments.extend(re.findall(r"\d+", comment[j].text))
        sales.extend(re.findall(r"\d+",sale[j].text))
        links.append(name[j].get_attribute("href"))
        pictures.append("https:"+picture[j].get_attribute("data-pic"))

# 创建csv文件
frame = pd.DataFrame({'商品名称':names, '价格':prices, '地区':locations, '销量':sales, '评论数':comments, '商品链接':links, '图片':pictures})
frame.to_csv("data.csv", index=False, sep=',', encoding="gbk")
print("产品详细页已经保存完毕!")

# 返回主页
send = driver.find_element(By.XPATH, r'//*[@id="mainsrp-header"]/div/div/div/div[1]/a')
send.click()