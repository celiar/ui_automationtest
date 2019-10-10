from pxframe.pxutil import *


class Declarationwjb(TestBase):
    '''首页-报单管理'''
    def test01(self):
        '''验证创新业务--新增报单-待审核'''
        poco(text="首页").click()
        poco("com.puxin.accountant:id/rl_order").click()
        poco(text="待签约").click()
        try:
            pname = poco("com.puxin.accountant:id/tv_name").get_text()
            orderId = poco("com.puxin.accountant:id/tv_order_num").get_text()
        except:
            back()
            self.assertTrue(False,"待签约列表为空")
        back()
        poco("com.puxin.accountant:id/tv_declaration").click()
        poco(text="创新业务").click()
        poco("com.puxin.accountant:id/iv_share").click()
        try:
            order1 = poco("com.puxin.accountant:id/tv_order_num").get_text()
        except:
            back(3)
            self.assertTrue(False,"我要报单页面不存在单据，或网络异常")
        poco("com.puxin.accountant:id/tv_detail").click()
        swipe_down("android.widget.ScrollView")
        # 客户身份证人像面
        poco("com.puxin.accountant:id/iv_cardfront").click()
        try:
            poco("com.puxin.accountant:id/btn_back").click()
        except:
            poco("com.puxin.accountant:id/dialog_item_bt")[1].click()
            poco("com.puxin.accountant:id/iv_thumb")[0].click()
        # 客户身份证国徽面
        poco("com.puxin.accountant:id/iv_cardback").click()
        try:
            poco("com.puxin.accountant:id/btn_back").click()
        except:
            poco("com.puxin.accountant:id/dialog_item_bt")[1].click()
            poco("com.puxin.accountant:id/iv_thumb")[0].click()
        swipe_down("android.widget.ScrollView")
        sleep(3)
        # 打款凭证
        poco("com.puxin.accountant:id/iv_trade_paper").click()
        try:
            poco("com.puxin.accountant:id/btn_back").click()
        except:
            poco("com.puxin.accountant:id/dialog_item_bt")[1].click()
            poco("com.puxin.accountant:id/iv_thumb")[0].click()
        # 合同签字页
        poco("com.puxin.accountant:id/iv_img").click()
        try:
            poco("com.puxin.accountant:id/btn_back").click()
        except:
            poco("com.puxin.accountant:id/dialog_item_bt")[1].click()
            poco("com.puxin.accountant:id/iv_thumb")[0].click()
            poco("com.puxin.accountant:id/btn_ok").click()
        # 提交报单
        poco("com.puxin.accountant:id/toolbar_menu_title").click()
        # 因存在网络延迟，需加等待
        sleep(5)
        if poco("com.puxin.accountant:id/toolbar_title").get_text() == "我要报单":
            back(3)
            print("输入信息有误请核对脚本或页面属性值，或网络连接有问题")
        elif poco("com.puxin.accountant:id/iv_error").exists() and poco(
                "com.puxin.accountant:id/toolbar_title").get_text() == "报单管理":
            back(2)
            print("网络连接有问题")
        else:
            try:
                order2 = poco("com.puxin.accountant:id/tv_order_num").get_text()
                back(2)
            except:
                self.assertTrue(False,"{}报单失败".format(orderId))
            self.assertEqual(order1, order2, "提交报单{}失败".format(order1))
            print("提交报单{}成功".format(order2))

    def test02(self):
        '''验证创新业务--审核报单--通过审核'''
        l = self.locator
        poco(text="首页").click()
        poco("com.puxin.accountant:id/tv_declaration").click()
        poco(text="创新业务").click()
        poco(text="待审核").click()
        sleep(5)
        try:
            pname = poco("com.puxin.accountant:id/tv_name").get_text()
            orderId = poco("com.puxin.accountant:id/tv_order_num").get_text()
            print(pname,orderId)
        except:
            back(2)
            self.assertTrue(False, "待审核列表为空")
        # try:
        #     cbslogin()
        # except:
        #     back(2)
        #     self.assertTrue(False, "由于目标计算机积极拒绝，无法连接")
        self.driver.get(cbshost+"/sell/declaration/declarationList")
        sleep(2)
        l.findby('name','orderNo').send_keys(orderId)
        sleep(1)
        try:
            # 单号、审核状态
            orderId1 = l.findby("xpath", "//div[@class='declarationListContain']//td[2]").text
            status1 = l.findby("xpath", "//div[@class='declarationListContain']//td[14]").text
        except:
            back(2)
            self.assertTrue(False, "报单列表不存在单号{}".format(orderId))
        if orderId1 == orderId and status1== "待审核":
            l.findsby("class","stateChoose")[0].click()
            sleep(1)
            self.driver.execute_script("window.scrollTo(0,1000)")
            sleep(1)
            l.findby("id","auditInstruction").send_keys("通过")
            sleep(1)
            l.findby("linktext", "通过").click()
            sleep(1)
            self.driver.get(cbshost+"/sell/declaration/declarationList")
            sleep(1)
            l.findby('name', 'orderNo').send_keys(orderId)
            sleep(1)
            l.findby('linktext', '查询').click()
            sleep(1)
            try:
                orderId2 = l.findby("xpath", "//div[@class='declarationListContain']//td[2]").text
                status2 = l.findby("xpath", "//div[@class='declarationListContain']//td[14]").text
            except:
                back(2)
                self.assertTrue(False, "报单列表不存在单号{}".format(orderId))
            self.assertEqual(status2,'审核通过','单号{}的状态为{}'.format(orderId,status2))
            print('{}审核通过'.format(orderId))
            poco(text="审核通过").click()
            try:
                orderId3 = poco("com.puxin.accountant:id/tv_order_num").get_text()
                cname3 = poco("com.puxin.accountant:id/tv_order_customer").get_text()
                status3 = poco("com.puxin.accountant:id/tv_lable").get_text()
                back(2)
                self.assertEqual(orderId3, orderId1, "客户{}的{}未审核通过，状态为{}".format(cname3, orderId, status2))
                print("{}审核成功".format(orderId1))
            except:
                back(2)
                print("网络异常，或{}审核未通过".format(orderId))
        else:
            back(2)
            self.assertTrue(False,'报单列表单号{}的审核状态为{}'.format(orderId1,status1))

    def test03(self):
        '''cbs到账列表--导入到账列表匹配'''
        l = self.locator
        # 预约管理--待签约--获取单号
        poco(text="首页").click()
        poco("com.puxin.accountant:id/rl_order").click()
        poco(text="待签约").click()
        try:
            pname = poco("com.puxin.accountant:id/tv_name").get_text()
            orderId = poco("com.puxin.accountant:id/tv_order_num").get_text()
            print(pname, orderId)
        except:
            back()
            self.assertTrue(False, "待签约列表为空")
        # cbslogin()
        self.driver.get(cbshost+'/sell/declaration/declarationList')
        sleep(1)
        l.findby('name', 'orderNo').send_keys(orderId)
        sleep(1)
        l.findby('linktext', '查询').click()
        sleep(2)
        try:
            # 客户姓名、认购金额
            cname2 = l.findby("xpath", "//div[@class='declarationListContain']//td[3]").text
            value2 = l.findby("xpath", "//div[@class='declarationListContain']//td[8]").text
            l.findby('linktext','详情').click()
            sleep(1)
        except:
            back()
            self.assertTrue(False, "报单列表不存在单号{}".format(orderId))
        # 银行卡号
        bnum2 = l.findby("xpath", "//div[@class='refundTheAudit_main declarationTheAuditContain']/table[4]//tr[2]/td[1]").text
        sleep(1)
        self.driver.get(cbshost+'/product/productList')
        sleep(1)
        l.findby('name', 'name').send_keys(pname)
        sleep(1)
        l.findby('linktext', '查询').click()
        sleep(1)
        l.findby('class', 'name').click()
        sleep(1)
        # 募集账户
        refund2 = l.findby('xpath', '//*[text()="募集账户账号"]/../../tr[2]/td[3]').text
        sleep(1)
        snum2 = 'WYX' + str(int(time.time()))
        sleep(2)
        print(snum2, value2, bnum2, cname2, refund2)
        # 写入匹配模板
        rb = xlrd.open_workbook("./pxcase/cbs/到账导入模板003.xls")
        wb = copy(rb)
        sheet = wb.get_sheet(0)
        sheet.write(1, 0, snum2)
        sheet.write(1, 7, value2)
        sheet.write(1, 10, bnum2)
        sheet.write(1, 11, cname2)
        sheet.write(1, 1, refund2)
        wb.save("./pxcase/cbs/到账导入模板003.xls")

        self.driver.get(cbshost+'/wjb/searchAccountList')
        sleep(1)
        l.findby('class', 'ite_import').click()
        sleep(1)
        self.driver.execute_script('$("#accountfile").removeAttr("readonly")')
        p_dir = os.path.dirname(os.path.dirname(__file__))
        l.findby('id', 'accountfile').send_keys(p_dir + '/到账导入模板003.xls')
        l.findby('class', 'confirmBtn').click()
        # 获取excel流水号，匹配cbs列表
        rb2 = xlrd.open_workbook("./pxcase/cbs/到账导入模板003.xls")
        x2 = rb2.sheet_by_index(0)
        a = x2.cell_value(1,0)
        try:
            l.findby('name','matchOrderNo').send_keys(orderId)
            sleep(1)
            l.findby('linktext','查询').click()
            sleep(1)
            # 获取匹配成功的单号和状态
            status2 = l.findby('xpath','//tr[@class="tr_checked"]/td[4]').text
            orderId2 = l.findby('xpath','//tr[@class="tr_checked"]/td[5]').text
        except:
            back()
            self.assertTrue(False,"查询{}列表为空，未匹配成功")

        if orderId==orderId2 and status2=='匹配成功':
            poco(text='已签约').click()
            sleep(5)
            try:
                pname3 = poco("com.puxin.accountant:id/tv_name").get_text()
                orderId3 = poco("com.puxin.accountant:id/tv_order_num").get_text()
                print(pname3, orderId3)
            except:
                back()
                self.assertTrue(False, "已签约列表为空")
            back()
            self.assertEqual(orderId3,orderId,'单号不一致，预约匹配失败或单据是其他数据')
            print(orderId+"匹配成功，状态为已签约")
        else:
            back()
            self.assertTrue(False,'{}匹配状态为{}'.format(orderId2,status2))