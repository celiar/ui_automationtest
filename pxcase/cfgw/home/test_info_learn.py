from pxframe.pxutil import *


class InfoLearn(TestBase2):
    '''首页-资讯学习'''
    def test1(self):
        '''每日分享列表'''
        # CMS提供每日分享信息
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_share").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")
        self.assertEqual(title,'每日分享','每日分享跳转页面是{}'.format(title))
        print('每日分享跳转正常')


    def test2(self):
        '''每日分享详情'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_share").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        self.assertEqual(title, '每日分享', '每日分享跳转页面是{}'.format(title))
        try:
            title2 = poco("com.puxin.accountant:id/tv_title").get_text()
        except:
            back()
            self.assertTrue(False,'每日分享列表为空，或网络异常')
        poco("com.puxin.accountant:id/tv_title").click()
        poco("com.puxin.accountant:id/iv_share").click()
        snapp(title+'-'+title2)
        try:
            poco(text="取消分享").click()
        except:
            keyevent('KEYCODE_BACK')
            back(2)
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False,'分享功能异常')
        back(2)
        swipe_up("com.puxin.accountant:id/fl_tab_container")
        print('每日分享详情见截图')


    def test3(self):
        '''精彩瞬间列表'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_wonderful").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")
        self.assertEqual(title, '精彩瞬间', '精彩瞬间跳转页面是{}'.format(title))
        print('精彩瞬间跳转正常')

    def test4(self):
        '''精彩瞬间详情'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_wonderful").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        try:
            title2 = poco("com.puxin.accountant:id/tv_title").get_text()
        except:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False,'精彩瞬间列表为空，或网络异常')
        poco("com.puxin.accountant:id/tv_title").click()
        try:
            poco("com.puxin.accountant:id/center_start").click()
            snapp(title+'-'+title2)
        except:
            snapp(title + '-' + title2)
            keyevent("BACK")
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False,'精彩瞬间播放功能异常')
        keyevent("BACK")
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")
        print('精彩瞬间详情见截图')

    def test5(self):
        '''课程中心列表'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/tv_course_center").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title=='课程中心':
            print('课程中心跳转正常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False,'课程中心跳转页面是{}'.format(title))
        try:
            while True:
                a1 = len(poco("android.widget.TextView"))
                v1 = poco("android.widget.TextView")[a1 - 1].get_text()
                poco("android.widget.TextView")[a1 - 1].click()
                a2 = len(poco("android.widget.TextView"))
                v2 = poco("android.widget.TextView")[a2 - 1].get_text()
                # print(v1, v2)
                if v1 == v2:
                    break
        except:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False,'课程中心菜单跳转异常')
        print('课程中心菜单跳转正常')
        try:
            poco("com.puxin.accountant:id/tab_layout").swipe([-10, 0])
            sleep(1)
            snapp(title+'列表导航')
            poco("com.puxin.accountant:id/tab_layout").swipe([10, 0])
        except:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False,'课程中心导航栏滑动异常')
        print('课程中心导航栏滑动正常')
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")

    @unittest.skip("模块异常，无法加载信息")
    def test6(self):
        '''课程中心详情'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/tv_course_center").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '课程中心':
            print('课程中心跳转正常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False, '课程中心跳转页面是{}'.format(title))
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")

    def test7(self):
        '''知识库列表'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/tv_repository").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title=='知识库':
            print('知识库跳转正常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False,'知识库跳转页面是{}'.format(title))
        try:
            while True:
                a1 = len(poco("android.widget.TextView"))
                v1 = poco("android.widget.TextView")[a1 - 1].get_text()
                poco("android.widget.TextView")[a1 - 1].click()
                a2 = len(poco("android.widget.TextView"))
                v2 = poco("android.widget.TextView")[a2 - 1].get_text()
                # print(v1, v2)
                if v1 == v2:
                    break
        except:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False,'知识库菜单跳转异常')
        print('知识库菜单跳转正常')
        try:
            poco("com.puxin.accountant:id/tab_layout").swipe([-10, 0])
            sleep(1)
            snapp(title+'列表导航')
            poco("com.puxin.accountant:id/tab_layout").swipe([10, 0])
        except:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False,'知识库导航栏滑动异常')
        print('知识库导航栏滑动正常')
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")

    @unittest.skip("模块异常，无法加载信息")
    def test8(self):
        '''知识库详情'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/tv_repository").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '知识库':
            print('知识库跳转正常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False, '知识库跳转页面是{}'.format(title))
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")

    def test9(self):
        '''线下培训列表'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/tv_offline").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title=='线下培训':
            print('线下培训跳转正常')
            try:
                title2 = poco("com.puxin.accountant:id/tv_title").get_text()
                time2 = poco("com.puxin.accountant:id/tv_time").get_text()
                print(title2,time2)
            except:
                back()
                swipe_up("com.puxin.accountant:id/fl_tab_container")
                self.assertTrue(False,'线下培训列表为空，或网络异常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False,'线下培训跳转页面是{}'.format(title))
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")

    @unittest.skip("模块异常，无法加载信息")
    def test10(self):
        '''线下培训详情'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/tv_offline").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '线下培训':
            print('线下培训跳转正常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False, '线下培训跳转页面是{}'.format(title))
        swipe_up("com.puxin.accountant:id/fl_tab_container")
        back()

    def test11(self):
        '''投研报告列表'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_vision").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title=='投研报告':
            print('投研报告跳转正常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False,'投研报告跳转页面是{}'.format(title))
        s = len(poco("com.puxin.accountant:id/tv_type_name"))
        v = []
        for i in range(s):
            try:
                poco("com.puxin.accountant:id/tv_type_name")[i].click()
                v.append(poco("com.puxin.accountant:id/tv_type_name")[i].get_text())
            except:
                back()
                swipe_up("com.puxin.accountant:id/fl_tab_container")
                self.assertTrue(False,'投研报告子菜单【{}】跳转异常'.format(i))
        print('投研报告菜单跳转正常,依次是', v)
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")

    @unittest.skip("模块异常，无法加载信息")
    def test12(self):
        '''投研报告详情'''
        poco(text="首页").click()
        swipe_down("com.puxin.accountant:id/rootview")
        poco("com.puxin.accountant:id/rl_vision").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        if title == '投研报告':
            print('投研报告跳转正常')
        else:
            back()
            swipe_up("com.puxin.accountant:id/fl_tab_container")
            self.assertTrue(False, '投研报告跳转页面是{}'.format(title))
        back()
        swipe_up("com.puxin.accountant:id/fl_tab_container")

