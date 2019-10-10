from selenium import webdriver


def get_driver(type, timeout=30):

    type = type.strip().lower()
    if type == 'ff':
        driver = webdriver.Firefox()
        driver.implicitly_wait(timeout)
    elif type == 'ch':
        driver = webdriver.Chrome()
        driver.implicitly_wait(timeout)
    elif type == 'ie':
        driver = webdriver.Ie()
        driver.implicitly_wait(timeout)
    else:
        driver = None
        print('浏览器类型不存在')
    return driver

