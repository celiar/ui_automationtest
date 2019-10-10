from pxconfig import *
from pxframe.pxos_handle import *
import requests,json

def jflogin_api():
    phonecode = inputcode('请{}输入金服验证码'.format(jfname))
    logindata = {"phone": jfphone, "phonecode": phonecode, "registrationId": ""}
    url1 = jfhost+'/jfapp/user/login'
    headers1 = {'Content-Type': 'application/json'}
    res = requests.post(url=url1, json=logindata, headers=headers1).json()
    # gwtoken = res["token"]
    # gwId = res["result"]["userId"]
    with open('./jflogin_res.json','w') as rw:
        json.dump(res,rw)

# @property
def jfheaders():
    # 若在本文件调用，path为os.path.dirname(__file__)
    path = os.path.dirname(os.path.dirname(__file__))
    with open(path + '/jflogin_res.json','r') as rr:
        a = json.load(rr)
    jftoken = a['result']['token']
    jfId = a['result']['userId']
    header = {
        'token': jftoken,
        'clientId': jfId,
        'Content-Type': 'application/json'
    }
    return header


# gwpwd是肖冰玉的密码，如需更换，请联系开发了解密码加密算法
def gwlogin_api():
    phonecode = inputcode('请{}输入顾问验证码'.format(gwname))
    if pmode=='sc':
        pwd = gwpwden_sc
    else:
        pwd = gwpwden_zsc
    logindata = {"mobile":gwphone,"phonecode":phonecode,"financialpwd":pwd,"registrationId":""}
    url1 = cfphost+'/cfpapp/employee/login'
    headers1 = {'Content-Type': 'application/json'}
    res = requests.post(url=url1, json=logindata, headers=headers1).json()
    # gwtoken = res["token"]
    # gwId = res["result"]["userId"]
    with open('./gwlogin_res.json','w') as rw:
        json.dump(res,rw)

def gwtoken():
    path = os.path.dirname(os.path.dirname(__file__))
    with open(path + '/gwlogin_res.json','r') as rr:
        a = json.load(rr)
    gwtoken = a['token']
    return gwtoken

def mypreappoint():
    url5 = jfhost+'/jfapp/user/new/mypreappoint'
    data5 = {"startPage": "1", "pageSize": "10", "productType": "PXZCGL17"}
    res5 = requests.post(url=url5, json=data5, headers=jfheaders()).json()
    a = res5['result']['data']
    return a

#获取cfp数据
def getcfp(value):
    url = cfphost + value
    data = {"startPage": "1", "pageSize": "15"}
    headers = {
        'token': gwtoken(),
        "Content-Type": "application/json",
        "clientId": "3776"
    }
    return requests.post(url, headers=headers, json=data).json()["result"]["data"]

# 产品到期
def getduelist():
    url = cfphost+"/cfpapp/fortune/productDuelist"
    data = {"startPage": "1", "pageSize": "15"}
    headers = {
        'token': gwtoken(),
        "Content-Type": "application/json",
        "clientId": "3776"
    }
    return requests.post(url, headers=headers, json=data).json()["result"]["data"]

# 获取稳金宝产品列表
def getwybao(id):
    url=cfphost+"/cfpapp/innovate/productinnovatelist"
    data = {"startPage":"1","pageSize":"10","productType":"PXZCGL{}".format(id)}
    headers = {
        'token': gwtoken(),
        "Content-Type": "application/json",
        "clientId": "3776"
    }
    return requests.post(url,headers=headers,json=data).json()["result"]["data"]

#获取稳金宝产品列表
def getwybaodetail(id):
    url = cfphost+"/cfpapp/innovate/newProductinnovatedetail"
    headers = {
        'token': gwtoken(),
        "Content-Type": "application/json",
        "clientId": "3776"
    }
    data = {"id": str(id)}
    return requests.post(url, headers=headers, json=data).json()["result"]

#获取某顾问某活动管理的报名签到列表
def getenrollsignlist(id):
    url = cfphost+"/cfpapp/activity/enrollSignList"
    headers = {
        "clientId": "3776",
        "Content-Type": "application/json",
        "token": gwtoken()
    }
    data = {"id":str(id),"startPage":1,"pageSize":100}
    r = requests.post(url, headers=headers, json=data).json()["result"]["data"]
    a=[]
    for i in range(len(r)):
        if r[i]["isEnrollName"]=="是":
            try:
                a.append(r[i]["name"])
            except:
                continue
    return a

#接口获取投顾资讯的内容
def getinfo( type):
    url = cfphost+"/cfpapp/information/infomationlist"
    data = {"startPage":"1","pageSize":"10","articalType":type}
    headers = {
        "Content-Type":"application/json",
        "token":gwtoken()
    }
    r = requests.post(url,headers=headers,json=data).json()["result"]["data"][0]
    # print(r["title"],r["titleDetail"],r["conferenceTime"])
    return r

def getvideo(type):
    url = cfphost+"/cfpapp/information/videolist "
    data = {"startPage":"1","pageSize":"10","videoType":type}
    headers = {
        "Content-Type":"application/json",
        "token":gwtoken()
    }
    r = requests.post(url,headers=headers,json=data).json()["result"]["data"][0]
    # print(r["title"],r["titleDetail"],r["conferenceTime"])
    return r

