from pxframe.pxutil import *


class LatestMsg(TestBase2):
    '''首页-滚动'''
    def test01(self):
        '''检查动态列表详情'''
        poco(text="首页").click()
        mlist=["产品动态", "客户动态", "预约消息"]
        try:
            poco("com.puxin.accountant:id/latest_msg").click()
        except:
            self.assertTrue(False,"网络连接有问题，或不存在动态信息")

        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title in mlist:
            print('滚动条跳转后显示{}'.format(title))
        else:
            back()
            self.assertTrue(False,'滚动条跳转后显示{}'.format(title))
        try:
            msg = poco("com.puxin.accountant:id/summary").get_text()
            time = poco("com.puxin.accountant:id/time")[0].get_text()
        except:
            back()
            self.assertTrue(False, '滚动条跳转后列表为空，或网络异常')
        back()
        print("{}加载的第一条动态是{}".format(time,msg))

    def test02(self):
        '''检查首页滚动公告'''
        poco(text="首页").click()
        try:
            poco("android.widget.ImageView").swipe([1, 0])
            poco("android.widget.ImageView").swipe([1, 0])
            poco("android.widget.ImageView").swipe([-1, 0])
            poco("android.widget.ImageView").swipe([-1, 0])
        except:
            self.assertTrue(False,"滚动公告滑动异常")
        try:
            poco("android.widget.ImageView").click()
            sleep(1)
            snapp('首页滚动公告')
            print('滚动公告跳转页面见截图')
        except:
            back()
            self.assertTrue(False, '滚动公告无法跳转')
        back()

