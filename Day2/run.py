import unittest
from Day2.day2_work import DaytwoWork
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
tests = ["day2_work.DaytwoWork.test_case001","day2_work.DaytwoWork.test_case002","day2_work.DaytwoWork.test_case003","day2_work.DaytwoWork.test_case004"]
suite.addTest(unittest.TestLoader().loadTestsFromNames(tests))
# suite.addTest(DaytwoWork("test_case001"))
# unittest.TextTestRunner().run(suite)
filename = './' + 'result.html'  # 重构文件名
fp = open(filename, 'wb')  # 定义测试报告存放路径
runner = HTMLTestRunner(stream=fp, title='霍格沃兹测试开发', description='测试人搜索及结果判断', )  # 定义测试报告
runner.run(suite)
fp.close()