def getactlist():
    url = cfphost+"/cfpapp/activity/dataList"
    headers = {
        "clientId": "3776",
        "Content-Type": "application/json",
        "token": gwtoken()
    }
    data = {"startPage": 1, "pageSize": 10}
    return requests.post(url, headers=headers, json=data).json()["result"]["data"]

def getactdetail(id):
    url = cfphost+"/cfpapp/activity/detail"
    headers = {
        "clientId": "3776",
        "Content-Type": "application/json",
        "token": gwtoken()
    }
    data = {"id": id}
    return requests.post(url, headers=headers, json=data).json()["result"][0]

def getinforep():
    url = cfphost+"/cfpapp/innovate/disclosurelist"
    data={"startPage":1,"pageSize":15}
    headers ={
        "clientId":"3776",
        'Content-Type': 'application/json',
        'token': gwtoken()
    }
    r1= requests.post(url=url,headers=headers,json=data).json()['result']['data'][0]['productName']
    r2 = requests.post(url=url, headers=headers, json=data).json()['result']['data'][0]['data'][0]['name']
    r3= requests.post(url=url, headers=headers, json=data).json()['result']['data'][0]['data'][0]['disclosureTime']
    return r1,r2,r3

#顾问APP--预约处理四个列表
def getcpreappoint(id):
    # id取1-2-3-99
    url = cfphost+"/cfpapp/innovate/customerpreappoint"
    data = {"startPage":"1","pageSize":"10","employeeId":"0300350","state":id}
    headers = {
        "clientId": "3776",
        'Content-Type': 'application/json',
        'token': gwtoken()
    }
    return requests.post(url, headers=headers, json=data).json()["result"]["data"]

#金服-产品-稳金宝-智信-SJP-稳金宝-new，预约接口数据提交
def save_preappoint(productId, preAmount):
    url1 = jfhost+"/jfapp/innovate/savepreappoint"
    headers1 = {'token':'98548f711146ee9e8adde59ccd1df457dc098776393240fb94449a149be31ca1',
               'clientId': '515486',
               'Content-Type': 'application/json'}
    data1 = {"productId":productId, "preAmount":preAmount, "preTime":"2019-04-24", "remark":"请审核请通过"}
    response1 = requests.post(url=url1, json=data1, headers=jfheaders())
    # print(response1.text)
    # print(response1.status_code)
    r1 = json.loads(response1.text)
    print(r1['message'])
    if r1['message']=='成功':
        pass
    else:
        print("数据有误")

def approve_preappoint(appointId):
    url2 = cfphost+"/cfpapp/innovate/approvepreappoint"
    data2 = {"appointId": appointId,"state":"2"}
    headers = {
        "clientId": "3776",
        'Content-Type': 'application/json',
        'token': gwtoken()
    }
    response2 = requests.post(url=url2, json=data2, headers=headers)
    print(response2.text)
    print(response2.status_code)
    r2 = json.loads(response2.text)
    print(r2['message'])

#获取消息列表
def getmsgindex():
    url = cfphost+"/cfpapp/user/messageindex"
    headers = {
        "clientId": "3776",
        "Content-Type": "application/x-www-form-urlencoded",
        "token": gwtoken()
    }
    return requests.post(url, headers=headers).json()["result"]

#获取商业保理产品列表
def getbaoli():
    url = cfphost+"/cfpapp/innovate/productinnovatelist"
    headers = {
        "clientId": "3776",
        "Content-Type": "application/json",
        "token": gwtoken()
    }
    data = {"startPage":"1","pageSize":"10","productType":"PXZCGLBL"}
    return requests.post(url, headers=headers, json=data).json()["result"]["data"]


def getsimu( type):
    url = cfphost+"/cfpapp/innovate/productinnovatelist"
    data = {"startPage": "1", "pageSize": "10", "productType": "PXZCGL{}".format(type)}
    headers = {
            "clientId": "3776",
            "Content-Type": "application/json",
            "token": gwtoken()
        }
    return requests.post(url, headers=headers, json=data).json()["result"]["data"]

def getsimudetail( id):
    url = cfphost+"/cfpapp/innovate/newProductinnovatedetail"
    data = {"id":"{}".format(id)}
    headers = {
        "clientId": "3776",
        "Content-Type": "application/json",
        "token": gwtoken()
    }
    return requests.post(url, headers=headers, json=data).json()["result"]

# 商票url有更新（home变homepage）
def getshpiao():
    url=sphost+"/bill-mobile/gwhome/getProductList?pageNum=0&auctionStatus=0&duration=0&channel=pxjf"
    headers = {
        "Content-Type": "application/json"
    }
    return requests.post(url,headers=headers).json()["data"]


def getshpiaodetail(id):
    url = sphost+"/bill-mobile/borrow/searchBillPacket?itemId={}&token=&channel=pxjf".format(id)
    headers = {
        "Content-Type": "application/json"
    }
    return requests.post(url, headers=headers).json()

def getpiaojudetail(id):
    url = sphost+"/bill-mobile/borrow/searchBilldetails?itemId={}&channel=pxjf".format(id)
    headers = {
        "Content-Type": "application/json"
    }
    return requests.post(url, headers=headers).json()["data"]
