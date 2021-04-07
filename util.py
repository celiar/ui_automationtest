import requests
from lxml import etree
import time
from base64 import b64encode

class util:
    # 获取属性值
    @classmethod
    def get_element(cls,text,xpath):
        html = etree.HTML(str(text))
        # html = etree.parse("./bd.html")
        # html = etree.tostring(html,encoding="utf-8").decode("utf-8")
        # for hit in html.xpath('//span[@class="hitClass"]'):
        #     return hit.text
        # x1 = '//span[@class="hitClass"]'
        # 返回LIST第一项，或其他自定义定位方法
        return html.xpath(xpath)[0].text

    @classmethod
    def the_time(self):
        return time.strftime("%H:%M:%S", time.localtime())

    @classmethod
    def the_date(self):
        return time.strftime("%Y%m%d", time.localtime())

    def login(self,url,name,pwd):
        # 需从开发获取加密算法，比如是bs64加密
        pwd = b64encode(pwd)
        data = {
            "LoginName":name,
            "LoginPwd":pwd
        }

        with requests.post(url=url,data=data,headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}) as res:
            return res.json()
