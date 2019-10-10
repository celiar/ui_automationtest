from pxframe.pxutil import *


class ProductManagement(TestBase2):
    '''首页-产品管理'''
    def test1(self):
        '''产品中心跳转'''
        poco(text="首页").click()
        poco("com.puxin.accountant:id/rl_product").click()
        title = poco("android.widget.TextView").get_text()
        if title == "全球资产配置服务":
            snapp('首页--产品中心跳转')
            print("主页--产品中心跳转正常")
        else:
            poco("com.puxin.accountant:id/iv_back").click()
            self.assertTrue(False,"主页--产品中心跳转功能异常")
        poco("com.puxin.accountant:id/iv_back").click()

    def test2(self):
        '''信息披露列表'''
        poco(text="首页").click()
        poco("com.puxin.accountant:id/rl_inforeport").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title=='信息披露':
            try:
                product_name = poco("com.puxin.accountant:id/product_name").get_text()
            except:
                back()
                self.assertTrue(False,'信息披露列表为空，或网络异常')
            back()
            print('信息披露跳转正常，第一条标题是{}'.format(product_name))
        else:
            back()
            self.assertTrue(False,'信息披露跳转后页面是{}'.format(title))

    def test3(self):
        '''信息披露--查看投资客户'''
        poco(text="首页").click()
        poco("com.puxin.accountant:id/rl_inforeport").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '信息披露':
            try:
                product_name = poco("com.puxin.accountant:id/product_name").get_text()
            except:
                back()
                self.assertTrue(False, '信息披露列表为空，或网络异常')
            try:
                poco("com.puxin.accountant:id/pdf_list").click()
            except:
                back()
                self.assertTrue(False, '信息披露，查看投资客户异常')
            title2 = poco("com.puxin.accountant:id/toolbar_title").get_text()
            back(2)
            self.assertEqual(product_name,title2,'{}跳转后页面是{}'.format(product_name,title2))
            print('信息披露,查看投资客户功能正常')
        else:
            back(2)
            self.assertTrue(False, '信息披露跳转后页面是{}'.format(title))

    def test4(self):
        '''信息披露pdf'''
        poco(text="首页").click()
        poco("com.puxin.accountant:id/rl_inforeport").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '信息披露':
            try:
                product_name = poco("com.puxin.accountant:id/product_name").get_text()
            except:
                back()
                self.assertTrue(False, '信息披露列表为空，或网络异常')
            try:
                pdf_name = poco("com.puxin.accountant:id/pdf_name").get_text()
                poco("com.puxin.accountant:id/pdf_name").click()
                sleep(3)
                snapp('信息披露-{}pdf'.format(pdf_name))
            except:
                back()
                self.assertTrue(False, '信息披露，查看pdf异常')
            back(2)
            print('信息披露,pdf见截图')
        else:
            back(2)
            self.assertTrue(False, '信息披露跳转后页面是{}'.format(title))

