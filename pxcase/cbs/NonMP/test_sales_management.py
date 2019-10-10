from pxframe.pxutil import *


class SalesManagement(TestBaseWeb):
    '''销售管理'''
    def test_01_searchAccountList01(self):
        '''到账列表--募集账号'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '到账列表')
        l.send_keys('到账列表', '募集账号', "a")
        l.click('到账列表', '查询')

    def test_01_searchAccountList02(self):
        '''到账列表--对方姓名'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '到账列表')
        l.send_keys('到账列表', '对方姓名', "a")
        l.click('到账列表', '查询')

    def test_01_searchAccountList03(self):
        '''到账列表--对方账户'''
        l = self.locator
        l.move_to('主页','销售管理')
        l.click('销售管理', '到账列表')
        l.send_keys('到账列表', '对方账户', "a")
        l.click('到账列表', '查询')

    def test_01_searchAccountList04(self):
        '''到账列表--预约流水匹配状态'''
        l = self.locator
        l.move_to('主页','销售管理')
        l.click('销售管理', '到账列表')
        for i in range(len(l.get_elements('预约流水匹配状态', '选项'))):
            l.click('到账列表', '预约流水匹配状态')
            l.clicks('预约流水匹配状态', '选项', i)
            l.click('到账列表', '查询')

    def test_01_searchAccountList05(self):
        '''到账列表--预约单号'''
        l = self.locator
        l.move_to('主页','销售管理')
        l.click('销售管理', '到账列表')
        l.send_keys('到账列表', '预约单号', "a")
        l.click('到账列表', '查询')

    def test_01_searchAccountList06(self):
        '''到账列表--匹配结果'''
        l = self.locator
        l.move_to('主页','销售管理')
        l.click('销售管理', '到账列表')
        for i in range(len(l.get_elements('匹配结果', '选项'))):
            l.click('到账列表', '匹配结果')
            l.clicks('匹配结果', '选项', i)
            l.click('到账列表', '查询')

    def test_02_bookingList01(self):
        '''预约列表--产品名称'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '预约列表')
        l.send_keys('预约列表', '产品名称', "a")
        l.click('预约列表', '查询')

    def test_02_bookingList02(self):
        '''预约列表--产品大类--产品子类'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '预约列表')
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('预约列表', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('预约列表', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('预约列表', '查询')

    def test_02_bookingList03(self):
        '''预约列表--客户姓名'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '预约列表')
        l.send_keys('预约列表', '客户姓名', "a")
        l.click('预约列表', '查询')

    def test_02_bookingList04(self):
        '''预约列表--预约流水匹配状态'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '预约列表')
        for i in range(len(l.get_elements('预约流水匹配状态', '选项'))):
            l.click('预约列表', '预约流水匹配状态')
            l.clicks('预约流水匹配状态', '选项', i)
            l.click('预约列表', '查询')

    def test_02_bookingList05(self):
        '''预约列表--交易状态'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '预约列表')
        for i in range(len(l.get_elements('交易状态', '选项'))):
            l.click('预约列表', '交易状态')
            l.clicks('交易状态', '选项', i)
            l.click('预约列表', '查询')

    def test_02_bookingList06(self):
        '''预约列表--所属顾问'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '预约列表')
        l.send_keys('预约列表', '所属顾问', "a")
        l.click('预约列表', '查询')

    def test_02_bookingList07(self):
        '''预约列表--顾问所属机构'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '预约列表')
        l.send_keys('预约列表', '顾问所属机构', "a")
        l.click('预约列表', '查询')

    def test_02_bookingList08(self):
        '''预约列表--预约单号'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '预约列表')
        l.send_keys('预约列表', '预约单号', "a")
        l.click('预约列表', '查询')

    def test_02_bookingList09(self):
        '''预约列表--合同编号'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '预约列表')
        l.send_keys('预约列表', '合同编号', "a")
        l.click('预约列表', '查询')

    def test_02_bookingList10(self):
        '''预约列表--银行卡号'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '预约列表')
        l.send_keys('预约列表', '银行卡号', "a")
        l.click('预约列表', '查询')

    def test_03_declarationList01(self):
        '''报单列表--审核状态'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '报单列表')
        for i in range(len(l.get_elements('审核状态', '选项'))):
            l.click('报单列表', '审核状态')
            l.clicks('审核状态', '选项', i)
            l.click('报单列表', '查询')

    def test_03_declarationList02(self):
        '''报单列表--产品名称'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '报单列表')
        l.send_keys('报单列表', '产品名称', "a")
        l.click('报单列表', '查询')

    def test_03_declarationList03(self):
        '''报单列表--客户姓名'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '报单列表')
        l.send_keys('报单列表', '客户姓名', "a")
        l.click('报单列表', '查询')

    def test_03_declarationList04(self):
        '''报单列表--交易状态'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '报单列表')
        for i in range(len(l.get_elements('交易状态', '选项'))):
            l.click('报单列表', '交易状态')
            l.clicks('交易状态', '选项', i)
            l.click('报单列表', '查询')

    def test_03_declarationList05(self):
        '''报单列表--所属顾问'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '报单列表')
        l.send_keys('报单列表', '所属顾问', "a")
        l.click('报单列表', '查询')

    def test_03_declarationList06(self):
        '''报单列表--所属机构'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '报单列表')
        l.send_keys('报单列表', '所属机构', "a")
        l.click('报单列表', '查询')

    def test_03_declarationList07(self):
        '''报单列表--预约单号'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '报单列表')
        l.send_keys('报单列表', '预约单号', "a")
        l.click('报单列表', '查询')

    def test_04_refundList(self):
        '''我的清算--all'''
        # 我的清算列表为空，暂时不予添加检查点
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '我的清算')
        l.send_keys('我的清算', '客户姓名', "a")
        l.click('我的清算', '查询')
        l.send_keys('我的清算', '证件号码', "a")
        l.click('我的清算', '查询')
        l.send_keys('我的清算', '产品名称', "a")
        l.click('我的清算', '查询')
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('我的清算', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('我的清算', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('我的清算', '查询')
        for k in range(len(l.get_elements('交易状态', '选项'))):
            l.click('我的清算', '交易状态')
            l.clicks('交易状态', '选项', k)
            l.click('我的清算', '查询')

    def test_05_shareImportSearch(self):
        '''导入份额列表--导入文件名'''
        # 导入份额列表为空，暂不予添加检查点
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '导入份额列表')
        l.send_keys('导入份额列表', '导入文件名', "a")
        l.click('导入份额列表', '查询')

    def test_06_customerShareSearch(self):
        '''客户份额列表--all'''
        # 客户份额列表为空，暂不予添加检查点
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '客户份额列表')
        l.send_keys('客户份额列表', '客户姓名', "a")
        l.click('客户份额列表', '查询')
        l.send_keys('客户份额列表', '证件号码', "a")
        l.click('客户份额列表', '查询')
        l.send_keys('客户份额列表', '产品名称', "a")
        l.click('客户份额列表', '查询')

    def test_07_findLiquTradeOrderList(self):
        '''赎回列表--all'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '赎回列表')
        l.send_keys('赎回列表', '客户姓名', "a")
        l.click('赎回列表', '查询')
        l.send_keys('赎回列表', '证件号码', "a")
        l.click('赎回列表', '查询')
        l.send_keys('赎回列表', '产品名称', "a")
        l.click('赎回列表', '查询')
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('赎回列表', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('赎回列表', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('赎回列表', '查询')

    def test_08_getHoldList01(self):
        '''继续持有列表--产品名称'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '继续持有列表')
        l.send_keys('继续持有列表', '产品名称', "a")
        l.click('继续持有列表', '查询')

    def test_08_getHoldList02(self):
        '''继续持有列表--产品大类--产品子类'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '继续持有列表')
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('继续持有列表', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('继续持有列表', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('继续持有列表', '查询')

    def test_08_getHoldList03(self):
        '''继续持有列表--客户姓名'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '继续持有列表')
        l.send_keys('继续持有列表', '客户姓名', "a")
        l.click('继续持有列表', '查询')

    def test_08_getHoldList04(self):
        '''继续持有列表--财富顾问'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '继续持有列表')
        l.send_keys('继续持有列表', '财富顾问', "a")
        l.click('继续持有列表', '查询')

    def test_08_getHoldList05(self):
        '''继续持有列表--所属机构'''
        l = self.locator
        l.move_to('主页', '销售管理')
        l.click('销售管理', '继续持有列表')
        l.send_keys('继续持有列表', '所属机构', "a")
        l.click('继续持有列表', '查询')
