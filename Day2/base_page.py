from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    #获取url
    def get_url(self,url):
        self.driver.get(url)

    #元素定位
    def locator_element(self,loc):
        return self.driver.find_element(*loc)

    #输入
    def sendkeys(self,loc,value):
        self.locator_element(loc).send_keys(value)

    #元素点击
    def click(self,loc):
        self.locator_element(loc).click()

    #获取断言文本
    def text(self,loc):
        return self.locator_element(loc).text

    #关闭网页
    def quit(self):
        self.driver.quit()

    #截屏
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # #enter搜索
    # def keyboard(self,loc,value):
    #     self.driver.find_element(loc).send_keys(value)
