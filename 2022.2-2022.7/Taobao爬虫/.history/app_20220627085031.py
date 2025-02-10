import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

input = '显卡'

chrome_options = Options()
chrome_options.debugger_address="127.0.0.1:9222"
chrome_driver = r"C:\Users\a\AppData\Local\Programs\Python\Python310\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver,chrome_options=chrome_options)

# 查找搜索框
send = driver.find_element(By.XPATH, r'//*[@id="q"]')
send.click()
time.sleep(1)
send.send_keys(input)
# 点击搜索按钮进行搜索
search = driver.find_element(By.XPATH, r'//*[@id="J_TSearchForm"]/div[1]/button')
time.sleep(1)
search.click()
time.sleep(1)
# 转到新窗口
windows = driver.window_handles
driver.switch_to.window(windows[-1])
time.sleep(1)

# 切换销量排序
send = driver.find_element(By.XPATH, r'//*[@id="J_relative"]/div[1]/div/ul/li[2]/a')
send.click()
time.sleep(2)
# 切换列表模式
send = driver.find_element(By.XPATH, r'//*[@id="J_relative"]/div[1]/div/div[3]/ul/li[2]/a')
send.click()
time.sleep(2)

# 查询商品链接
links = []
names = []
prices = []
locations = []
comments = []
sales = []
for i in range(0, 2):
    name = driver.find_elements(By.XPATH, r'//div[@class="col col-2"]/p/a')
    # name = driver.find_elements(By.XPATH, r'//*[@id="mainsrp-itemlist"]/div/div/div/div/div[2]/div[2]/p/a/text()')
    price = driver.find_elements(By.XPATH, r'//span[@class="price g_price g_price-highlight"]/strong')
    location = driver.find_elements(By.XPATH, r'//div[@class="location"]')
    comment = driver.find_elements(By.XPATH, r'//div[@class="col col-4"]/p/a')
    sale = driver.find_elements(By.XPATH, r'//p[@class="deal-cnt"]')

    # links.extend(link)
    for j in range(0,44):
        names.append(name[j].text)
        prices.append(price[j].text)
        locations.append(location[j].text)
        comments.append(comment[j].text)
        sales.append(sale[j].text)

    time.sleep(1)
    send = driver.find_element(By.XPATH, r'//*[@id="J_relative"]/div[1]/div/div[2]/ul/li[3]/a')
    send.click()
    time.sleep(1)

print(names)
print(len(names))
send = driver.find_element(By.XPATH, r'//*[@id="mainsrp-header"]/div/div/div/div[1]/a')
send.click()

"""
time.sleep(5)
login_out = driver.find_element_by_id("J_Logout")
login_out.click()
driver.back()
time.sleep(2)
details = driver.find_element_by_class_name("product-iWrap")
details.click()
time.sleep(3)
# 转到新窗口
windows = driver.window_handles
driver.switch_to.window(windows[-1])
time.sleep(3)
content = driver.page_source
 
with open("./产品详细.html", "w", encoding="utf-8") as file:
    file.write(content)
time.sleep(12)
print("产品详细页已经保存完毕!!!!")
driver.quit()
"""