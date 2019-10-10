from pxframe.pxutil import *


class MarketActivity(TestBase2):
    '''首页-市场活动'''
    def test1(self):
        '''活动管理列表'''
        poco(text="首页").click()
        poco("com.puxin.accountant:id/rl_activity").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        try:
            intro = poco("com.puxin.accountant:id/tv_introduce").get_text()
        except:
            back()
            self.assertTrue(False,'活动管理列表为空，或网络异常')
        back()
        self.assertEqual(title, '活动管理', '活动管理跳转后页面是{}'.format(title))
        print('活动管理第一个活动概要是{}'.format(intro))

    def test2(self):
        '''活动管理-活动详情'''
        poco(text="首页").click()
        poco("com.puxin.accountant:id/rl_activity").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        try:
            intro = poco("com.puxin.accountant:id/tv_introduce").get_text()
            poco("com.puxin.accountant:id/tv_introduce").click()
        except:
            back()
            self.assertTrue(False,'活动管理列表为空，或网络异常')
        poco("com.puxin.accountant:id/iv_share").click()
        snapp('活动管理-活动详情')
        try:
            poco(text="取消分享").click()
        except:
            keyevent("BACK")
            back(3)
            self.assertTrue(False,'活动详情，取消分享功能异常')
        back(2)
        print("活动管理-活动详情见截图")

    def test3(self):
        '''活动管理-报名签到表'''
        poco(text="首页").click()
        poco("com.puxin.accountant:id/rl_activity").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        try:
            intro = poco("com.puxin.accountant:id/tv_introduce").get_text()
            poco("com.puxin.accountant:id/tv_introduce").click()
        except:
            back()
            self.assertTrue(False, '活动管理列表为空，或网络异常')
        poco("com.puxin.accountant:id/bt_enlist").click()
        title2 = poco("com.puxin.accountant:id/toolbar_title").get_text()
        sleep(1)
        back(3)
        self.assertEqual(title2,'报名签到表','报名签到表跳转后页面是{}'.format(title2))
        print("活动管理，报名签到表正常")

    def test4(self):
        '''活动管理-协助客户报名'''
        poco(text="首页").click()
        poco("com.puxin.accountant:id/rl_activity").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        try:
            intro = poco("com.puxin.accountant:id/tv_introduce").get_text()
            poco("com.puxin.accountant:id/tv_introduce").click()
        except:
            back()
            self.assertTrue(False, '活动管理列表为空，或网络异常')
        poco("com.puxin.accountant:id/bt_help_enlist").click()
        title2 = poco("com.puxin.accountant:id/toolbar_title").get_text()
        back(2)
        self.assertEqual(title2, '协助报名', '协助报名跳转后页面是{}'.format(title))
        back()
        print("需link支持，否则验证报名流程很被动")
