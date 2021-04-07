from locust import TaskSet, HttpUser, between, task, constant
import queue
import xlrd
import os, sys
import time
import logging
import subprocess
from util import *


# 定义用户行为
class flfg_task(TaskSet):
    '''法律法规库'''

    def on_start(self):
        self.kw = "绿化"
        pass

    # @task(1)装饰压测行为，1是组合场景任务比重
    # @task(1)
    # def chl_Fulltext(self):
    #     self.client.post(url,data)

    @task(1)
    def chl_title(self):
        # # 消费数据队列
        # try:
        #     v = self.parent.user_data_queue.get_nowait()
        # except queue.Empty:
        #     exit(0)

        # # 使用数据
        # name = v["NAME"]

        # 压测UI中对应的名称
        apiname = "中央法规"

        # 接口路由
        url = "/law/chl"

        # 接口传入数据body
        data = {
            "Menu": "law",
            "Keywords": self.kw,
            "PreKeywords": "",
            "SearchKeywordType": "Title",
            "MatchType": "Exact",
            "RangeType": "Piece",
            "Library": "chl",
            "ClassFlag": "chl",
            "GroupLibraries": "",
            "QuerySearchCondition": "Title+Exact+Piece+0",
            "QueryOnClick": False,
            "AfterSearch": True,
            "RequestFrom": "btnSearch",
            "SearchInResult": "",
            "PreviousLib": "chl",
            "IsSynonymSearch": "false",
            "RecordShowType": "List",
            "ClassCodeKey": " ,,,,,",
            "IsSearchErrorKeyword": "",
            "X-Requested-With": "XMLHttpRequest"
        }

        # 请求头，包括文本格式，身份信息，设备信息等
        headers = {
            "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "pkulaw_v6_sessionid=lg4nyjck4z3y5xi45te41oc3; __RequestVerificationToken=iSY506zVUAndpc-OJtZ0cQkk6j8WSsqZQpcE8rMoqc0m_4EHB8KsHlaDbqnEuMwZRtYSLd3QrmBocK1_xSMzgPOlvgU1; QINGCLOUDELB=fb5583a589e2510ccd053c7ad27b4c63bfc65627d6c676fd45c63459fcfd7d1e; xClose=25; ASP.NET_SessionId=qcjyyawfr5x1u4j0l2w40ijy; FULL_BACKGROUND_DEFAULT_BG=bg-blue; FULLTEXT_FONT_DEFAULT_SIZE=16; bdshare_firstime=1609426983664; Hm_lvt_8266968662c086f34b2a3e2ae9014bf8=1615948402,1615949153,1616142092,1617176525; authormes=bd694c219a83d9ef5632fb287550dc115d22b14a1138c8e155a0342de0cd77a362b6652675c5736bbdfb; Hm_lpvt_8266968662c086f34b2a3e2ae9014bf8=1617349450; xCloseNew=3; redSpot=false",
        }

        # 发起请求，按实际请求方式设置（get、post）,catch_response=True记录locust断言日志
        with self.client.post(url=url, name=apiname, headers=headers, data=data, catch_response=True) as res:
            # 断言可用其他自定义方法
            if util.get_element(res.text, "//span[@class='hitClass']") == self.kw:
                res.success()
            else:
                res.failure("在法律法规库，对标题【{}】检索结果异常".format(self.kw))
        # 记录压测日志，包括响应数据和异常捕获
        logging.info(res.text)

# 模拟用户之间的任务执行和其他用户行为
class bdfb_User(HttpUser):
    # 加载任务集合
    tasks = [flfg_task]

    # 服务器地址或域名
    host = "http://192.168.0.179:8344"

    # 思考时间，按实际业务需求设定，constant固定，between取区间值
    # wait_time = between(1, 3)
    wait_time = constant(1)

    # 生产数据队列
    # user_data_queue = queue.Queue()
    # rb = xlrd.open_workbook("./data.xlsx")
    # sheet = rb.sheet_by_index(0)
    # n = sheet.nrows
    # for i in range(1, n):
    #     name = sheet.cell_value(i, 0)
    #     userId = sheet.cell_value(i, 0)
    #     data = {
    #         "USERID": int(userId),
    #         'NAME': name,
    #     }
    #     user_data_queue.put_nowait(data)


if __name__ == '__main__':
    # 获取本文件名称
    fname = os.path.basename(sys.argv[0]).split('.')[0]

    # -s响应超时10s;-f指定文件；' 1>{1}.log 2>&1'写入日志log
    os.system('locust'
              ' --loglevel=INFO'
              ' 1>{1}.log 2>&1'
              # ' --headless -t 10s'
              # ' --exit-code-on-error 404'
              ' -s 10'
              ' -f {0}.py'.format(fname, '法律法规性能测试日志'))
