from pxframe.pxutil import *


class OnsaleProduct(TestBaseWeb):
    '''在售产品'''
    def test_01(self):
        '''产品名称--产品大类'''
        l = self.locator
        l.click('主页', '在售产品')
        l.send_keys('在售产品', '产品名称', "a")
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('在售产品', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('在售产品', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('在售产品', '查询')

    def test_02(self):
        '''产品组织形式'''
        l = self.locator
        l.click('主页', '在售产品')
        for k in range(len(l.get_elements('产品组织形式', '选项'))):
            l.click('在售产品', '产品组织形式')
            l.clicks('产品组织形式', '选项', k)
            l.click('在售产品', '查询')

    def test_03(self):
        '''产品状态'''
        l = self.locator
        l.click('主页', '在售产品')
        for k in range(len(l.get_elements('产品状态', '选项'))):
            l.click('在售产品', '产品状态')
            l.clicks('产品状态', '选项', k)
            l.click('在售产品', '查询')


    def test_04(self):
        '''产品来源'''
        l = self.locator
        l.click('主页', '在售产品')
        for k in range(len(l.get_elements('产品来源', '选项'))):
            l.click('在售产品', '产品来源')
            l.clicks('产品来源', '选项', k)
            l.click('在售产品', '查询')