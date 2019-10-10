from pxframe.pxutil import *


class link(TestBase):

    def add_act(self):
        driver = self.driver
        driver.get("http://link.zhengheht.com/login.jsp")
        driver.find_element_by_id("mobile").send_keys("13671086530")
        driver.find_element_by_id("password").send_keys("linkadmin")
        a = input("请输入验证码：")
        driver.find_element_by_id("validateCode").send_keys(a)
        driver.find_element_by_id("logins").click()
        driver.get("http://link.zhengheht.com/activityPlanReport/getActivityPlanReport")
        driver.maximize_window()
        # 创建活动按钮
        self.locator.wait(2)
        driver.find_element_by_xpath("//*[contains(text(),'创建活动')]").click()
        sleep(3)
        # 索引0是活动类型的请选择
        driver.find_elements_by_xpath("//*[text()='活动类型']/..//div[@class='autocompleteSelectDiv']")[0].click()
        s = driver.find_elements_by_xpath("//*[text()='活动类型']/../div[2]//span[@class='ng-binding']")
        for i in range(len(s)):
            print(s[i].text)
        # 索引0是请选择
        s[1].click()
        sleep(2)
        # 索引1是活动性质的请选择
        driver.find_elements_by_xpath("//*[text()='活动类型']/..//div[@class='autocompleteSelectDiv']")[1].click()
        #  # 向下对浏览器翻页
        # js = "document.getElementById('id').scrollTop=2000"
        # driver.execute_script("window.scrollTo(0,1000)")

        s1 = driver.find_elements_by_xpath("//*[text()='活动类型']/../div[4]//span[@class='ng-binding']")
        for i in range(len(s1)):
            print(s1[i].text)
        s1[1].click()
        t = time.strftime('%m%d', time.localtime(time.time()))
        a = random.randint(0, 999)
        driver.find_element_by_name("activityTheme").send_keys("活动主题名称{}-{}".format(t, a))
        driver.find_element_by_name("activityPersonInCharge").send_keys("活动负责人{}".format(t))
        driver.find_element_by_name("activitySite").send_keys("活动地点{}".format(t))
        driver.find_element_by_xpath("//div[@class='input-group']/input").click()
        driver.find_element_by_xpath("//table[@class='table table-condensed day-view']/tbody/tr[3]/td[5]/div").click()
        #  活动主题执行方的请选择定位
        driver.find_element_by_xpath("//*[text()='活动主题发起方']/..//div[@class='autocompleteSelectDiv']").click()
        s2 = driver.find_elements_by_xpath("//*[text()='活动主题发起方']/../div[4]//span[@class='ng-binding']")
        for i in range(len(s2)):
            print(s2[i].text)
        s2[1].click()
        driver.find_elements_by_xpath("//div[text()='费用归属']/..//div[@class='autocompleteSelectDiv']")[0].click()
        # s3  =\
        driver.find_elements_by_xpath("//*[text()='费用归属']/../div[2]//span[@class='ng-binding']")[1].click()
        # for i in range(len(s3)):
        #     print(s3[i].text)
        # s3[1].click()
        driver.find_elements_by_xpath("//div[text()='费用归属']/..//div[@class='autocompleteSelectDiv']")[1].click()
        driver.find_elements_by_xpath("//*[text()='费用归属']/../div[4]//span[@class='ng-binding']")[1].click()
        wait(2)
        # js1 = 'document.getElementsByTagName("textarea")[0].removeAttribute("readonly")'
        # print(js1)
        # driver.execute_script(js1)
        # driver.find_elements_by_tag_name("textarea")[0].send_keys("董事会/财富平台/信息管理中心\n" + "董事会/财富平台/培训支持中心")
        driver.find_element_by_xpath("//button[text()='选择']").click()
        wait(5)
        driver.find_element_by_id("ztreeOrgs_1_switch").click()
        wait(1)
        driver.find_element_by_id("ztreeOrgs_2_switch").click()
        wait(1)
        driver.find_element_by_id("ztreeOrgs_34_check").click()
        wait(3)
        driver.find_element_by_xpath("//button[contains(text(),'确定')]").click()
        wait(2)
        driver.find_element_by_name("investingCustomerCount").send_keys("10")
        driver.find_element_by_name("activitySpeaker").send_keys("晓晓")
        driver.find_element_by_name("lectureContent").send_keys("主讲内容")
        driver.execute_script("window.scrollTo(0,500)")
        driver.find_element_by_name("instructionAndRemark").send_keys("说明及备注")
        driver.find_element_by_name("activityInfo").send_keys("活动信息")
        # t = driver.find_element_by_xpath("//*[contains(text(),'本人')]")
        # t.click()
        wait(5)
        driver.find_element_by_xpath("//button[text()='本人']").click()
        driver.find_element_by_name("editForm.newCustomerNum").send_keys("2")
        driver.find_element_by_name("editForm.oldCustomerNum").send_keys("3")
        driver.find_element_by_name("editForm.staffNum").send_keys("1")
        driver.execute_script("window.scrollTo(0,1000)")
        driver.find_element_by_name("editForm.estimateScalePerformance").send_keys("1000")
        driver.find_element_by_name("editForm.estimateDiscountPerformance").send_keys("999")
        driver.find_element_by_xpath("//button[text()='添加']").click()
        # driver.find_element_by_xpath("//*[text()='预估费用明细']/../../following-sibling::div/div[2]//div[@class='autocompleteSelectDiv']").click()
        driver.find_element_by_xpath(
            "//*[text()='科目']/../../following-sibling::tbody//div[@class='autocompleteSelectDiv']").click()
        s3 = driver.find_elements_by_xpath("//*[text()='科目']/../../following-sibling::tbody//span[@class='ng-binding']")
        for i in range(len(s3)):
            print(s3[i].text)
        s3[1].click()
        driver.find_element_by_name("fitem.brandName").send_keys("品牌")
        driver.find_element_by_name("fitem.expenseName").send_keys("名称")
        driver.find_element_by_name("fitem.specification").send_keys("规格")
        driver.find_element_by_name("fitem.unitPrice").send_keys("2")
        driver.find_element_by_name("fitem.quantity").send_keys("1000")
        driver.find_element_by_name("item.remark").send_keys("备注")
        wait(2)
        # 可把文件放在工程目录下
        driver.find_element_by_id("fileUploads").send_keys("D:\\demo.jpg")
        wait(1)
        driver.find_element_by_id("fileUploads").send_keys("D:\\gwhome.mp4")
        wait(2)
        driver.find_element_by_id("fileUploads").send_keys("D:\\c.zip")
        wait(4)
        driver.find_element_by_id("fileUploads").send_keys("D:\\d.ppt")
        wait(3)
        driver.find_element_by_xpath("//*[text()='保存']").click()