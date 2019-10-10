from pxframe.pxutil import *


class PersonalSetting(TestBase2):
    '''我的-设置与个人名片'''
    def test_updatepw(self):
        '''修改密码'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/iv_settimg").wait_for_appearance(5)
        poco("com.puxin.accountant:id/iv_settimg").click()
        sleep(2)
        if not poco("com.puxin.accountant:id/iv_error").exists():
            poco("com.puxin.accountant:id/tv_customer").click()
            poco("com.puxin.accountant:id/et_oldpassword").set_text(gwpwd)
            poco("com.puxin.accountant:id/et_first").set_text(gwpwd)
            poco("com.puxin.accountant:id/et_second").set_text(gwpwd)
            poco("com.puxin.accountant:id/bt_next").click()
            if poco("com.puxin.accountant:id/toolbar_title").get_text()=="修改密码":
                back()
                back()
                self.assertTrue(False, "密码修改功能有误")
            else:
                back()
                print("修改密码成功")
        else:
            print("网络连接有问题")
            back()

    def test_help(self):
        '''帮助中心'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/iv_settimg").wait_for_appearance(5)
        poco("com.puxin.accountant:id/iv_settimg").click()
        sleep(2)
        poco("com.puxin.accountant:id/tv_select_contact_date").click()
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        back(2)
        self.assertEqual(title,'帮助中心','帮助中心跳转后是{}'.format(title))
        print('帮助中心跳转正常')

    def test_feedback(self):
        '''意见反馈'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/iv_settimg").wait_for_appearance(5)
        poco("com.puxin.accountant:id/iv_settimg").click()
        sleep(2)
        if not poco("com.puxin.accountant:id/iv_error").exists():
            sleep(2)
            poco(text="意见反馈").click()
            poco("com.puxin.accountant:id/et_count").set_text("请至少输入15字以上！想了想也没什么可以拼凑的，不管字数够不够就这样了")
            poco("com.puxin.accountant:id/et_address").set_text("123@123.com")
            poco("com.puxin.accountant:id/bt_ok").click()
            if poco("com.puxin.accountant:id/toolbar_title").get_text()=="个人中心":
                print("添加留言成功")
                back()
            else:
                back()
                back()
                self.assertTrue(False, "服务器繁忙...1003")
        else:
            print("网络连接有问题")
            back()

    def test_version(self):
        '''版本号'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/iv_settimg").wait_for_appearance(5)
        poco("com.puxin.accountant:id/iv_settimg").click()
        sleep(2)
        if poco("com.puxin.accountant:id/tv_version").exists():
            print("当前APP的版本号是"+poco("com.puxin.accountant:id/tv_version").get_text())
            back()
        else:
            back()
            self.assertTrue(False, "版本号模块有误")

    def test_row(self):
        '''个人名片'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/iv_row").wait_for_appearance(5)
        name = poco("com.puxin.accountant:id/tv_name").get_text()
        poco("com.puxin.accountant:id/iv_row").click()
        sleep(3)
        title = poco("com.puxin.accountant:id/toolbar_title").get_text()
        snapshot('./pxcapture/{}个人名片.png'.format(name))
        back()
        self.assertEqual(title, '个人名片', '个人名片跳转后是{}'.format(title))
        print('个人名片跳转正常')