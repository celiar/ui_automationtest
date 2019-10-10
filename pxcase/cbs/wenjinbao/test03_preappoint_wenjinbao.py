from pxframe.pxutil import *


class PreappointWjb(TestBase):
    '''金服客户预约'''
    def test01(self):
        '''app预约产品'''
        with open('jflogin_res.json', 'r') as rf:
            cookies = json.loads(rf.read())
        usertoken = cookies['token']
        userId = cookies['result']['userId']
        # 获取产品id
        url2 = jfhost+"/jfapp/innovate/productinnovatelist "
        headers2 = {'token': usertoken,
                    'clientId': userId,
                    'Content-Type': 'application/json'
                    }
        # PXZCGL18是稳金宝--智信,选取第一个可预约的产品（可预约金额大于最低起购额）
        data2 = {"startPage": "1", "pageSize": "100", "productType": "PXZCGL18"}
        res2 = requests.post(url=url2, json=data2, headers=headers2,verify=False).json()
        k = 0
        for i in range(len(res2["result"]["data"])):
            pdata = res2["result"]["data"][i]
            # print(pdata)
            if pdata['pre'] == False and pdata['remainAmount'] == '无上限':
                pid = pdata['productId']
                puramount = int(pdata['purchaseAmountDesc'])
                # reamount = int(pdata['remainAmount'])
                break
            elif pdata['pre'] == False and int(pdata['remainAmount']) - int(pdata['purchaseAmountDesc']) > 0:
                pid = pdata['productId']
                puramount = int(pdata['purchaseAmountDesc'])
                # reamount = int(pdata['remainAmount'])
                break
            else:
                k += 1
                while k == len(res2["result"]["data"]):
                    self.assertTrue(False, '无可预约的订单，无法预约')
                continue
        # id = res2["result"]["data"][0]["productId"]

        # 邮寄信息
        url3 = jfhost+'/jfapp/innovate/new/saveCustomerInfo'
        headers3 = {'token': usertoken,
                    'clientId': userId,
                    'Content-Type': 'application/json'
                    }
        data3 = {"email":"123@sina.com","address":"合生汇","province":"北京市","city":"北京市","area":"朝阳区"}
        res3 = requests.post(url=url3, json=data3, headers=headers3,verify=False).json()
        print(res3)


        # 添加银行卡--》选择银行卡
        def savebankcard():
            url30 = jfhost+'/jfapp/innovate/new/bankcardlist'
            headers30 = {'token': usertoken,
                        'clientId': userId,
                        'Content-Type': 'application/json'
                        }
            data30 = {"startPage":1,"pageSize":10}
            res30 = requests.post(url=url30, json=data30, headers=headers30,verify=False).json()
            if res30['result']['total']=='0':
                url = jfhost+'/jfapp/innovate/new/savebankcard'
                data = {"cardNo":"6217 0001 8000 9400 222","bankName":"中国建设银行","province":"北京市","city":"北京市","area":"朝阳区","bankBranchName":"合生汇111","bankCode":"CCB"}
                res31 = requests.post(url=url, json=data, headers=headers30,verify=False).json()
                print(res31)
                return res31['result']['id']
            else:
                return res30['result']['data'][0]['id']

        # 提交预约
        url4 = jfhost+'/jfapp/innovate/savepreappoint'
        data4 = {"productId":pid,"preAmount":puramount,"bankId":savebankcard(),"remark":""}
        res4 = requests.post(url=url4,json=data4,headers=headers2,verify=False).json()
        print(res4)

        # 查询配置记录状态PXZCGL16稳金宝
        def mypreappoint():
            try:
                url5 = jfhost+'/jfapp/user/new/mypreappoint '
                data5 = {"startPage":"1","pageSize":"10","productType":"PXZCGL16"}
                res5 = requests.post(url=url5, json=data5, headers=headers2,verify=False).json()
            except:
                self.assertTrue(False,'模块异常')
            a = res5['result']['data']
            return a
        k=0
        for i in range(len(mypreappoint())):
            if mypreappoint()[i]['stateName']=='待受理':
                print('客户预约单号是'+mypreappoint()[i]['orderId'])
                print('产品名称是'+mypreappoint()[i]['productName'])
                break
            else:
                k += 1
                while k == len(mypreappoint()):
                    self.assertTrue(False, '无待受理的订单，预约失败')
                continue
