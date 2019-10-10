from pxframe.pxutil import *


class Privatefund(TestBase):
    '''产品--私募基金'''
    def test01(self):
        '''验证新增类固收类产品'''
        # 私募基金--类固收类--募集中--第一个产品信息
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 2)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 1)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '私募基金--类固收类--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_private").click()
        poco("com.puxin.accountant:id/tv_type_name")[0].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                name = poco("com.puxin.accountant:id/fixed_name")[0].get_text()
            except:
                snapshot('./pxcapture/类固收类异常.png')
                back()
                self.assertTrue(False,'类固收类列表为空，或网络异常')
            back()
            self.assertEqual(names[0],name,'私募基金顾问app类固收类产品是{}'.format(name))
            print('类固收类产品列表显示正常')
        else:
            back()
            print("网络连接有问题")

    def test02(self):
        '''验证类固收类产品明细'''
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 2)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 1)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '私募基金--类固收类--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_private").click()
        poco("com.puxin.accountant:id/tv_type_name")[0].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                poco("com.puxin.accountant:id/fixed_name")[0].click()
            except:
                back()
                snapshot('./pxcapture/类固收类异常.png')
                self.assertTrue(False, '类固收类列表为空，或网络异常')
            snapshot('./pxcapture/类固收类【{}】详情.png'.format(names[0]))
            back(2)
            print('类固收类详情见附件')
        else:
            back()
            print("网络连接有问题")

    def test03(self):
        '''验证新增股权投资产品'''
        # 私募基金--股权投资--募集中--第一个产品信息
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 2)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 2)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '私募基金--股权投资--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_private").click()
        poco("com.puxin.accountant:id/tv_type_name")[1].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                name = poco("com.puxin.accountant:id/fixed_name")[0].get_text()
            except:
                snapshot('./pxcapture/股权投资异常.png')
                back()
                self.assertTrue(False, '股权投资列表为空，或网络异常')
            back()
            self.assertEqual(names[0], name, '私募基金顾问app股权投资产品是{}'.format(name))
            print('股权投资产品列表显示正常')
        else:
            back()
            print("网络连接有问题")

    def test04(self):
        '''验证股权投资产品明细'''
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 2)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 2)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '私募基金--股权投资--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_private").click()
        poco("com.puxin.accountant:id/tv_type_name")[1].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                poco("com.puxin.accountant:id/fixed_name")[0].click()
            except:
                snapshot('./pxcapture/股权投资异常.png')
                back()
                self.assertTrue(False, '股权投资列表为空，或网络异常')
            snapshot('./pxcapture/股权投资【{}】详情.png'.format(names[0]))
            back(2)
            print('股权投资详情见附件')
        else:
            back()
            print("网络连接有问题")

    def test05(self):
        '''验证新增私募证券产品'''
        # 私募基金--私募证券--募集中--第一个产品信息
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 2)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 3)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '私募基金--私募证券--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_private").click()
        poco("com.puxin.accountant:id/tv_type_name")[2].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                name = poco("com.puxin.accountant:id/fixed_name")[0].get_text()
            except:
                snapshot('./pxcapture/私募证券异常.png')
                back()
                self.assertTrue(False, '私募证券列表为空，或网络异常')
            back()
            self.assertEqual(names[0], name, '私募基金顾问app私募证券产品是{}'.format(name))
            print('私募证券产品列表显示正常')
        else:
            back()
            print("网络连接有问题")

    def test06(self):
        '''验证私募证券产品明细'''
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 2)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 3)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '私募基金--私募证券--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_private").click()
        poco("com.puxin.accountant:id/tv_type_name")[2].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                poco("com.puxin.accountant:id/fixed_name")[0].click()
            except:
                snapshot('./pxcapture/私募证券异常.png')
                back()
                self.assertTrue(False, '私募证券列表为空，或网络异常')
            snapshot('./pxcapture/私募证券【{}】详情.png'.format(names[0]))
            back(2)
            print('私募证券详情见附件')
        else:
            back()
            print("网络连接有问题")

    def test07(self):
        '''验证新增不良资产'''
        # 私募基金--不良资产--募集中--第一个产品信息
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 2)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 4)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '私募基金--不良资产--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_private").click()
        poco("com.puxin.accountant:id/tv_type_name")[3].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                name = poco("com.puxin.accountant:id/fixed_name")[0].get_text()
            except:
                snapshot('./pxcapture/不良资产异常.png')
                back()
                self.assertTrue(False, '不良资产列表为空，或网络异常')
            back()
            self.assertEqual(names[0], name, '私募基金顾问app不良资产产品是{}'.format(name))
            print('不良资产产品列表显示正常')
        else:
            back()
            print("网络连接有问题")

    def test08(self):
        '''验证不良资产产品明细'''
        l = self.locator
        l.open('http://newcbs.puxinzichan.com/product/productList')
        l.click('产品列表', '产品大类')
        l.clicks('产品大类', '选项', 2)
        l.click('产品列表', '产品子类')
        l.clicks('产品子类', '选项', 4)
        l.click('产品列表', '产品状态')
        l.clicks('产品状态', '选项', 2)
        sleep(1)
        l.click('产品列表', '查询')
        try:
            names = l.texts('产品列表', '产品名称')
        except:
            self.assertTrue(False, '私募基金--不良资产--募集中列表为空')

        poco(text="产品").click()
        poco("com.puxin.accountant:id/tv_private").click()
        poco("com.puxin.accountant:id/tv_type_name")[3].click()
        if not poco("com.puxin.accountant:id/iv_net_statu").exists():
            try:
                poco("com.puxin.accountant:id/fixed_name")[0].click()
            except:
                snapshot('./pxcapture/不良资产异常.png')
                back()
                self.assertTrue(False, '不良资产列表为空，或网络异常')
            snapshot('./pxcapture/不良资产【{}】详情.png'.format(names[0]))
            back(2)
            print('不良资产详情见附件')
        else:
            back()
            print("网络连接有问题")

    @unittest.skip('根据项目需要，增加脚本')
    def test09(self):
        '''验证新增测试子类1'''
        print('untest')
