from pxframe.pxutil import *


if __name__ == '__main__':

    # 此处登录为获取金服用户的token,用于请求接口数据；
    # 若金服app也开发前端ui测试脚本，需替换现有调接口请求的测试脚本，并弃用所有金服app接口请求，避免一端多种调用方法影响自动化执行
    # jflogin_api()

    # 需输入前端登录页面的验证码，获取登录后cookies，实现实例webdriver刷入cookies而绕过验证码
    # get_cbslogin_cookies()
    #
    # 因受限于安全机制，顾问app请求登录api后，操作前端时需再次请求验证码，一端多种请求方式不适用于自动化，暂弃用
    # gwlogin_api()

    suite = unittest.defaultTestLoader.discover(start_dir=star_dir, pattern=pattern)
    with open('./pxreport/{}({}).html'.format(report_title, nowtime(2)), 'wb') as fm:
        HTMLTestReportCN.HTMLTestRunner(stream=fm,title=report_title,tester=tester,
                                        description=report_desc,verbosity=2).run(suite)

    # 定制发送邮件功能
    # send_email()