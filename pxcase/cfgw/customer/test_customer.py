from pxframe.pxutil import *


class CustomerPage(TestBase2):
    '''客户页面'''
    def test_birth_remind(self):
        '''检查生日提醒'''
        poco(text="客户").click()
        poco("com.puxin.accountant:id/icon_birth").wait_for_appearance()
        poco("com.puxin.accountant:id/icon_birth").click()
        sleep(2)
        try:
            title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        except:
            title = None
        self.assertEqual(title,'生日提醒','生日提醒模块有误')
        back()
        print('生日提醒跳转后页面标题是{}'.format(title))

    def test_add_customer(self):
        '''客户开户'''
        poco(text="客户").click()
        poco("com.puxin.accountant:id/tv_add_customer").wait_for_appearance(2)
        poco("com.puxin.accountant:id/tv_add_customer").click()
        sleep(2)
        try:
            title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        except:
            title = None
        self.assertEqual(title, '客户开户', '客户开户模块有误')
        back()
        print('客户开户跳转后页面标题是{}'.format(title))

    def test_customerpage(self):
        '''验证客户页'''
        poco(text="客户").click()
        # sleep(3)
        try:
            name = poco("com.puxin.accountant:id/name")[0].get_text()
        except:
            self.assertTrue(False,"网络连接有问题，或客户数量为0，请检查APP")
        poco("com.puxin.accountant:id/name")[0].click()
        sleep(2)
        try:
            title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        except:
            title = None
        self.assertEqual(title, name, '客户跳转后详情页的姓名有误')
        back()
        print('客户详情跳转后页面标题是{}'.format(title))

    def test_investinfo(self):
        '''获取客户投资情况'''
        poco(text="客户").click()
        if not poco("com.puxin.accountant:id/iv_error").exists():
            # poco("com.puxin.accountant:id/refresh_layout").swipe([0, 0.5])
            # sleep(2)
            name = poco("com.puxin.accountant:id/name")[0].get_text()
            poco("com.puxin.accountant:id/name")[0].click()
            try:
                poco(text="投资情况").click()
            except:
                poco(text="投资情况").wait_for_appearance(5)
                poco(text="投资情况").click()
            poco("com.puxin.accountant:id/recyclerview").swipe([0, 0.5])
            sleep(4)
            total_value = poco("com.puxin.accountant:id/total_value").get_text()
            title = poco("com.puxin.accountant:id/title")
            amount = poco("com.puxin.accountant:id/sub_title")
            for i in range(len(title)):
                print("{}客户：{}的投资金额是{}万元".format(name,title[i].get_text(), amount[i].get_text()))
            print("总投资额为{}万元".format(total_value))
            back()
        else:
            back()
            print("网络连接有问题，或客户数量为0，请检查APP")

    def test_customerinfo(self):
        '''获取客户详情'''
        poco(text="客户").click()
        if not poco("com.puxin.accountant:id/iv_error").exists():
            # poco("com.puxin.accountant:id/refresh_layout").swipe([0, 0.5])
            # sleep(2)
            name = poco("com.puxin.accountant:id/name")[0].get_text()
            poco("com.puxin.accountant:id/name")[0].click()
            try:
                poco(text="客户详情").click()
            except:
                poco(text="客户详情").wait_for_appearance(5)
                poco(text="客户详情").click()
            snapshot("./pxcapture/{}详情.png".format(name))
            back()
        else:
            back()
            print("网络连接有问题，或客户数量为0，请检查APP")
        print("客户详情见截图")

    def test_phone_jump(self):
        '''点击电话按钮'''
        poco(text="客户").click()
        # sleep(3)
        poco("com.puxin.accountant:id/phone_icon")[0].click()
        if not poco("com.puxin.accountant:id/title").exists():
            try:
                mobile = poco("com.samsung.android.dialer:id/digits").get_text()
            except:
                mobile = poco("com.android.contacts:id/digits").get_text()
            else:
                mobile = None
                print('因手机型号问题，请检查手机号相关的代码')
            keyevent("BACK")
            keyevent("BACK")
            sleep(2)
            title = poco("com.puxin.accountant:id/title").get_text()
            print("手机号是{}，回退后显示页面为【{}】".format(mobile,title))
        else:
            keyevent("BACK")
            self.assertTrue(False,"电话按钮功能有误")

    def test_search1_name(self):
        '''搜索列表存在的客户姓名'''
        poco(text="客户").click()
        try:
            name = poco("com.puxin.accountant:id/name")[0].get_text()
        except:
            self.assertTrue(False,"网络连接有问题，或客户数量为0，请检查APP")
        poco("com.puxin.accountant:id/icon_search").click()
        poco("com.puxin.accountant:id/search_edit").set_text(name)
        keyevent("ENTER")
        poco("com.puxin.accountant:id/name").wait_for_appearance(5)
        name2 = poco("com.puxin.accountant:id/name").get_text()
        if name == name2:
            print("搜索后显示的客户姓名为{}".format(name2))
            poco("com.puxin.accountant:id/search_cancel").click()
        else:
            poco("com.puxin.accountant:id/search_cancel").click()
            self.assertTrue(False, "搜索客户姓名功能有误")

    def test_search2_name(self):
        '''搜索列表不存在的客户姓名'''
        poco(text="客户").click()
        name1 = "佛拉基米尔"
        # num1 = "15389898989"
        poco("com.puxin.accountant:id/icon_search").click()
        poco("com.puxin.accountant:id/search_edit").set_text(name1)
        keyevent("ENTER")
        sleep(4)
        if poco("com.puxin.accountant:id/name").exists():
            name2 = poco("com.puxin.accountant:id/name").get_text()
            poco("com.puxin.accountant:id/search_cancel").click()
            self.assertTrue(False, "搜索后内容应为空，但显示的客户姓名为{}".format(name2))
        else:
            poco("com.puxin.accountant:id/search_cancel").click()
            print("在列表搜索不存在【{}】，该功能正常".format(name1))

    def test_search3_phone(self):
        '''搜索列表不存在的客户手机号'''
        poco(text="客户").click()
        mobile = '19999999999'
        poco("com.puxin.accountant:id/icon_search").click()
        poco("com.puxin.accountant:id/search_edit").set_text(mobile)
        keyevent("ENTER")
        sleep(4)
        if poco("com.puxin.accountant:id/name").exists():
            poco("com.puxin.accountant:id/search_cancel").click()
            self.assertTrue(False,'搜索功能异常')
        else:
            poco("com.puxin.accountant:id/search_cancel").click()
            print("网络异常，或不存在该用户信息")

    def test_news_jump(self):
        '''验证信息披露'''
        poco(text="客户").click()
        poco("com.puxin.accountant:id/icon_news").wait_for_appearance(2)
        poco("com.puxin.accountant:id/icon_news").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        back()
        self.assertEqual(title,'信息披露','显示的页面是{}'.format(title))
        print('信息披露页面跳转正常')