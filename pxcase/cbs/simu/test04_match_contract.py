from pxframe.pxutil import *


class ContractMatch(TestBaseWeb):
    '''预约单分配合同'''
    def test01(self):
        '''分配合同'''
        l = self.locator
        with open('jflogin_res.json', 'r') as rf:
            cookies = json.loads(rf.read())
        usertoken = cookies['token']
        userId = cookies['result']['userId']
        # print(usertoken,userId)

        # 获取产品id
        headers2 = {'token': usertoken,
                    'clientId': userId,
                    'Content-Type': 'application/json'
                    }
        def mypreappoint():
            try:
                url5 = jfhost+'/jfapp/user/new/mypreappoint '
                data5 = {"startPage": "1", "pageSize": "10", "productType": "PXZCGL17"}
                res5 = requests.post(url=url5, json=data5, headers=headers2).json()
            except:
                self.assertTrue(False, '模块异常')
            a = res5['result']['data']
            return a
        # 获取待受理订单，若无待受理则报错，需首先发起预约流程
        k = 0
        for i in range(len(mypreappoint())):

            if mypreappoint()[i]['stateName'] == '待受理':
                orderId = (mypreappoint()[i]['orderId'])
                productName = (mypreappoint()[i]['productName'])
                break
            else:
                k+=1
                while k == len(mypreappoint()):
                    self.assertTrue(False, '无待受理的订单，预约失败')
                continue
        sleep(3)
        self.driver.get(cbshost+"/sell/booking/bookingList")
        sleep(1)
        l.findby('name','orderNo').send_keys(orderId)
        sleep(1)
        l.findby('linktext','查询').click()
        sleep(1)
        orderId1 = l.findby('xpath', '//div[@class="declarationListContain"]//td[2]').text
        sleep(1)
        print(orderId1)
        if orderId1==orderId:
            # 增加分部合同未签约剩余数目
            try:
                l.findby('linktext','分配合同').click()
                sleep(2)
                l.findby('id','pForAssign').click()
            except:
                # 添加分配合同流程
                # self.assertTrue(False,"没有可以分配的合同")
                self.driver.get(cbshost+"/contractDistribute/search")
                sleep(1)
                l.findby("linktext", "分发合同").click()
                l.findby("id", "productNameGive").send_keys(productName)
                l.findby("id", "autocompleter-2").click()
                l.findby("id", "applicantOrgNameGive").send_keys("测试组")
                l.findby("id", "autocompleter-1").click()
                js = "document.getElementById('grantTimeGive').removeAttribute('readOnly');"
                self.driver.execute_script(js)
                l.findby("xpath", "//input[@id='grantTimeGive']").send_keys(nowtime())
                l.findby("id", "grantNumberGive").send_keys("2")
                l.findby("id", "contractPreGive").send_keys("Test-HT")
                l.findby("id", "contractOrderStartGive").click()
                l.findby("id", "contractOrderEndGive").click()
                l.findby("id", "branchRecipientsNameGive").send_keys("肖冰玉")
                l.findby("id", "branchRecipientsMobileGive").send_keys("13120256784")
                l.findby("id", "branchRecipientsAddressGive").send_keys("北京市朝阳区合生汇")
                l.findby("id", "grantCourierFirmGive").send_keys("顺丰速运")
                l.findby("id", "grantCourierOrderNoGive").send_keys("SF1010101")
                l.findby("xpath", "//div[@class='sendBtnContain contractBtnContain contractBtnCustom']/button[1]").click()
                pname2 = l.findby("xpath", "//table[@class='myProductList_table']/tbody/tr[1]/td[2]").text
                sleep(1)
                if productName == pname2:
                    print("合同分发成功！")
                else:
                    self.assertTrue(False,"合同分发失败，请检查！")
                time.sleep(2)
                self.driver.get(cbshost+"/contractReceive/search")
                sleep(1)
                l.findby("linktext", "合同签收").click()
                sleep(1)
                js = "document.getElementById('branchSignReceiveTime').removeAttribute('readOnly');"
                self.driver.execute_script(js)
                l.findby("xpath", "//input[@id='branchSignReceiveTime']").send_keys(nowtime())
                sleep(1)
                l.findby("linktext", "确定").click()
                sleep(3)
                status2 = l.findby("xpath", "//table[@class='myProductList_table']/tbody/tr[1]/td[8]").text
                print(status2)
                if status2 == "分部已签收":
                    print("分部签收成功！")
                else:
                    self.assertTrue(False,"分部签收失败，请检查！")
                self.driver.get(cbshost+"/sell/booking/bookingList")
                sleep(1)
                l.findby('name', 'orderNo').send_keys(orderId)
                sleep(1)
                l.findby('linktext', '查询').click()
                sleep(1)
                l.findby('linktext', '分配合同').click()
                sleep(3)
                l.findby('id', 'pForAssign').click()
            l.findby('xpath','//ul[@id="contractToAssign"]/li[2]/a').click()
            sleep(1)
            l.findsby('class','trueRaise')[1].click()
            sleep(2)
            try:
                # 交易状态，合同编号
                status3 = l.findby('xpath', '//div[@class="declarationListContain"]//td[22]').text
                cnum3 = l.findby('xpath', '//div[@class="declarationListContain"]//td[24]').text
                self.assertEqual(status3,"待签约","{}分配合同失败，合同编号是{}".format(orderId1,cnum3))
                print("{}分配合同成功，合同编号是{}".format(orderId1,cnum3))
            except:
                self.assertTrue(False,"分配合同后列表为空，或不存在交易状态列")
        else:
            self.assertTrue(False,"单号不一致")

