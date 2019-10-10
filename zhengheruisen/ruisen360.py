from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import time,logging
from pxframe.pxos_handle import *
now = time.strftime('%Y_%m_%d_%H.%M.%S', time.localtime(time.time()))
__browser_url = r"C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe"
chrome_options = Options()
chrome_options.binary_location = __browser_url
driver=webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)
# driver2=webdriver.Chrome(chrome_options=chrome_options)
# driver2.implicitly_wait(10)
driver.get('http://www.puxinasset.com')
# driver2.get('http://fin.puxinasset.com')
c = ['首页','咨询服务','家族财富服务','普信研究','普信动态','关于普信']
# a = driver.find_elements_by_xpath('//ul[@class="headul clearfix"]/li/a')
# b = driver2.find_elements_by_xpath('//ul[@class="headul clearfix"]/li/a')
flag = 0
while True:
    for m in c:
        driver.implicitly_wait(5)
        driver.find_element_by_link_text(m).click()
        print(driver.title)
        sleep(1)
        # print(driver.title)
        # driver.get('http://www.puxinasset.com')
    print(flag)
    flag+=1



# flag=0
# for i in range(1000):
#
#     sleep(1)
#     try:
#         driver.find_element_by_link_text('关于我们').click()
#         print(flag, driver.title, nowtime(2))
#     except:
#         print(flag, driver.title, nowtime(2))
#         # print(flag)
#         driver.get('http://www.zhrscapital.com/webcms/index!index.action')
#
#     # sleep(1)
#     try:
#         driver.find_element_by_link_text('投资策略').click()
#         print(flag, driver.title, nowtime(2))
#     except:
#         print(flag, driver.title, nowtime(2))
#         driver.get('http://www.zhrscapital.com/webcms/index!index.action')
#
#     # sleep(1)
#     try:
#         driver.find_element_by_link_text('联系我们').click()
#         print(flag, driver.title, nowtime(2))
#     except:
#         print(flag, driver.title, nowtime(2))
#         driver.get('http://www.zhrscapital.com/webcms/index!index.action')
#
#     # sleep(1)
#     try:
#         driver.find_element_by_link_text('新闻公告').click()
#         print(flag, driver.title, nowtime(2))
#     except:
#         print(flag, driver.title, nowtime(2))
#         driver.get('http://www.zhrscapital.com/webcms/index!index.action')
#
#     flag+=1
#     print(flag)
#
# driver.quit()
# driver.service.stop()