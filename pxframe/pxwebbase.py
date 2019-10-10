# 实现添加cookie绕过登录验证码，与testbase的driver非同一实例，请知悉
from selenium import webdriver
from selenium.webdriver.common.by import By
from pxconfig import *
from time import sleep
import json

def get_cbslogin_cookies():
    driver = webdriver.Chrome()
    driver.get(cbsurl)
    driver.find_element_by_id('mobile').send_keys(cbsphone)
    driver.find_element_by_id('password').send_keys(cbspwd)
    if pmode == 'sc':
        vcode = inputcode('请输入cbs系统登录验证码，并按回车键')
    else:
        vcode = inputcode('请输入cbs系统登录验证码，并按回车键')
        # vcode = '0000'

    driver.find_element_by_id('validateCode').send_keys(vcode)
    driver.find_element_by_css_selector('[type="submit"]').click()
    sleep(2)
    cookies = driver.get_cookies()
    print(cookies)
    with open('./cbscookie.json','w') as wf:
            wf.write(json.dumps(cookies))
    driver.quit()
    driver.service.stop()

def get_cmslogin_cookies():
    driver = webdriver.Chrome()
    driver.get(cmsurl)
    driver.find_element_by_name('account').send_keys(cmsphone)
    driver.find_element_by_name('password').send_keys(cmspwd)
    if pmode == 'zsc':
        vcode = inputcode('请输入cms系统登录验证码，并按回车键')
    else:
        vcode = inputcode('请输入cms系统登录验证码，并按回车键')
        # vcode = '0000'

    driver.find_element_by_name('randCode').send_keys(vcode)
    driver.find_element_by_id('ext-gen30').click()
    cookies = driver.get_cookies()
    print(cookies)
    with open('./cmscookie.json','w') as wf:
            wf.write(json.dumps(cookies))
    driver.quit()
    driver.service.stop()

# # get_cmslogin_cookies()
# driver = webdriver.Chrome()
# driver.get(cmsurl)
# with open('./cmscookie.json', 'r') as rf:
#     cookies = json.loads(rf.read())
# for cookie in cookies:
#     driver.add_cookie({
#         'name': cookie['name'],
#         'value': cookie['value']
#
#     })
#     print(driver.get_cookies())
# driver.get(cmshomeurl)
# # driver.refresh()

