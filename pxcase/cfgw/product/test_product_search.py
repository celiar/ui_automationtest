from pxframe.pxutil import *


class SearchProduct(TestBase2):
    '''产品-搜索产品'''

    def test01(self):
        '''搜索任意内容'''
        name1 = "稳金宝"
        poco(text="产品").click()
        poco("com.puxin.accountant:id/im_ph_search").click()
        poco("com.puxin.accountant:id/search_edit").set_text(name1)
        sleep(3)
        try:
            item = poco("com.puxin.accountant:id/tv_product_name")
        except:
            self.assertTrue(False, "搜索产品【{}】结果为空，请重新输入条件".format(name1))
        for i in range(len(item)):
            name2 = item[i].get_text()
            if name1 in name2:
                pass
            else:
                self.assertTrue(False, "搜索【{}】后列表不包含：{}".format(name2,name1))
        poco("com.puxin.accountant:id/iv_back").click()
        print("搜索产品【{}】结果显示正常".format(name1))
