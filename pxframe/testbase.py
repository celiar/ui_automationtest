from pxframe.assertions import *
from pxframe.driverbase import *
from pxframe.pxpoco import *
from pxframe.pxselenium import *
import json


class TestBase(unittest.TestCase):

    # 每个测试类对webdriver实例一次
    @classmethod
    def setUpClass(cls):
        stopapp()
        cls.driver = get_driver(browser_type)
        cls.driver.get(cbsurl)
        with open('cbscookie.json', 'r') as rf:
            cookies = json.loads(rf.read())
        for cookie in cookies:
            cls.driver.add_cookie({
                'name': cookie['name'],
                'value': cookie['value']
            })
        cls.driver.get(cbshomeurl)
        cls.locator = Locator(cls.driver)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.check = Check()
        # print('类初始化')
        startapp()
        gwlogin()
        sleep(3)
    # def __int__(self):
    #     self.driver = get_driver('hh')

    # # 每个测试方法对app状态初始化
    # def setUp(self):
    #
    # # 还原app测试环境
    # def tearDown(self):


    # 清理关闭webdriver
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.driver.service.stop()
        stopapp()
        # print('类环境还原')
class TestBaseWeb(unittest.TestCase):

    # 每个测试类对webdriver实例一次
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver(browser_type)
        cls.driver.get(cbsurl)
        with open('cbscookie.json', 'r') as rf:
            cookies = json.loads(rf.read())
        for cookie in cookies:
            cls.driver.add_cookie({
                'name': cookie['name'],
                'value': cookie['value']
            })
        cls.driver.get(cbshomeurl)
        cls.locator = Locator(cls.driver)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.check = Check()

    # 清理关闭webdriver
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.driver.service.stop()
        # print('类环境还原')

# 顾问app单元测试
class TestBase2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        stopapp()
        startapp()
        gwlogin()
        sleep(3)
        pass
    @classmethod
    def tearDownClass(cls):
        stopapp()
        pass

# 因受限于数据安全制度，需OA申请生产环境数据权限，本工程暂时弃用
class TestBase_CMS(unittest.TestCase):

    # 每个测试类对webdriver实例一次
    @classmethod
    def setUpClass(cls):
        # stopapp()
        cls.driver = get_driver(browser_type)
        cls.driver.get(cmsurl)
        cls.driver.delete_all_cookies()
        with open('cmscookie.json', 'r') as rf:
            cookies = json.loads(rf.read())
        for cookie in cookies:
            cls.driver.add_cookie({
                'name': cookie['name'],
                'value': cookie['value'],
                # 'httpOnly':cookie['httpOnly'],
                # 'path': cookie['path'],
                # 'secure': cookie['secure'],
                'domain':'.puxinzichan.com'
            })
        cls.driver.get(cmshomeurl)
        cls.locator = Locator(cls.driver)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.check = Check()
        print('类初始化')
        # startapp()
        # gwlogin()
        # sleep(3)


    # 清理关闭webdriver
    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        # cls.driver.service.stop()
        # stopapp()
        print('类环境还原')