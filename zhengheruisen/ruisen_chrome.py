from selenium import webdriver
from time import sleep
from pxframe.pxos_handle import *


driver = webdriver.Chrome()
# driver2 = webdriver.Chrome()
driver.get('http://fin.puxinasset.com')
driver.implicitly_wait(10)
# driver2.get('http://fin.puxinasset.com')
# driver2.implicitly_wait(10)
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
    flag +=1
# while True:
#     for m in c:
#         driver.implicitly_wait(5)
#         driver.find_element_by_link_text(m).click()
#         print(driver.title)
#         sleep(1)
#         # print(driver.title)
#         # driver.get('http://www.puxinasset.com')
#         print(flag)

# flag=0
# for i in range(1000):
#     # sleep(3)
#     try:
#         driver.find_element_by_link_text('关于我们').click()
#         print(flag, driver.title, nowtime(2))
#     except:
#         print(flag,driver.title,nowtime(2))
#         driver.get('http://www.zhrscapital.com/webcms/index!index.action')
#     # sleep(3)
#
#     try:
#         driver.find_element_by_link_text('投资策略').click()
#         print(flag, driver.title, nowtime(2))
#     except:
#         print(flag, driver.title, nowtime(2))
#         driver.get('http://www.zhrscapital.com/webcms/index!index.action')
#     # sleep(3)
#
#     try:
#         driver.find_element_by_link_text('新闻公告').click()
#         print(flag, driver.title, nowtime(2))
#     except:
#         print(flag, driver.title, nowtime(2))
#         driver.get('http://www.zhrscapital.com/webcms/index!index.action')
#     # sleep(3)
#
#     try:
#         driver.find_element_by_link_text('联系我们').click()
#         print(flag, driver.title, nowtime(2))
#     except:
#         print(flag, driver.title, nowtime(2))
#         driver.get('http://www.zhrscapital.com/webcms/index!index.action')
#     flag+=1
#     print(flag)
#
# driver.quit()
# driver.service.stop()