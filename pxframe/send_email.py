import smtplib,os
from email.mime.text import MIMEText
from pxconfig import *
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

# 获取最新的测试报告全路径
def new_report(pxreport_dir):
    #将测试报告文件夹下的所有文件名作为一个列表返回
    lists = os.listdir(pxreport_dir)
    # print(lists)
    #对所有测试报告按照生成时间进行排序
    lists.sort(key=lambda filename: os.path.getmtime(pxreport_dir+filename))
    #获取最新的测试报告
    recent = lists[-1]
    #指定最新的测试报告路径
    file_path = os.path.join(pxreport_dir, recent)
    return file_path

# 发送邮件
def send_email():
    password = inputcode('邮箱{}的密码'.format(fromaddr))
    textApart = MIMEText(content,'plain')

    rfile = new_report(rpath)
    msg = MIMEApplication(open(rfile, 'rb').read())
    msg.add_header('Content-Disposition', 'attachment', filename=rfile)

    m = MIMEMultipart()
    m['from'] = fromaddr
    m.attach(textApart)

    m.attach(msg)
    m['Subject'] = Header(email_subject,'utf-8')

    try:
        server = smtplib.SMTP(smtpserver)
        # server.set_debuglevel(1)
        # server.starttls()
        server.login(fromaddr,password)
        server.sendmail(fromaddr,toaddrs,m.as_string())
        print('向{}发送测试报告成功'.format(toaddrs))
        server.quit()
    except smtplib.SMTPException as e:
        print('error:',e)

