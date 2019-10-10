from pxframe.pxutil import *


class CustomerContact(TestBase2):
    '''首页-客户管理'''
    def test_add_contact(self):
        '''新增沟通记录'''
        poco(text="首页").click()
        poco("com.puxin.accountant:id/rl_contact").click()
        poco("com.puxin.accountant:id/iv_share").click()
        poco("com.puxin.accountant:id/tv_customer").click()
        sleep(3)
        if not poco("com.puxin.accountant:id/name").exists():
            poco("com.puxin.accountant:id/search_cancel").click()
            back(2)
            print("网络连接有问题")
        else:
            poco("com.puxin.accountant:id/name").click()
            poco("com.puxin.accountant:id/et_contact_address").set_text("国贸大酒店101房间")
            poco("com.puxin.accountant:id/tv_select_contact_date").click()
            poco("com.puxin.accountant:id/btnSubmit").click()
            a = random.randint(1000,9999)
            poco("com.puxin.accountant:id/et_content").set_text("中国尊会见厅"+str(a))
            poco("com.puxin.accountant:id/iv_share").click()
            if poco("com.puxin.accountant:id/toolbar_title").get_text()=="添加记录":
                back(2)
                self.assertTrue(False,"添加记录功能有误")
            else:
                back()
                print("添加沟通记录功能正常")

    def test_del_contact(self):
        '''删除沟通记录'''
        #需有增加沟通记录用例，否则该用例废弃
        poco(text="首页").click()
        poco("com.puxin.accountant:id/rl_contact").click()
        if poco("com.puxin.accountant:id/iv_error").exists():
            back()
            print("网络连接有问题,或无沟通记录")
        else:
            content = poco("com.puxin.accountant:id/tv_content").get_text()
            poco("com.puxin.accountant:id/tv_content").click()
            poco("com.puxin.accountant:id/tv_submit").click()
            poco("com.puxin.accountant:id/btn_dialog_simple_enter").click()
            if poco("com.puxin.accountant:id/tv_content").exists() and poco("com.puxin.accountant:id/tv_content").get_text()==content:
                back()
                self.assertTrue(False,"删除沟通记录失败")
            else:
                back()
                print("删除沟通记录成功")

    def test_customer_jump(self):
        '''检查主页我的客户跳转'''
        poco(text="首页").click()
        poco("com.puxin.accountant:id/rl_customer").click()
        if poco("com.puxin.accountant:id/title").get_text()=="客户":
            print("我的客户页面跳转成功")
        else:
            self.assertTrue(False,"我的客户页面跳转失败")


