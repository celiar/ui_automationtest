from pxframe.pxutil import *


class ProductManagement(TestBaseWeb):
    '''产品管理'''
    def test_01_myProduct01(self):
        '''我的产品--产品名称'''
        l = self.locator
        l.move_to('主页','产品管理')
        l.click('产品管理', '我的产品')
        l.send_keys('我的产品', '产品名称', "a")
        l.click('我的产品', '查询')

    def test_01_myProduct02(self):
        '''我的产品--产品大类'''
        l = self.locator
        l.move_to('主页','产品管理')
        l.click('产品管理', '我的产品')
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('我的产品', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('我的产品', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('我的产品', '查询')

    def test_01_myProduct03(self):
        '''我的产品--审核状态'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '我的产品')
        for k in range(len(l.get_elements('审核状态', '选项'))):
            l.click('我的产品', '审核状态')
            l.clicks('审核状态', '选项', k)
            l.click('我的产品', '查询')

    def test_01_myProduct04(self):
        '''我的产品--产品来源'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '我的产品')
        for k in range(len(l.get_elements('产品来源', '选项'))):
            l.click('我的产品', '产品来源')
            l.clicks('产品来源', '选项', k)
            l.click('我的产品', '查询')

    def test_01_myProduct05(self):
        '''我的产品--募集类型'''
        l = self.locator
        l.move_to('主页','产品管理')
        l.click('产品管理', '我的产品')
        for k in range(len(l.get_elements('募集类型', '选项'))):
            l.click('我的产品', '募集类型')
            l.clicks('募集类型', '选项', k)
            l.click('我的产品', '查询')

    def test_02_productList01(self):
        '''产品列表--产品名称'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品列表')
        l.send_keys('产品列表', '产品名称', "a")
        l.click('产品列表', '查询')

    def test_02_productList02(self):
        '''产品列表--产品大类'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品列表')
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('产品列表', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('产品列表', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('产品列表', '查询')

    def test_02_productList03(self):
        '''产品列表--募集类型'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品列表')
        for k in range(len(l.get_elements('募集类型', '选项'))):
            l.click('产品列表', '募集类型')
            l.clicks('募集类型', '选项', k)
            l.click('产品列表', '查询')

    def test_02_productList04(self):
        '''产品列表--审核状态'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品列表')
        for k in range(len(l.get_elements('审核状态', '选项'))):
            l.click('产品列表', '审核状态')
            l.clicks('审核状态', '选项', k)
            l.click('产品列表', '查询')

    def test_02_productList05(self):
        '''产品列表--产品状态'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品列表')
        for k in range(len(l.get_elements('产品状态', '选项'))):
            l.click('产品列表', '产品状态')
            l.clicks('产品状态', '选项', k)
            l.click('产品列表', '查询')

    def test_02_productList06(self):
        '''产品列表--产品来源'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品列表')
        for k in range(len(l.get_elements('产品来源', '选项'))):
            l.click('产品列表', '产品来源')
            l.clicks('产品来源', '选项', k)
            l.click('产品列表', '查询')

    def test_02_productList07(self):
        '''产品列表--合同状态'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品列表')
        for k in range(len(l.get_elements('合同状态', '选项'))):
            l.click('产品列表', '合同状态')
            l.clicks('合同状态', '选项', k)
            l.click('产品列表', '查询')

    def test_03_productAudit01(self):
        '''产品审核--产品名称'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品审核')
        l.send_keys('产品审核', '产品名称', "a")
        l.click('产品审核', '查询')

    def test_03_productAudit02(self):
        '''产品审核--产品大类'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品审核')
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('产品审核', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('产品审核', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('产品审核', '查询')

    def test_03_productAudit03(self):
        '''产品审核--募集类型'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品审核')
        for k in range(len(l.get_elements('募集类型', '选项'))):
            l.click('产品审核', '募集类型')
            l.clicks('募集类型', '选项', k)
            l.click('产品审核', '查询')

    def test_03_productAudit04(self):
        '''产品审核--审核状态'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品审核')
        for k in range(len(l.get_elements('审核状态', '选项'))):
            l.click('产品审核', '审核状态')
            l.clicks('审核状态', '选项', k)
            l.click('产品审核', '查询')

    def test_03_productAudit05(self):
        '''产品审核--产品状态'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品审核')
        for k in range(len(l.get_elements('产品状态', '选项'))):
            l.click('产品审核', '产品状态')
            l.clicks('产品状态', '选项', k)
            l.click('产品审核', '查询')

    def test_03_productAudit06(self):
        '''产品审核--产品来源'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品审核')
        for k in range(len(l.get_elements('产品来源', '选项'))):
            l.click('产品审核', '产品来源')
            l.clicks('产品来源', '选项', k)
            l.click('产品审核', '查询')

    def test_03_productAudit07(self):
        '''产品审核--申请操作'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品审核')
        for k in range(len(l.get_elements('申请操作', '选项'))):
            l.click('产品审核', '申请操作')
            l.clicks('申请操作', '选项', k)
            l.click('产品审核', '查询')

    def test_04_productAudit01(self):
        '''产品类别--新增--取消'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '产品类别')
        l.click('产品类别', '新增子类')
        for k in range(len(l.get_elements('产品大类名称', '选项'))):
            l.click('新增子类', '产品大类名称')
            l.clicks('产品大类名称', '选项', k)
        l.send_keys('新增子类', '产品子类名称','汇鑫')
        l.send_keys('新增子类', '备注', '备注一下')
        l.click("新增子类","取消")

    def test_05_survivingList01(self):
        '''存续列表--输入项'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.clicks('产品管理', '存续列表',0)
        l.send_keys('存续列表', '预约单号', "a")
        l.send_keys('存续列表', '产品名称', "a")
        l.send_keys('存续列表', '客户姓名', "a")
        l.send_keys('存续列表', '客户证件号', "a")
        l.send_keys('存续列表', '客户手机号', "a")
        l.send_keys('存续列表', '所属顾问', "a")
        l.send_keys('存续列表', '顾问所属机构', "a")
        l.click('存续列表', '查询')

    def test_05_survivingList02(self):
        '''存续列表--产品大类'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.clicks('产品管理', '存续列表',0)
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('存续列表', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('存续列表', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('存续列表', '查询')

    def test_05_survivingList03(self):
        '''存续列表--募集类型'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.clicks('产品管理', '存续列表', 0)
        for k in range(len(l.get_elements('募集类型', '选项'))):
            l.click('存续列表', '募集类型')
            l.clicks('募集类型', '选项', k)
            l.click('存续列表', '查询')

    def test_05_survivingList04(self):
        '''存续列表--交易状态'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.clicks('产品管理', '存续列表', 0)
        for k in range(len(l.get_elements('交易状态', '选项'))):
            l.click('存续列表', '交易状态')
            l.clicks('交易状态', '选项', k)
            l.click('存续列表', '查询')

    def test_05_survivingList05(self):
        '''存续列表--是否下发佣金'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.clicks('产品管理', '存续列表', 0)
        for k in range(len(l.get_elements('是否下发佣金', '选项'))):
            l.click('存续列表', '是否下发佣金')
            l.clicks('是否下发佣金', '选项', k)
            l.click('存续列表', '查询')


    def test_06_liquidationList01(self):
        '''清算列表--产品名称'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.clicks('产品管理', '清算列表', 1)
        l.send_keys('清算列表', '产品名称', "a")
        l.click('清算列表', '查询')

    def test_06_liquidationList02(self):
        '''清算列表--产品大类'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.clicks('产品管理', '清算列表', 1)
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('清算列表', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('清算列表', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('清算列表', '查询')

    def test_06_liquidationList03(self):
        '''清算列表--产品状态'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.clicks('产品管理', '清算列表', 1)
        for k in range(len(l.get_elements('产品状态', '选项'))):
            l.click('清算列表', '产品状态')
            l.clicks('产品状态', '选项', k)
            l.click('清算列表', '查询')

    def test_06_liquidationList04(self):
        '''清算列表--审核状态'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.clicks('产品管理', '清算列表', 1)
        for k in range(len(l.get_elements('审核状态', '选项'))):
            l.click('清算列表', '审核状态')
            l.clicks('审核状态', '选项', k)
            l.click('清算列表', '查询')

    def test_06_liquidationList05(self):
        '''清算列表--收益模式'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.clicks('产品管理', '清算列表', 1)
        for k in range(len(l.get_elements('收益模式', '选项'))):
            l.click('清算列表', '收益模式')
            l.clicks('收益模式', '选项', k)
            l.click('清算列表', '查询')

    def test_07_getLiquidationAuditList01(self):
        '''清算审核--产品名称'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '清算审核')
        l.send_keys('清算审核', '产品名称', "a")
        l.click('清算审核', '查询')

    def test_07_getLiquidationAuditList02(self):
        '''清算审核--产品大类'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '清算审核')
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('清算审核', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('清算审核', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('清算审核', '查询')

    def test_07_getLiquidationAuditList03(self):
        '''清算审核--产品状态'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '清算审核')
        for k in range(len(l.get_elements('产品状态', '选项'))):
            l.click('清算审核', '产品状态')
            l.clicks('产品状态', '选项', k)
            l.click('清算审核', '查询')

    def test_07_getLiquidationAuditList04(self):
        '''清算审核--审核状态'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '清算审核')
        for k in range(len(l.get_elements('审核状态', '选项'))):
            l.click('清算审核', '审核状态')
            l.clicks('审核状态', '选项', k)
            l.click('清算审核', '查询')

    def test_07_getLiquidationAuditList05(self):
        '''清算审核--收益模式'''
        l = self.locator
        l.move_to('主页', '产品管理')
        l.click('产品管理', '清算审核')
        for k in range(len(l.get_elements('收益模式', '选项'))):
            l.click('清算审核', '收益模式')
            l.clicks('收益模式', '选项', k)
            l.click('清算审核', '查询')
