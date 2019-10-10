from pxframe.pxutil import *


class InsuranceProduct(TestBase2):
    '''产品-商业保理'''
    def test01(self):
        '''查看商业保理列表'''
        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_insurance").click()
        try:
            title = poco("com.puxin.accountant:id/toolbar_title").get_text()
            name = poco("com.puxin.accountant:id/fixed_name").get_text()
        except:
            back()
            self.assertTrue(False,'页面标题不存在，或保理列表为空')
        back()
        self.assertEqual(title,'商业保理','实际页面是{}'.format(title))
        print('{}页面的首个产品名称为{}'.format(title,name))


    def test02(self):
        '''验证商业保理产品详情'''
        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_insurance").click()
        try:
            title = poco("com.puxin.accountant:id/toolbar_title").get_text()
            name = poco("com.puxin.accountant:id/fixed_name").get_text()
        except:
            back()
            self.assertTrue(False, '页面标题不存在，或保理列表为空')
        try:
            poco("com.puxin.accountant:id/fixed_name").click()
            snapshot('./pxcapture/{}页{}详情.png'.format(title,name))
        except:
            back()
        title2 = poco("com.puxin.accountant:id/toolbar_title").get_text()
        back(2)
        self.assertEqual(title2, '产品详情', '实际页面是{}'.format(title2))
        print("商业保理，见截图")
