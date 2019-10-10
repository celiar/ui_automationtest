from pxframe.pxutil import *


class ContractManagement(TestBaseWeb):
    '''合同管理'''
    def test_01_contractIssueListHQ01(self):
        '''历总--输入项'''
        l = self.locator
        l.move_to('主页','合同管理')
        l.click('合同管理', '历总')
        l.send_keys('历总', '产品名称', "a")
        l.send_keys('历总', '客户姓名', "a")
        l.send_keys('历总', '财富顾问', "a")
        l.send_keys('历总', '所属机构', "a")
        l.click('历总', '查询')

    def test_01_contractIssueListHQ02(self):
        '''历总--产品大类'''
        l = self.locator
        l.move_to('主页','合同管理')
        l.click('合同管理', '历总')
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('历总', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('历总', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('历总', '查询')

    def test_01_contractIssueListHQ03(self):
        '''历总--合同使用情况'''
        l = self.locator
        l.move_to('主页','合同管理')
        l.click('合同管理', '历总')
        for k in range(len(l.get_elements('合同使用情况', '选项'))):
            l.click('历总', '合同使用情况')
            l.clicks('合同使用情况', '选项', k)
            l.click('历总', '查询')


    def test_01_contractIssueListHQ04(self):
        '''历总--合同发放状态'''
        l = self.locator
        l.move_to('主页','合同管理')
        l.click('合同管理', '历总')
        for k in range(len(l.get_elements('合同发放状态', '选项'))):
            l.click('历总', '合同发放状态')
            l.clicks('合同发放状态', '选项', k)
            l.click('历总', '查询')

    def test_02_contractIssueListDepartment01(self):
        '''历分--输入项'''
        l = self.locator
        l.move_to('主页','合同管理')
        l.click('合同管理', '历分')
        l.send_keys('历分', '产品名称', "a")
        l.send_keys('历分', '客户姓名', "a")
        l.send_keys('历分', '财富顾问', "a")
        l.send_keys('历分', '所属机构', "a")
        l.click('历分', '查询')

    def test_02_contractIssueListDepartment02(self):
        '''历分--产品大类'''
        l = self.locator
        l.move_to('主页','合同管理')
        l.click('合同管理', '历分')
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('历分', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('历分', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('历分', '查询')

    def test_02_contractIssueListDepartment03(self):
        '''历分--合同使用情况'''
        l = self.locator
        l.move_to('主页','合同管理')
        l.click('合同管理', '历分')
        for k in range(len(l.get_elements('合同使用情况', '选项'))):
            l.click('历分', '合同使用情况')
            l.clicks('合同使用情况', '选项', k)
            l.click('历分', '查询')

    def test_02_contractIssueListDepartment04(self):
        '''历分--合同发放状态'''
        l = self.locator
        l.move_to('主页','合同管理')
        l.click('合同管理', '历分')
        for k in range(len(l.get_elements('合同发放状态', '选项'))):
            l.click('历分', '合同发放状态')
            l.clicks('合同发放状态', '选项', k)
            l.click('历分', '查询')

    def test_03_contractStatistics01(self):
        '''历统计--产品名称'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.clicks('合同管理', '历统计', 0)
        l.send_keys('历统计', '产品名称', "a")
        l.click('历统计', '查询')

    def test_03_contractStatistics02(self):
        '''历统计--产品大类'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.clicks('合同管理', '历统计', 0)
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('历统计', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('历统计', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('历统计', '查询')

    def test_03_contractStatistics03(self):
        '''历统计--产品状态'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.clicks('合同管理', '历统计', 0)
        for i in range(len(l.get_elements('产品状态', '选项'))):
            l.click('历统计', '产品状态')
            l.clicks('产品状态', '选项', i)
            l.click('历统计', '查询')

    def test_04_zongbufa01(self):
        '''总发--输入项'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.click('合同管理', '总发')
        l.send_keys('总发', '产品名称', "a")
        l.send_keys('总发', '分部收件人姓名', "a")
        l.send_keys('总发', '机构名称', "a")
        l.send_keys('总发', '快递单号', "a")
        l.click('总发', '查询')

    def test_04_zongbufa02(self):
        '''总发--募集类型'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.click('合同管理', '总发')
        for i in range(len(l.get_elements('募集类型', '选项'))):
            l.click('总发', '募集类型')
            l.clicks('募集类型', '选项', i)
            l.click('总发', '查询')

    def test_04_zongbufa03(self):
        '''总发--合同发放状态'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.click('合同管理', '总发')
        for i in range(len(l.get_elements('合同发放状态', '选项'))):
            l.click('总发', '合同发放状态')
            l.clicks('合同发放状态', '选项', i)
            l.click('总发', '查询')

    def test_05_zongbuguan01(self):
        '''总管-选项'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.clicks('合同管理', '总管',1)
        a = ["合同发放状态","合同分配情况","合同使用状态"]
        for b in a:
            for i in range(len(l.get_elements(b, '选项'))):
                l.click('总管', b)
                l.clicks(b, '选项', i)
                l.click('总管', '查询')


    def test_05_zongbuguan02(self):
        '''总管-输入项'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.clicks('合同管理', '总管', 1)
        l.send_keys('总管', '产品名称', "a")
        l.send_keys('总管', '认购起点', "a")
        l.send_keys('总管', '客户姓名', "a")
        l.send_keys('总管', '所在机构', "a")
        l.send_keys('总管', '原机构', "a")
        l.send_keys('总管', '财富顾问', "a")
        l.send_keys('总管', '顾问所属机构', "a")
        l.send_keys('总管', '合同编号', "a")
        l.click('总管', '查询')

    def test_06_contractIssueListDepartmentNew01(self):
        '''分签--输入项'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.click('合同管理', '分签')
        l.send_keys('分签', '产品名称', "a")
        l.send_keys('分签', '快递单号', "a")
        l.click('分签', '查询')

    def test_06_contractIssueListDepartmentNew02(self):
        '''分签--募集类型'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.click('合同管理', '分签')
        for i in range(len(l.get_elements('募集类型', '选项'))):
            l.click('分签', '募集类型')
            l.clicks('募集类型', '选项', i)
            l.click('分签', '查询')

    def test_06_contractIssueListDepartmentNew03(self):
        '''分签--合同发放状态'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.click('合同管理', '分签')
        for i in range(len(l.get_elements('合同发放状态', '选项'))):
            l.click('分签', '合同发放状态')
            l.clicks('合同发放状态', '选项', i)
            l.click('分签', '查询')

    def test_07_contractIssueListDepartmentUse(self):
        '''分用'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.clicks('合同管理', '分用', 2)

    def test_08_contractUseStatistics01(self):
        '''合同统计-产品名称--产品大类'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.click('合同管理', '合同统计')
        l.send_keys('合同统计', '产品名称', "a")
        for i in range(len(l.get_elements('产品大类', '选项'))):
            l.click('合同统计', '产品大类')
            l.clicks('产品大类', '选项', i)
            for j in range(len(l.get_elements('产品子类', '选项'))):
                l.click('合同统计', '产品子类')
                l.clicks('产品子类', '选项', j)
                l.click('合同统计', '查询')

    def test_08_contractUseStatistics02(self):
        '''合同统计--产品状态'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.click('合同管理', '合同统计')
        for i in range(len(l.get_elements('产品状态', '选项'))):
            l.click('合同统计', '产品状态')
            l.clicks('产品状态', '选项', i)
            l.click('合同统计', '查询')

    def test_09_contractTemplate(self):
        '''合同模板'''
        l = self.locator
        l.move_to('主页', '合同管理')
        l.click('合同管理', '合同模板')
        l.send_keys('合同模板', '模板名称', "a")
        for i in range(len(l.get_elements('状态', '选项'))):
            l.click('合同模板', '状态')
            l.clicks('状态', '选项', i)
            l.click('合同模板', '查询')

