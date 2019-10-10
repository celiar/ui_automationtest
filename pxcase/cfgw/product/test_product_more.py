from pxframe.pxutil import *


class MoreProduct(TestBase2):
    '''产品-更多'''

    def test01(self):
        '''私募基金-更多'''
        data=["私募基金","类固收类","股权投资","私募证券","不良资产"]
        data2=[]
        poco(text="产品").click()
        poco("com.puxin.accountant:id/group_more").click()
        # poco("com.puxin.accountant:id/refreshlayout").swipe([0, -1])
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if data[0]==title:
            name = poco("com.puxin.accountant:id/tv_type_name")
            for i in range(len(name)):
                data2.append(name[i].get_text())
            back()
            print("私募基金显示子产品名称为{}".format(data2))
        else:
            back()
            self.assertTrue(False, "私募基金跳转后的页面名称为{}".format(title))

    def test02(self):
        '''稳金宝-更多'''
        data = ["稳金宝", "智信", "惠盈", "华裕"]
        data2 = []
        poco(text="产品").click()
        poco("com.puxin.accountant:id/group_more")[1].click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if data[0] == title:
            name = poco("com.puxin.accountant:id/tv_type_name")
            for i in range(len(name)):
                data2.append(name[i].get_text())
            back()
            print("稳金宝显示子产品名称为{}".format(data2))
        else:
            back()
            self.assertTrue(False, "稳金宝跳转后的页面名称为{}".format(title))

    def test03(self):
        '''商业保理-更多'''
        title1 = "商业保理"
        poco(text="产品").click()
        poco("com.puxin.accountant:id/refreshlayout").swipe([0, -1])
        poco("com.puxin.accountant:id/group_more").click()
        title2 = poco("com.puxin.accountant:id/toolbar_title").get_text()
        back()
        poco("com.puxin.accountant:id/refreshlayout").swipe([0, 1])
        self.assertEqual(title1,title2, "商业保理跳转后的页面名称为{}".format(title2))
        print("商业保理跳转正常")
    # def test04(self):
    #     '''第四项-更多'''
    #     poco(text="产品").click()
    #     poco("com.puxin.accountant:id/group_more").click()
