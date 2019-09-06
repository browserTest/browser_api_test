import unittest

from test_case.testcast import *
from common.HTMLTestReportCN import HTMLTestRunner
from common.send_email import send_email
from config.config import *

"""整合用例"""
suite = unittest.TestSuite()
suite.addTest(TestCase('test_get_test002a'))


# suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)

"""执行用例"""
if send_email_switch:
    file = open(report_dir, 'wb') # 二进制写格式打开要生成的报告文件
    HTMLTestRunner(stream = file,title = "",description="", tester="autoBuild").run(suite)
    file.close()
else:
    unittest.TextTestRunner(verbosity = 2).run(suite)



"""发送邮件"""
if send_email_switch:
    send_email(report_dir,email_receiver)








