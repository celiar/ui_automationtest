from pxframe.pxutil import *


class ContractSendbackSign(TestBaseWeb):
    '''分部合同寄回'''
    def test01_contract_sendback(self):
        l = self.locator
        try:
            sleep(1)
            self.driver.get(cbshost+"/contractUse/search")
            sleep(1)
            l.findby("id", "productName").send_keys(ProductName.wjb)
            sleep(1)
            l.findby("xpath", "//input[@id='grantState']/../p").click()
            l.findby("linktext", "分部已签收").click()
            sleep(1)
            l.findby("linktext", "查询").click()
            sleep(1)
            l.findby("id", "_all_checked").click()
            l.findby("linktext", "合同寄回").click()
            sleep(1)
            js = "document.getElementById('branchMailTime').removeAttribute('readOnly');"
            self.driver.execute_script(js)
            l.findby("xpath", "//input[@id='branchMailTime']").send_keys(nowtime())
            sleep(1)
            l.findby("id", "trunkRecipientsName").send_keys("总部运营")
            sleep(1)
            l.findby("id", "trunkRecipientsMobile").send_keys("13100000001")
            sleep(1)
            l.findby("id", "trunkRecipientsAddress").send_keys("北京市朝阳区合生汇5层")
            sleep(1)
            l.findby("id", "branchMailCourierFirm").send_keys("韵达快递")
            sleep(1)
            l.findby("id", "branchMailOrderNo").send_keys("YD0000001")
            sleep(1)
            l.findby("xpath", "//button[@class='confirmBtnSignIn']").click()
            sleep(3)
            self.driver.get(cbshost+"/contractManage/search")
            sleep(2)
            l.findby("id", "productName").send_keys(ProductName.wjb)
            sleep(1)
            l.findby("xpath", "//div[@class='selectBox']/p").click()
            sleep(1)
            l.findby("linktext", "分部已寄回").click()
            sleep(1)
            l.findby("linktext", "查询").click()
            sleep(1)
            pname = l.findby("xpath", "//table[@class='myProductList_table']/tbody/tr[1]/td[5]").text
            # print(pname)
            # 应该与已签约订单的产品名称做比对
            if pname == ProductName.wjb:
                print("【{}】分部合同寄回成功！".format(ProductName.wjb))
            else:
                self.assertTrue(False, "【{}】分部寄回失败，请检查！".format(ProductName.wjb))
        except:
            print("合同寄回执行失败，请检查！")

    def test02_contract_sign(self):
        '''总部合同签收'''
        l = self.locator
        try:
            sleep(1)
            l.findby("id", "checkboxManage").click()
            sleep(1)
            l.findby("linktext", "合同签收").click()
            sleep(1)
            js = "document.getElementById('contractReceive').removeAttribute('readOnly');"
            self.driver.execute_script(js)
            l.findby("xpath", "//input[@id='contractReceive']").send_keys(nowtime())
            sleep(1)
            l.findby("class", "confirmBtnSignIn").click()
            sleep(1)
            self.driver.get(cbshost+"/contractManage/search")
            sleep(2)
            l.findby("id", "productName").send_keys(ProductName.wjb)
            sleep(1)
            l.findby("linktext", "查询").click()
            sleep(2)
            status = l.findby("xpath", "//table[@class='myProductList_table']/tbody/tr[1]/td[15]").text
            # print(status)
            if status == "总部已签收":
                print("【{}】总部签收合同成功！".format(ProductName.wjb))
            else:
                self.assertTrue(False, "【{}】总部签收失败，请检查！".format(ProductName.wjb))
        except:
            print("总部签收合同执行失败，请检查！")