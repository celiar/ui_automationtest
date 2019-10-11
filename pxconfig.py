# 读取config.ini文件信息
# import configparser,os
# config_path = os.path.join(os.path.split(os.path.realpath(__file__))[0],'config.ini')
# config = configparser.ConfigParser()
# config.read(config_path)
# value = config.get('oop','object_path')


from pxframe.pxos_handle import *

# 切换系统环境，准生产zsc，生产sc
pmode = 'zsc'.lower()
# 测试系统的配置信息,入参不区分大小写ff,ch,ie
star_dir = './pxcase/cbs/NonMP'
browser_type = 'ch'
object_path = './pagebase.xml'
pattern = 'test*.py'
snapshot_path ='./pxcapture/'

# cbs全流程相关的参数
class ProductName:
    simu = "信远类固收类0902期"
    wjb = "信远智信0902期"
    # other = ''
# 有交互的管理系统地址或host
if pmode=='zsc':
    cbshomeurl = 'http://newcbs.puxinzichan.com/home'
    cbsurl = 'http://newcbs.puxinzichan.com/login.jsp'
    cbshost = 'http://newcbs.puxinzichan.com'
    linkurl = 'http://link.puxinzichan.com/login.jsp'
    jfhost = 'http://jfapp.puxinzichan.com'
    cfphost = 'http://cfpapp.puxinzichan.com'
    sphost = 'http://211.103.153.208:8081'
    cmsurl = 'http://fin.puxinzichan.com/puxin-cms-bg/loginShow.sdo'
    cmshomeurl = 'http://fin.puxinzichan.com/puxin-cms-bg/loginMain.sdo'
else:
    cbshomeurl = 'http://newcbs.puxinasset.com/home'
    cbsurl = 'http://newcbs.puxinasset.com/login.jsp'
    cbshost = 'http://newcbs.puxinasset.com'
    linkurl = 'http://link.puxinasset.com/login.jsp'
    jfhost = 'http://jfapp.puxinasset.com'
    cfphost = 'http://cfpapp.puxinasset.com'
    sphost = 'http://211.103.153.208:8081'
    cmsurl = 'http://fin.puxinasset.com/puxin-cms-bg/loginShow.sdo'
    cmshomeurl = 'http://fin.puxinasset.com/puxin-cms-bg/loginMain.sdo'






# 账号信息
jfname = '肖冰玉'
jfphone = '13120256784'

# gwname = '黎海南'
# gwphone = '18600141740'
# gwpwd = '03003503916'
gwname = '肖冰玉'
gwphone = '13120256784'
gwpwd = '100038873340'
gwpwden_sc = 'Dg7JrrNDrB222v2FuL6IBaxPrqITAeN4CKFnvCK7USMa6yzn501Kyvc1aKXbD+VKY1ooxqFvEIrl\n57fkAFCM9VDQE+RKD9488ElV0tfznWbuAAdUNHoH78ldU44Rjo119sjswFPjlKSR1QHmN99MPdgk\nPvAAZysCBwA2DJ2+ofE=\n'
gwpwden_zsc = 't5nDB8XCRWtIOhPltY7TZGYBB93NWhQ7Nhsnjr\/qAOzw+9VIjIy9ALzGWYZ9b7j9DKM2+zmKrdoe\nGR\/T6ohfgSOU8WLGWyYfcjBuKMr+JUYJ45ygG3NSoz36dHHXhI3EPSAk718ffTT8M2qMCLni\/1dr\nsQGevB7EbtBocp2Tekg=\n'

cbsphone = '13120256784'
cbspwd = 'xiao805633'

cmsphone = '15000000000'
cmspwd = '000000'

linkphone = '18888888888'
linkpwd = 'linkadmin'


# 手机相关信息
gwapk = 'com.puxin.accountant'
jfapk = 'com.puxin.asset'
sn = '49783871'#红米
# sn = '2b94d3b5433f7ece'

# 测试报告信息
tester = 'AutomationTest'
report_title = '测试报告标题'
report_desc = '测试报告描述'


# 邮件信息,需在邮箱设置开启SMTP服务器
smtpserver = 'smtp.sina.com'
fromaddr = "*@sina.com"
toaddrs = ["*@qq.com",'*@qq.com']
rpath = './pxreport/'
email_subject = '普信自动化测试报告{}'.format(nowtime(2))
content = '普信ui测试报告，详情见附件'

