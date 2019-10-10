from pxframe.pxutil import *


class IcManagement(TestBaseWeb):
    '''IC管理'''

    def test_icmanage_01(self):
        '''IC人员管理--IC姓名'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', 'IC人员管理')
        l.send_keys("IC人员管理","IC姓名","a")
        l.click("IC人员管理", "查询")

    def test_icmanage_02(self):
        '''IC人员管理--常驻办公地点'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', 'IC人员管理')
        l.send_keys("IC人员管理", "常驻办公地点", "a")
        l.click("IC人员管理", "查询")

    def test_icmanage_03(self):
        '''IC人员管理--手机号'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', 'IC人员管理')
        l.send_keys("IC人员管理", "手机号", "a")
        l.click("IC人员管理", "查询")
        

    def test_icmanage_04(self):
        '''IC人员管理--上架状态'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', 'IC人员管理')
        l.click("IC人员管理","上架状态")
        l.clicks("上架状态", "选项", 1)
        l.click("IC人员管理", "查询")
        l.move("下")
        l.click("IC人员管理", "上架状态")
        l.clicks("上架状态", "选项", 2)
        l.click("IC人员管理", "查询")
        l.move("下")

    # def test_icmanage_05(self):
    #     '''IC人员管理--日期'''
    #     l = self.locator
    #     l.move_to('主页', 'IC管理')
    #     l.click('IC管理', 'IC人员管理')
    #     l.click("IC人员管理","上架状态")
    #     l.clicks("上架状态","选项",2)
    #

    def test_icmanage_06(self):
        '''IC人员管理--新增IC'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', 'IC人员管理')
        l.click("IC人员管理","新增IC")
        l.click("IC人员管理", "查询")

    # def test_icmanage_07(self):
    #     '''IC人员管理--导出'''
    #     l = self.locator
    #     l.move_to('主页', 'IC管理')
    #     l.click('IC管理', 'IC人员管理')
    #     l.click("IC人员管理","上架状态")
    #     l.clicks("上架状态","选项",2)
    #

    # def test_icmanage_08(self):
    #     '''IC人员管理--上架--下架--置顶'''
    #     l = self.locator
    #     l.move_to('主页', 'IC管理')
    #     l.click('IC管理', 'IC人员管理')
    #     l.click("IC人员管理","上架状态")
    #     l.clicks("上架状态","选项",2)

    def test_icappointment01(self):
        '''IC预约-预约人'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', 'IC预约')
        l.send_keys('IC预约', '预约人',"a")
        l.click('IC预约', '查询')

    def test_icappointment02(self):
        '''IC预约-IC姓名'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', 'IC预约')
        l.send_keys('IC预约', 'IC姓名',"a")
        l.click('IC预约', '查询')

    def test_icappointment03(self):
        '''IC预约-宣讲城市'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', 'IC预约')
        l.send_keys('IC预约', '宣讲城市',"a")
        l.click('IC预约', '查询')

    def test_icappointment04(self):
        '''IC预约-IC受理状态'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', 'IC预约')
        for i in range(len(l.get_elements('IC受理状态', '选项'))):
            l.click('IC预约', 'IC受理状态')
            l.clicks('IC受理状态', '选项', i)
            l.click('IC预约', '查询')

    def test_icaccompanying01(self):
        '''IC陪访--IC姓名'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', 'IC陪访')
        l.send_keys('IC陪访', 'IC姓名', "a")
        l.click('IC陪访', '查询')

    def test_icaccompanying02(self):
        '''IC陪访--所属顾问'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', 'IC陪访')
        l.send_keys('IC陪访', '所属顾问', "a")
        l.click('IC陪访', '查询')

    def test_icaccompanying03(self):
        '''IC陪访--顾问所属机构'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', 'IC陪访')
        l.send_keys('IC陪访', '顾问所属机构', "a")
        l.click('IC陪访', '查询')

    def test_icaccompanying04(self):
        '''IC陪访--是否关单'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', 'IC陪访')
        for i in range(len(l.get_elements('是否关单', '选项'))):
            l.click('IC陪访', '是否关单')
            l.clicks('是否关单', '选项', i)
            l.click('IC陪访', '查询')

    def test_ictraining01(self):
        '''对内培训--IC姓名'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', '对内培训')
        l.send_keys('对内培训', 'IC姓名', "a")
        l.click('对内培训', '查询')

    def test_ictraining02(self):
        '''对内培训--手机号'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', '对内培训')
        l.send_keys('对内培训', '手机号', "a")
        l.click('对内培训', '查询')

    def test_ictraining03(self):
        '''对内培训--培训主题'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', '对内培训')
        l.send_keys('对内培训', '培训主题', "a")
        l.click('对内培训', '查询')

    def test_icforum01(self):
        '''论坛讲座--IC姓名'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', '论坛讲座')
        l.send_keys('论坛讲座', 'IC姓名', "a")
        l.click('论坛讲座', '查询')

    def test_icforum02(self):
        '''论坛讲座--手机号'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', '论坛讲座')
        l.send_keys('论坛讲座', '手机号', "a")
        l.click('论坛讲座', '查询')

    def test_icforum03(self):
        '''论坛讲座--活动主题'''
        l = self.locator
        l.move_to('主页', 'IC管理')
        l.click('IC管理', '论坛讲座')
        l.send_keys('论坛讲座', '活动主题', "a")
        l.click('论坛讲座', '查询')


