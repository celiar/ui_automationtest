from pxframe.pxutil import *


class AddProductWenjinbao(TestBaseWeb):
    '''cbs产品管理-新增稳金宝产品'''
    def test01_basic_info(self):
        '''基本信息'''
        l = self.locator

        if l.findby("class", "hiname"):
            print("登录成功")
        else:
            self.assertTrue(False, "登录失败,请检查！")
        sleep(1)
        self.driver.get(cbshost + "/product/productList")
        l.send_keys('产品列表', '产品名称输入', ProductName.wjb)
        l.click('产品列表', '查询')
        sleep(1)
        try:
            # 验证当日是否已创建产品
            pname = l.findsby("xpath", "//td[@class='name']/a")[0].text
            status = l.findsby("xpath", "//td[@class='name']/../td[7]/em")[0].text
            self.assertIsNot(pname, ProductName.wjb, '{}已存在，状态为{}'.format(ProductName, status))
        except:
            # 测试产品-非微动力-产品来源-管理人
            self.driver.get(cbshost + "/product/myProduct")
            l.findby("linktext", "新增产品").click()
            l.findsby("id", "isTest")[0].click()
            l.findsby("id", "isWdl")[1].click()
            sleep(1)
            l.findby("xpath", "//input[@id='source']/../p").click()
            l.findby("linktext", "自研").click()
            sleep(1)
            l.findby("id", "manager").send_keys("测试")
            sleep(1)

            # 大类-子类-业绩-组织
            l.findbyx("parentProductTypeId").click()
            l.findby("linktext", "稳金宝").click()
            sleep(1)
            l.findbyx("productTypeId").click()
            l.findby("linktext", "智信").click()
            sleep(1)
            l.findbyx("achievementType").click()
            l.findby("linktext", "保理产品").click()
            sleep(1)
            l.findbyx("raiseType").click()
            l.findby("linktext", "定向募集(明星产品)").click()
            sleep(1)
            l.findbyx("attribute").click()
            l.findby("linktext", "有限合伙基金").click()
            sleep(1)

            # 产品名称-币种-封闭期-认购起点-递增金额
            l.findby("id", "name").send_keys(ProductName.wjb)
            sleep(1)
            l.findbyx("currency").click()
            l.findby("linktext", "人民币").click()
            sleep(1)
            # 如下两项为非必填项，期限-备注
            # l.findby("id","periodYear").send_keys("5")
            # l.findby("id","periodRemark").send_keys("备注a")
            l.findby("id", "closedPeriod").send_keys("1")
            sleep(1)
            l.findby("id", "minPurchaseAmountWan").send_keys("3")
            sleep(1)
            l.findby("id", "increaseAmount").send_keys("5000")
            sleep(1)

            #是否有产品规模--金额规模--金额警戒线--人数上限--人数警戒线--风险等级--投向分类--特点
            l.findbyx("isScaled").click()
            l.findby("linktext", "否").click()
            sleep(1)
            # l.findby("id", "scaleAmountWan").send_keys("1000")
            # sleep(1)
            # l.findby("id", "scaleAlarmAmountWan").send_keys("900")
            # sleep(1)
            l.findby("id", "scalePersion").send_keys("100")
            sleep(1)
            l.findby("id", "scaleAlarmPersion").send_keys("1")
            sleep(1)
            l.findsby("name", "riskLevel")[0].click()
            l.findby("id", "investCategory").send_keys("投向二")
            sleep(1)
            l.findby("id", "hightlights").send_keys("流动性好")
            l.findby("id", "hightlights2").send_keys("双备案")
            l.findby("id", "hightlights3").send_keys("债权真实")
            sleep(1)

            # 郎福-普信-返佣-亮点-风险提示
            l.findby("id", "lfFoldRatio").send_keys("1")
            sleep(1)
            l.findby("id", "pxFoldRatio").send_keys("1.2")
            sleep(1)
            l.findby("name", "rakebackList[0].positionName").send_keys("测试经理")
            l.findby("name", "rakebackList[0].commissionProportion").send_keys("5")
            sleep(1)
            reviews = '''流动性好：应收账款账期均不超过1.5年，资金使用率高，流动性强；
            双备案：已通过中国证券基金业协会备案，已通过中登网登记， 无备案风险；
            低折扣受让底层资产：底层资产价值远超基金规模，价值充分，安全边际较高；
            债权真实、回款明确：以真实发生的资产收益权为底层，债权真实可靠；
            资金监管：基金全程银行托管，与管理人基本户防火墙隔离；'''
            rlist = reviews.split("；")
            l.findby("id", "productReview").send_keys(rlist[0])
            l.findby("id", "productReview2").send_keys(rlist[1])
            l.findby("id", "productReview3").send_keys(rlist[2])
            l.findby("id", "productReview4").send_keys(rlist[3])
            l.findby("id", "productReview5").send_keys(rlist[4])
            sleep(1)
            rp = '''(一) 特殊风险揭示 1、 基金合同与中国基金业协会合同指引不一致所涉风险 
            2、 私募基金委托募集所涉风险 
            3、 私募基金未在中国证券投资基金业协会履行备案手续或备案不通过所涉风险 
            4、 私募基金外包事项（如有）所涉风险 
            5、 产品架构、底层标的、关联交易、资金流动性所涉风险 
            (二) 一般风险揭示 1、 市场风险 
            2、 管理风险 
            3、 资金损失风险 
            4、 基金运营风险 
            5、 募集失败风险'''
            l.findby("id", "riskPrompt").send_keys(rp)
            sleep(1)
            l.findsby("css", "button")[0].click()
            if l.findby("id", "profitType"):
                print("新增产品--基本信息执行成功！")
            else:
                self.assertTrue(False, "产品已存在，或信息有误，请检查！")

    def test02_profit(self):
        '''收益类型'''
        l = self.locator
        if l.findby("id", "profitType"):
            l.findbyx("profitType").click()
            l.findby("linktext", "固定收益").click()
            sleep(1)
            l.findbyx("payInterestWay").click()
            l.findby("linktext", "自然半年度").click()
            sleep(1)
            l.findby("xpath", "//table[@id='tab']/tbody/tr[1]/td[2]/input[2]").send_keys("50")
            l.findby("xpath", "//table[@id='tab']/tbody/tr[1]/td[3]/input").send_keys("1")
            sleep(1)
            l.findby("xpath", "//img[@src='/static/images/addicon.png']").click()
            l.findby("xpath", "//table[@id='tab']/tbody/tr[2]/td[3]/input").send_keys("2")
            sleep(1)
            # l.findbyx("profitType").click()
            # l.findby("linktext", "浮动收益").click()
            # sleep(1)
            # l.findbyx("payInterestWay").click()
            # l.findby("linktext", "自然季度").click()
            # sleep(1)
            try:
                l.findsby("css", "button")[1].click()
                if l.findby("id", "raiseAccountName"):
                    print("新增产品--收益模式执行成功！")
            except:
                print("新增产品--收益模式执行失败！")
                self.assertTrue(False, "产品已存在，请检查！")
        else:
            print("未进入收益模式页面！")

    def test03_account(self):
        '''募集账号'''
        l = self.locator
        try:
            # 获取募集账号页面tag
            tag1 = l.findby('xpath','//input[@id="raiseAccountName"]/../span').text
        except:
            self.assertTrue(False, "未进入收益模式页面,流程异常或产品已添加。")
        if tag1=='募集账户户名':
            l.findby("id", "raiseAccountName").send_keys("普信资产私募基金募集专用账户")
            sleep(1)
            l.findby("id", "raiseAccountBank").send_keys("中国银行北京市万达支行")
            sleep(1)
            l.findby("id", "raiseAccountNo").send_keys(account_random())
            sleep(1)
            try:
                # alert索引，确认是0，拒绝是1
                l.findsby("css", "button")[1].click()
                sleep(1)
                l.findsby("css", "button")[1].click()
                sleep(1)
                if l.findby("class", "btn_width"):
                    print("新增产品--募集账号&产品附件执行成功！")
                else:
                    self.assertTrue(False, "产品已存在，请检查")
            except:
                print("新增产品--募集账号&产品附件执行失败！")
        else:
            print("进入页面非募集账号页面！")

    def test04_electronic_contract(self):
        '''设置电子合同'''
        l = self.locator
        if l.findby("class", "btn_width"):
            l.findby("xpath", "//div[@class='stepsContain']/button[2]").click()
            sleep(1)
            if ProductName.wjb == l.findsby("xpath", "//td[@class='name']/a")[0].text:
                print("新增产品--设置电子合同执行成功！")
            else:
                print("新增产品--设置电子合同执行失败！")
        else:
            print("未进入设置电子合同页面！")

    def test05_submit_audit(self):
        '''提交审核'''
        l = self.locator
        self.driver.get(cbshost + "/product/myProduct")
        sleep(2)
        l.send_keys('产品列表', '产品名称输入', ProductName.wjb)
        l.click('产品列表', '查询')
        try:
            pname = l.findsby("xpath", "//td[@class='name']/a")[0].text
            status1 = l.findsby("xpath", "//td[@class='name']/../td[13]")[0].text
        except:
            self.assertTrue(False,'依赖流程异常，产品列表不存在{}'.format(ProductName.wjb))
        if pname == ProductName.wjb and status1=="待审核":
            l.findby("linktext", "提交审核").click()
            sleep(1)
            l.findby("class", "confirmBtnSignIn").click()
            try:
                status = l.findsby("xpath", "//td[@class='name']/../td[13]")[0].text
                # print(status)
                if status == "待审核":
                    print("新增产品【{}】提交审核执行成功，状态为{}".format(pname, status))
                else:
                    self.assertTrue(False, "产品已存在，请检查！")
            except:
                print("新增产品提交审核执行失败！")
        else:
            print("无需进行提交审核！产品审核状态为{}".format(status1))

    def test06_audit_pass(self):
        '''审核通过'''
        l = self.locator
        self.driver.get(cbshost+"/product/audit/productAuditList")
        sleep(2)
        l.send_keys('产品审核', '产品名称输入', ProductName.wjb)
        l.click('产品审核', '查询')
        try:
            pname = l.findsby("xpath", "//td[@class='red']")[0].text
            status1 = l.findsby("xpath", "//td[@class='red']/../td[8]")[0].text
        except:
            self.assertTrue(False,"产品审核列表不存在{}".format(ProductName.wjb))

        if pname == ProductName.wjb and status1 == "待上线":
            l.findsby("class", "stateChoose")[0].click()
            sleep(1)
            # 是否审核：确定-确定
            self.driver.switch_to_alert().accept()
            sleep(1)
            self.driver.switch_to_alert().accept()
            sleep()
            try:
                # 第十九列：操作
                status2 = l.findsby("xpath", "//td[@class='red']/../td[8]")[0].text
                if status2 == "预热中":
                    print("【{}】审核通过，状态为预热中".format(ProductName.wjb))
            except:
                print("【{}】审核未通过".format(ProductName.wjb))
                self.assertTrue(False, "产品已存在，请检查！")

        elif pname == ProductName.wjb and status1 == "预热中":
            print("【{}】已存在，状态为预热中".format(ProductName.wjb))
        else:
            print("产品审核列表不存在{}".format(ProductName.wjb))
