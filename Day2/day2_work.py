import time
import unittest
from HTMLTestRunner import HTMLTestRunner

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from Day2.base_page import BasePage
from Day2.search import Search


driver=webdriver.Chrome()

class DaytwoWork(unittest.TestCase):
    #实例化对象
    def setUp(self) -> None:
        self.driver=Search(driver)
    #关闭网页
    def tearDown_class(self) -> None:
        self.driver.quit()
    #冒烟测试
    def test_case001(self):
        self.driver.search(value='selenium')
        res_slement = self.driver.text((By.CSS_SELECTOR, ".topic-title"))
        if 'selenium' in res_slement:
            pass
        else:
            self.driver.save_screenshot("冒烟失败.png")
        assert 'selenium' in res_slement
        # allure.attach.file("image.png", name='hogwarts', attachment_type=allure.attachment_type.PNG)

    # 测试用例2，高级搜索测试
    def test_case002(self):
        self.driver.seniorsearch(value='selenium')
        res_slement=self.driver.text((By.CSS_SELECTOR,".topic-title"))
        if 'selenium' in res_slement:
            pass
        else:
            self.driver.save_screenshot("高级搜索失败.png")
        assert 'selenium' in res_slement

    #测试用例3，搜索空内容
    def test_case003(self):
        self.driver.seniorsearch(value='')
        res_slement = self.driver.text((By.CSS_SELECTOR, ".fps-invalid"))
        if '您的搜索词过短。' == res_slement:
            pass
        else:
            self.driver.save_screenshot("空内容搜索失败.png")
        assert '您的搜索词过短。' == res_slement

    #测试用例4，特殊字符
    def test_case004(self):
        self.driver.seniorsearch(value='$*&^^')
        res_slement = self.driver.text((By.CSS_SELECTOR, ".loading-container h3"))
        if '找不到结果222。' == res_slement:
            pass
        else:
            self.driver.save_screenshot("特殊字符搜索失败.png")
        assert '找不到结果222。' == res_slement





