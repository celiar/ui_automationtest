from pxframe.pxutil import *


class ProductOnline(TestBaseWeb):
    '''合同发放'''
    def test01_contract_distribute(self):
        l = self.locator
        try:
            self.driver.get(cbshost+"/contractDistribute/search")
            sleep(1)
            l.findby("linktext", "分发合同").click()
            sleep(1)
            l.findby("id", "productNameGive").send_keys(ProductName.wjb)
            l.findby("id", "autocompleter-2").click()
            sleep(1)
            l.findby("id", "applicantOrgNameGive").send_keys("测试组")
            l.findby("id", "autocompleter-1").click()
            sleep(1)
            js = "document.getElementById('grantTimeGive').removeAttribute('readOnly');"
            self.driver.execute_script(js)
            l.findby("xpath", "//input[@id='grantTimeGive']").send_keys(nowtime())
            sleep(1)
            l.findby("id", "grantNumberGive").send_keys("2")
            sleep(1)
            l.findby("id", "contractPreGive").send_keys("Test-HT")
            sleep(1)
            l.findby("id", "contractOrderStartGive").click()
            sleep(1)
            l.findby("id", "contractOrderEndGive").click()
            sleep(1)
            l.findby("id", "branchRecipientsNameGive").send_keys("肖冰玉")
            sleep(1)
            l.findby("id", "branchRecipientsMobileGive").send_keys("13120256784")
            sleep(1)
            l.findby("id", "branchRecipientsAddressGive").send_keys("北京市朝阳区合生汇")
            sleep(1)
            l.findby("id", "grantCourierFirmGive").send_keys("顺丰速运")
            sleep(1)
            l.findby("id", "grantCourierOrderNoGive").send_keys("SF1010101")
            sleep(1)
            l.findby("xpath", "//div[@class='sendBtnContain contractBtnContain contractBtnCustom']/button[1]").click()
            sleep(2)
            self.driver.get(cbshost+"/contractDistribute/search")
            sleep(1)
            l.findby("id", "productName").send_keys(ProductName.wjb)
            sleep(1)
            l.findby("linktext", "查询").click()
            sleep(1)
            status = l.findby("xpath", "//table[@class='myProductList_table']/tbody/tr[1]/td[9]").text
            sleep(1)
            if status == "总部已发放":
                print("【{}】总部分发合同成功！".format(ProductName.wjb))
            else:
                print("合同分发失败，请检查！")
        except:
            print("合同发放执行失败，请检查！")

    def test02_contract_sign(self):
        '''合同签收'''
        l = self.locator
        try:
            sleep(2)
            self.driver.get(cbshost+"/contractReceive/search")
            sleep(1)
            l.findby("id", "productName").send_keys(ProductName.wjb)
            sleep(1)
            l.findby("linktext", "查询").click()
            sleep(1)
            l.findby("linktext", "合同签收").click()
            sleep(1)
            js = "document.getElementById('branchSignReceiveTime').removeAttribute('readOnly');"
            self.driver.execute_script(js)
            l.findby("xpath", "//input[@id='branchSignReceiveTime']").send_keys(nowtime())
            sleep(1)
            l.findby("linktext", "确定").click()
            sleep(1)
            self.driver.get(cbshost+"/contractReceive/search")
            sleep(2)
            status = l.findby("xpath", "//table[@class='myProductList_table']/tbody/tr[1]/td[8]").text
            # print(status)
            if status == "分部已签收":
                print("【{}】分部签收合同成功！".format(ProductName.wjb))
            else:
                print("分部签收失败，请检查！")
        except:
            print("分部签收执行失败，请检查！")

    def test03_product_online(self):
        '''产品上线'''
        l = self.locator
        sleep(2)
        self.driver.get(cbshost+"/product/productList")
        sleep(1)
        for i in range(10):
            product_name = l.findsby("xpath", "//td[@class='name']/a")[i].text
            # print(product_name)
            if product_name == ProductName.wjb:
                status1 = l.findsby("xpath", "//td[@class='name']/../td[7]/em")[i].text
                # print(status1)
                if status1 == "预热中":
                    l.findsby("xpath", "//td[@class='newCZ']/a[2]")[i].click()
                    sleep(1)
                    js = "document.getElementById('OnlineTime').removeAttribute('readOnly');"
                    self.driver.execute_script(js)
                    l.findby("xpath", "//input[@id='OnlineTime']").send_keys(nowtime())
                    sleep(1)
                    l.findby("linktext", "确定").click()
                    sleep(2)
                    break
                else:
                    print("【{}】已上线，状态为募集中！".format(ProductName.wjb))
                    break
        sleep(1)
        l.findby("xpath", "//input[@name='name']").send_keys(ProductName.wjb)
        sleep(1)
        l.findby("linktext", "查询").click()
        sleep(1)
        status2 = l.findby("xpath", "/html/body/div[6]/div[5]/div[2]/table/tbody/tr/td[7]/em").text
        # print(status2)
        if status2 == "募集中":
            print("【{}】上线成功，状态为{}".format(ProductName.wjb, status2))
        else:
            print("【{}】上线失败，请检查！".format(ProductName.wjb))