from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import xml.etree.ElementTree as ET
from pxconfig import *


class Locator:
    # 实例化变量driver和et
    def __init__(self, driver):
        self.driver = driver
        self.et = ET.parse(object_path)

    def findby(self,type, value):
        if type == 'id':
            by = By.ID
        elif type == 'name':
            by = By.NAME
        elif type == 'xpath':
            by = By.XPATH
        elif type == 'class':
            by = By.CLASS_NAME
        elif type == 'linktext':
            by = By.LINK_TEXT
        elif type == 'css':
            by = By.CSS_SELECTOR
        elif type == 'tag':
            by = By.TAG_NAME
        else:
            by = None
            print('定位方式工具不支持')
        try:
            element = self.driver.find_element(by, value)
        except:
            element = None
        return element

    def findbyx(self,id):
        return self.driver.find_element_by_xpath("//input[@id='{}']/../p".format(id))

    def findsby(self,type, value):
        if type == 'id':
            by = By.ID
        elif type == 'name':
            by = By.NAME
        elif type == 'xpath':
            by = By.XPATH
        elif type == 'class':
            by = By.CLASS_NAME
        elif type == 'linktext':
            by = By.LINK_TEXT
        elif type == 'css':
            by = By.CSS_SELECTOR
        elif type == 'tag':
            by = By.TAG_NAME
        else:
            by = None
            print('定位方式工具不支持')
        try:
            element = self.driver.find_elements(by, value)
        except:
            element = None
        return element

    def get_element(self, page, name):
        try:
            type = self.et.find(u'.//%s/%s' % (page, name)).attrib['t']
            value = self.et.find(u'.//%s/%s' % (page, name)).attrib['v']
        except:
            print(page+' '+ name + '不存在')
        if type == 'id':
            by = By.ID
        elif type == 'name':
            by = By.NAME
        elif type == 'xpath':
            by = By.XPATH
        elif type == 'class':
            by = By.CLASS_NAME
        elif type == 'linktext':
            by = By.LINK_TEXT
        elif type == 'plinktext':
            by = By.PARTIAL_LINK_TEXT
        elif type == 'tag':
            by = By.TAG_NAME
        elif type == 'css':
            by = By.CSS_SELECTOR
        else:
            by = None
            print('定位方式工具不支持')
        try:
            element = self.driver.find_element(by, value)
        except:
            element = None
        return element

    def get_elements(self, page, name):
        try:
            type = self.et.find(u'.//%s/%s' % (page, name)).attrib['t']
            value = self.et.find(u'.//%s/%s' % (page, name)).attrib['v']
        except:
            print(page + ' ' + name + '不存在')
        if type == 'id':
            by = By.ID
        elif type == 'name':
            by = By.NAME
        elif type == 'xpath':
            by = By.XPATH
        elif type == 'class':
            by = By.CLASS_NAME
        elif type == 'linktext':
            by = By.LINK_TEXT
        elif type == 'plinktext':
            by = By.PARTIAL_LINK_TEXT
        elif type == 'tag':
            by = By.TAG_NAME
        elif type == 'css':
            by = By.CSS_SELECTOR
        else:
            by = None
            print('定位方式工具不支持')
        elements = self.driver.find_elements(by, value)
        return elements

    def wait(self, seconds):
        time.sleep(seconds)

    def open(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.close()
        
    def click(self, page, name):
        element = self.get_element(page, name)
        element.click()
        # time.sleep(2)

    def clicks(self, page, name,i):
        k = self.get_elements(page, name)
        k[i].click()
        # time.sleep(1)

    def send_keys(self, page, name, text):
        element = self.get_element(page, name)
        element.send_keys(text)
        # time.sleep(1)

    # 悬停
    def move_to(self, page, name):
        # time.sleep(1.5)
        element = self.get_element(page, name)
        ActionChains(self.driver).move_to_element(element).perform()
        # time.sleep(1)

    def text(self, page, name):
        try:
            element = self.get_element(page, name)
            return element.text
        except:
            return None

    def move(self,a):
        if a=='下':
            js1 = "document.documentElement.scrollTop=10000"
            self.driver.execute_script(js1)
        elif a=='上':
            js2 = "document.documentElement.scrollTop=0"
            self.driver.execute_script(js2)
        elif a=='左':
            js3 = "window.scrollTo(200,1000)"
            self.driver.execute_script(js3)
        else:
            print("不存在该方向的滑动操作")

    def attri(self, page, name, att):
        try:
            element = self.get_element(page, name)
            return element.get_attribute(att)
        except:
            return None

    def texts(self, page, name):
       list = []
       elements = self.get_elements(page, name)
       for e in elements:
           list.append(e.text)
       return list

    def attris(self,  page, name, att):
        list = []
        elements = self.get_elements(page, name)
        for e in elements:
            try:
                list.append(e.get_attribute(att))
            except:
                pass
        return list

    def select_by_value(self, page, name, text):
        element = self.get_element(page, name)
        Select(element).select_by_value(text)
        self.wait(1)

    def select_by_random(self, page, name):
        element = self.get_element(page, name)
        select = Select(element)
        index = random.randint(len(select.options))
        select.select_by_index(index)

    def elements_number(self, page, name):
        try:
            elements = self.get_elements(page, name)
        except:
            elements = []
        return len(elements)

    def element_is_exist(self, page, name):
        try:
            self.get_element(page, name)
            return True
        except:
            return False

    def elements_is_exist(self, by, value):
        elements = self.driver.find_elements(by, value)
        if len(elements)>0:
            return True
        else:
            return False

    def click_and_getText(self, by1, value1, by2, value2):
        links = []
        result = []
        elements = self.driver.find_elements(by1, value1)
        for e in elements:
            try:
                links.append(e.get_attribute('href'))
            except:
                pass

        for l in links:
            self.open(l)
            try:
                result.append(self.driver.find_element(by2, value2).text)
            except:
                pass
        return result