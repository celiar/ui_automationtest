from pxframe.pxutil import *


class IC(TestBase2):
    '''首页-投资咨询（IC）'''
    def test1(self):
        '''投顾观点列表'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_ask_view").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '投顾观点':
            print('投顾观点跳转正常')
            try:
                title2 = poco("com.puxin.accountant:id/tv_title").get_text()
                date = poco("com.puxin.accountant:id/tv_date").get_text()
                content = poco("com.puxin.accountant:id/tv_content").get_text()
                print(date,title2,content)
            except:
                back()
                swipe_up("com.puxin.accountant:id/fl_tab_container")
                self.assertTrue(False, '投顾观点列表为空，或网络异常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False, '投顾观点跳转页面是{}'.format(title))
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")

    def test2(self):
        '''投顾观点详情'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_ask_view").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '投顾观点':
            try:
                title2 = poco("com.puxin.accountant:id/tv_title").get_text()
                poco("com.puxin.accountant:id/tv_title").click()
                sleep(2)
                snapp('投顾观点{}'.format(title2))
            except:
                back()
                swipe_up("com.puxin.accountant:id/fl_tab_container")
                self.assertTrue(False, '投顾观点列表为空，或网络异常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False, '投顾观点跳转页面是{}'.format(title))
        back(2)
        swipe_up("com.puxin.accountant:id/fl_tab_container")
        print("投顾观点详情见截图")

    def test3(self):
        '''实战演练列表'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_ask_fact").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '实战演练':
            print('实战演练跳转正常')
            try:
                title2 = poco("com.puxin.accountant:id/tv_title").get_text()
                date = poco("com.puxin.accountant:id/tv_date").get_text()
                content = poco("com.puxin.accountant:id/tv_content").get_text()
                print(date, title2, content)
            except:
                back()
                swipe_up("com.puxin.accountant:id/fl_tab_container")
                self.assertTrue(False, '实战演练列表为空，或网络异常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False, '实战演练跳转页面是{}'.format(title))
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")

    def test4(self):
        '''实战演练详情'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_ask_fact").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '实战演练':
            try:
                title2 = poco("com.puxin.accountant:id/tv_title").get_text()
                poco("com.puxin.accountant:id/tv_title").click()
                sleep(2)
                snapp('实战演练{}'.format(title2))
            except:
                back()
                swipe_up("com.puxin.accountant:id/fl_tab_container")
                self.assertTrue(False, '实战演练列表为空，或网络异常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False, '实战演练跳转页面是{}'.format(title))
        keyevent("BACK")
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")
        print("实战演练详情见截图")

    def test5(self):
        '''竞品分析列表'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_ask_competetion").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '竞品分析':
            print('竞品分析跳转正常')
            try:
                title2 = poco("com.puxin.accountant:id/tv_title").get_text()
                date = poco("com.puxin.accountant:id/tv_date").get_text()
                content = poco("com.puxin.accountant:id/tv_content").get_text()
                print(date, title2, content)
            except:
                back()
                swipe_up("com.puxin.accountant:id/fl_tab_container")
                self.assertTrue(False, '竞品分析列表为空，或网络异常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False, '竞品分析跳转页面是{}'.format(title))
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")

    def test6(self):
        '''竞品分析详情'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_ask_competetion").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '竞品分析':
            try:
                title2 = poco("com.puxin.accountant:id/tv_title").get_text()
                poco("com.puxin.accountant:id/tv_title").click()
                sleep(2)
                snapp('竞品分析{}'.format(title2))
            except:
                back()
                swipe_up("com.puxin.accountant:id/fl_tab_container")
                self.assertTrue(False, '竞品分析列表为空，或网络异常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False, '竞品分析跳转页面是{}'.format(title))
        back(2)
        swipe_up("com.puxin.accountant:id/fl_tab_container")
        print("竞品分析详情见截图")

    def test7(self):
        '''产品Q&A列表'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_ask_qa").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '产品Q&A':
            print('产品Q&A跳转正常')
            try:
                title2 = poco("com.puxin.accountant:id/tv_title").get_text()
                date = poco("com.puxin.accountant:id/tv_date").get_text()
                content = poco("com.puxin.accountant:id/tv_content").get_text()
                print(date, title2, content)
            except:
                back()
                swipe_up("com.puxin.accountant:id/fl_tab_container")
                self.assertTrue(False, '产品Q&A列表为空，或网络异常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False, '产品Q&A跳转页面是{}'.format(title))
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")

    def test8(self):
        '''产品Q&A详情'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_ask_qa").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '产品Q&A':
            try:
                title2 = poco("com.puxin.accountant:id/tv_title").get_text()
                poco("com.puxin.accountant:id/tv_title").click()
                sleep(2)
                snapp('产品Q&A{}'.format(title2))
            except:
                back()
                swipe_up("com.puxin.accountant:id/fl_tab_container")
                self.assertTrue(False, '产品Q&A列表为空，或网络异常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False, '产品Q&A跳转页面是{}'.format(title))
        back(2)
        swipe_up("com.puxin.accountant:id/fl_tab_container")
        print("产品Q&A详情见截图")


