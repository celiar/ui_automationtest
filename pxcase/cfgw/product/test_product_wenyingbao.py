from pxframe.pxutil import *


class Wjb(TestBase):
    '''产品--稳金宝'''
    def test01(self):
        '''验证新增智信产品'''
        # 稳金宝--智信--募集中--第一个产品信息
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 1)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 1)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '稳金宝--智信--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_wenyingbao").click()
        poco("com.puxin.accountant:id/tv_type_name")[0].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                name = poco("com.puxin.accountant:id/fixed_name")[0].get_text()
            except:
                snapshot('./pxcapture/智信异常.png')
                back()
                self.assertTrue(False,'智信列表为空，或网络异常')
            back()
            self.assertEqual(names[0],name,'稳金宝顾问app智信产品是{}'.format(name))
            print('智信产品列表显示正常')
        else:
            back()
            print("网络连接有问题")

    def test02(self):
        '''验证智信产品明细'''
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 1)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 1)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '稳金宝--智信--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_wenyingbao").click()
        poco("com.puxin.accountant:id/tv_type_name")[0].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                poco("com.puxin.accountant:id/fixed_name")[0].click()
            except:
                back()
                snapshot('./pxcapture/智信异常.png')
                self.assertTrue(False, '智信列表为空，或网络异常')
            snapshot('./pxcapture/智信【{}】详情.png'.format(names[0]))
            back(2)
            print('智信详情见附件')
        else:
            back()
            print("网络连接有问题")

    def test03(self):
        '''验证新增惠盈产品'''
        # 稳金宝--惠盈--募集中--第一个产品信息
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 1)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 2)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '稳金宝--惠盈--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_wenyingbao").click()
        poco("com.puxin.accountant:id/tv_type_name")[1].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                name = poco("com.puxin.accountant:id/fixed_name")[0].get_text()
            except:
                snapshot('./pxcapture/惠盈异常.png')
                back()
                self.assertTrue(False, '惠盈列表为空，或网络异常')
            back()
            self.assertEqual(names[0], name, '稳金宝顾问app惠盈产品是{}'.format(name))
            print('惠盈产品列表显示正常')
        else:
            back()
            print("网络连接有问题")

    def test04(self):
        '''验证惠盈产品明细'''
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 1)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 2)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '稳金宝--惠盈--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_wenyingbao").click()
        poco("com.puxin.accountant:id/tv_type_name")[1].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                poco("com.puxin.accountant:id/fixed_name")[0].click()
            except:
                snapshot('./pxcapture/惠盈异常.png')
                back()
                self.assertTrue(False, '惠盈列表为空，或网络异常')
            snapshot('./pxcapture/惠盈【{}】详情.png'.format(names[0]))
            back(2)
            print('惠盈详情见附件')
        else:
            back()
            print("网络连接有问题")

    def test05(self):
        '''验证新增华裕产品'''
        # 稳金宝--华裕--募集中--第一个产品信息
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 1)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 3)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '稳金宝--华裕--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_wenyingbao").click()
        poco("com.puxin.accountant:id/tv_type_name")[2].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                name = poco("com.puxin.accountant:id/fixed_name")[0].get_text()
            except:
                snapshot('./pxcapture/华裕异常.png')
                back()
                self.assertTrue(False, '华裕列表为空，或网络异常')
            back()
            self.assertEqual(names[0], name, '稳金宝顾问app华裕产品是{}'.format(name))
            print('华裕产品列表显示正常')
        else:
            back()
            print("网络连接有问题")

    def test06(self):
        '''验证华裕产品明细'''
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 1)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 3)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '稳金宝--华裕--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_wenyingbao").click()
        poco("com.puxin.accountant:id/tv_type_name")[2].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                poco("com.puxin.accountant:id/fixed_name")[0].click()
            except:
                snapshot('./pxcapture/华裕异常.png')
                back()
                self.assertTrue(False, '华裕列表为空，或网络异常')
            snapshot('./pxcapture/华裕【{}】详情.png'.format(names[0]))
            back(2)
            print('华裕详情见附件')
        else:
            back()
            print("网络连接有问题")

    def test07(self):
        '''验证新增恒成'''
        # 稳金宝--恒成--募集中--第一个产品信息
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 1)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 4)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '稳金宝--恒成--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_wenyingbao").click()
        poco("com.puxin.accountant:id/tv_type_name")[3].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                name = poco("com.puxin.accountant:id/fixed_name")[0].get_text()
            except:
                snapshot('./pxcapture/恒成异常.png')
                back()
                self.assertTrue(False, '恒成列表为空，或网络异常')
            back()
            self.assertEqual(names[0], name, '稳金宝顾问app恒成产品是{}'.format(name))
            print('恒成产品列表显示正常')
        else:
            back()
            print("网络连接有问题")

    def test08(self):
        '''验证恒成产品明细'''
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 1)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 4)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '稳金宝--恒成--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_wenyingbao").click()
        poco("com.puxin.accountant:id/tv_type_name")[3].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                poco("com.puxin.accountant:id/fixed_name")[0].click()
            except:
                snapshot('./pxcapture/恒成异常.png')
                back()
                self.assertTrue(False, '恒成列表为空，或网络异常')
            snapshot('./pxcapture/恒成【{}】详情.png'.format(names[0]))
            back(2)
            print('恒成详情见附件')
        else:
            back()
            print("网络连接有问题")

    # @unittest.skip('根据项目需要，增加脚本')
    def test09(self):
        '''验证新增第五项'''
        # 稳金宝--第五项--募集中--第一个产品信息
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 1)
        l.click('产品列表', '产品子类')
        try:
            l.clicks('产品子类', '选项', 5)
        except:
            self.assertTrue(False,'稳金宝子类不存在第五项')
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '稳金宝--第五项--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_wenyingbao").click()
        poco("com.puxin.accountant:id/tv_type_name")[4].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                name = poco("com.puxin.accountant:id/fixed_name")[0].get_text()
            except:
                snapshot('./pxcapture/第五项异常.png')
                back()
                self.assertTrue(False, '第五项列表为空，或网络异常')
            back()
            self.assertEqual(names[0], name, '稳金宝顾问app第五项产品是{}'.format(name))
            print('第五项产品列表显示正常')
        else:
            back()
            print("网络连接有问题")
