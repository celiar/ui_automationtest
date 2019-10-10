import re,os,time,jsonpath,random,string
from datetime import date, timedelta
import xlrd,xlwt
from xlutils.copy import copy

def inputcode(msg):
    os.system('''python -c "print('{}')" \n'''.format(msg))
    value = input('')
    return value


def nowtime(s=1):
    if s==1:
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))
    else:
        return time.strftime('%Y_%m_%d_%H.%M.%S', time.localtime(time.time()))

def phonenum():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    return (random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8)))

def idCard():
    id1 = "100100"
    id2 = id1 + str(random.randint(1930, 2013))
    da = date.today() + timedelta(days=random.randint(1, 366))
    id3 = id2 + da.strftime('%m%d')
    return (id3 + str(random.randint(1000, 3000)))

def account_random():
    id1 = "100100"
    id2 = id1 + str(random.randint(1930, 2013))
    da = date.today() + timedelta(days=random.randint(1, 366))
    id3 = id2 + da.strftime('%m%d')
    return (id3 + str(random.randint(1000, 3000)))

def cname():
    s = string.ascii_lowercase
    return random.choice(s) + random.choice(s) + random.choice(s) + random.choice(s) + random.choice(s)

def res_expression(data, LB, RB):
    rule = LB + r"(.*?)" + RB
    association = re.findall(rule, data)
    return association

