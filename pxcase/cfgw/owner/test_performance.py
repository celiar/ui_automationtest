from pxframe.pxutil import *


class Performance(TestBase2):
    '''我的-业绩统计'''
    def test_performance01(self):
        '''折标业绩'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/tv_type").wait_for_appearance(5)
        if poco("com.puxin.accountant:id/tv_type").get_text() == "折标业绩":
            total = poco("com.puxin.accountant:id/total_value").get_text()
            print("折标业绩的总业绩为{}".format(total))
        else:
            poco("com.puxin.accountant:id/tv_type").click()
            poco("com.puxin.accountant:id/options1").swipe([0, 0.05])
            poco("com.puxin.accountant:id/btnSubmit").click()
            sleep(3)
            total = poco("com.puxin.accountant:id/total_value").get_text()
            print("折标业绩的总业绩为{}万元".format(total))

    def test_performance02(self):
        '''规模业绩'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/tv_type").wait_for_appearance(5)
        if poco("com.puxin.accountant:id/tv_type").get_text() == "规模业绩":
            total = poco("com.puxin.accountant:id/total_value").get_text()
            print("规模业绩的总业绩为{}".format(total))
        else:
            poco("com.puxin.accountant:id/tv_type").click()
            poco("com.puxin.accountant:id/options1").swipe([0, -0.05])
            poco("com.puxin.accountant:id/btnSubmit").click()
            sleep(3)
            total = poco("com.puxin.accountant:id/total_value").get_text()
            print("规模业绩的总业绩为{}".format(total))

    def test_percent(self):
        '''总业绩占比'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/tv_type").wait_for_appearance(5)
        poco("com.puxin.accountant:id/refresh_layout").swipe([0, 0.5])
        sleep(3)
        poco("com.puxin.accountant:id/refresh_layout").swipe([0, -1])
        a = poco("com.puxin.accountant:id/total_value").get_text()
        total = int(a)
        titles = poco("com.puxin.accountant:id/title")
        values = poco("com.puxin.accountant:id/sub_title")
        for i in range(4):
            print(titles[i].get_text()+values[i].get_text()+"万元")

    def test_simu_percent(self):
        '''私募基金占比'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/tv_type").wait_for_appearance(5)
        v = poco("com.puxin.accountant:id/fixedvalue").get_text()
        print("私募基金占比{}".format(v))

    def test_wenjinbao_percent(self):
        '''稳金宝占比'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/tv_type").wait_for_appearance(5)
        v = poco("com.puxin.accountant:id/stockvalue").get_text()
        sleep(2)
        print("稳金宝占比{}".format(v))

    def test_baoli_percent(self):
        '''保理产品占比'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/tv_type").wait_for_appearance(5)
        v = poco("com.puxin.accountant:id/insurancevalue").get_text()
        print("保理产品占比{}".format(v))

    def test_wangdai_percent(self):
        '''网贷产品占比'''
        poco(text="我的").click()
        poco("com.puxin.accountant:id/tv_type").wait_for_appearance(5)
        v = poco("com.puxin.accountant:id/netvalue").get_text()
        print("网贷产品占比{}".format(v))