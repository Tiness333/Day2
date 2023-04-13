from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from  Day2.base_page import BasePage
class Search(BasePage):
    #主页地址
    url='https://www.ceshiren.com'

    #元素定位
    #首页搜索按钮定位
    search_loc=(By.ID,'search-button')
    #高级搜索按钮定位
    advancedsearch_loc=(By.CSS_SELECTOR,".widget-link")
    #首页输入框定位
    input_loc1=(By.ID,'search-term')
    #高级搜索输入框定位
    input_loc=(By.CSS_SELECTOR,".full-page-search")
    # value='selenium'
    #高级搜索页面搜索按钮定位
    performsearch_loc=(By.CSS_SELECTOR,".search-cta")
    filename='定位异常.png'
    #冒烟搜索
    def search(self,value):
        try:
            # 打开网站
            self.get_url(self.url)
            # 点击搜索进入搜索模式
            self.click(loc=self.search_loc)
            # 点击搜素输入框并输入内容
            self.sendkeys(loc=self.input_loc1, value=value)
            # 执行搜索
            WebDriverWait(self.driver, 10).until (
                expected_conditions.element_to_be_clickable(
                    (By.ID,"search-term")))
            self.driver.find_element(By.ID,'search-term').send_keys(Keys.ENTER)
        except Exception:
            self.save_screenshot(filename=self.filename)
            print("用例执行失败")


    #高级搜索业务流程
    def seniorsearch(self,value):
        try:
            # 打开网站
            self.get_url(self.url)
            # 点击搜索进入搜索模式
            self.click(loc=self.search_loc)
            # 进入高级搜索模式
            self.click(loc=self.advancedsearch_loc)
            # 点击搜素输入框并输入内容
            self.sendkeys(loc=self.input_loc,value=value)
            # 执行搜索
            self.click(loc=self.performsearch_loc)
        except Exception:
            self.save_screenshot(filename=self.filename)
            print("用例执行失败")




