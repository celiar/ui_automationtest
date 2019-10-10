from pxframe.pxutil import *


class Publicfund(TestBase2):
    '''产品-公募基金'''
    def test01(self):
        '''验证公募基金页面'''
        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_public").click()
        try:
            tag = poco("com.puxin.accountant:id/toolbar_title").get_text()
            snapshot("./pxcapture/公募基金{}.png".format(nowtime()))
            back()
            self.assertEqual("公募基金",tag,"公募基金页面有误")
            print("公募基金页面正常")
        except:
            snapshot("./pxcapture/公募基金异常{}.png".format(nowtime()))
            back()
