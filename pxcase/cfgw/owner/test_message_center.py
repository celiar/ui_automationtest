from pxframe.pxutil import *


class MessageCenter(TestBase2):
    '''我的-消息中心'''
    def test_product_dynamic(self):
        '''检查产品动态'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/iv_message").wait_for_appearance()
        poco("com.puxin.accountant:id/iv_message").click()
        titles = poco("com.puxin.accountant:id/msg_title")
        titles[0].click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        back(2)
        self.assertEqual(title,'产品动态','产品动态调转后是{}'.format(title))
        print('产品动态跳转成功')

    def test_customer_dynamic(self):
        '''检查客户动态'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/iv_message").wait_for_appearance()
        poco("com.puxin.accountant:id/iv_message").click()
        titles = poco("com.puxin.accountant:id/msg_title")
        titles[1].click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        back(2)
        self.assertEqual(title, '客户动态', '客户动态调转后是{}'.format(title))
        print('客户动态跳转成功')

    def test_reservation(self):
        '''检查预约服务'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/iv_message").wait_for_appearance()
        poco("com.puxin.accountant:id/iv_message").click()
        titles = poco("com.puxin.accountant:id/msg_title")
        titles[2].click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        back(2)
        self.assertEqual(title, '预约服务', '预约服务调转后是{}'.format(title))
        print('预约服务跳转成功')

    def test_notice(self):
        '''检查通知公告'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/iv_message").wait_for_appearance()
        poco("com.puxin.accountant:id/iv_message").click()
        titles = poco("com.puxin.accountant:id/msg_title")
        titles[3].click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        back(2)
        self.assertEqual(title, '通知公告', '通知公告调转后是{}'.format(title))
        print('通知公告跳转成功')
