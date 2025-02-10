import time
 
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
 
option = ChromeOptions()
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("--disable-blink-features")
option.add_argument("--disable-blink-features=AutomationControlled")
driver = Chrome(options=option)
url = "https://www.taobao.com/"
 
driver.get(url)
# 查找搜索框，天猫会不定期更改元素，注意自行更改
send = driver.find_element(By.XPATH, r'//*[@id="q"]')
send.click()
time.sleep(2)
send.send_keys("良品铺子")
# 点击搜索按钮进行搜索
search = driver.find_element_by_xpath("//div[@class='rax-view-v2 SearchInput--searchButton--1Sz2UIn']")
time.sleep(1)
search.click()
time.sleep(3)
# 转到新窗口
windows = driver.window_handles
driver.switch_to.window(windows[-1])
# 查询用户登录名输入框
login_name = driver.find_element_by_id("fm-login-id")
# 手机号或用户名
number = "1********1"
# 一个一个输入增加模仿用户登录
for num in number:
    login_name.send_keys(num)
    time.sleep(0.3)
# 查询密码元素
login_pwd = driver.find_element_by_id("fm-login-password")
# 输入密码
pwd = "********"
for p_num in pwd:
    login_pwd.send_keys(p_num)
    time.sleep(0.3)
 
# 查询登录按钮
login = driver.find_element_by_xpath("//button[@type='submit']")
login.click()
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