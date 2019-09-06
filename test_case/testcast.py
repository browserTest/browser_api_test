from test_case.basecase import BaseCase
import logging
from data.getdb import *

class TestCase(BaseCase):

    # def test_get_http(self):
    #     result = self.get_request_code('test_get_http')
    #     self.assertEqual(result[0], result[1])
    #
    # def test_get_https(self):
    #     result = self.get_request_code('test_get_https')
    #     self.assertEqual(result[0], result[1])

    """test003——LYX"""
    def test_get_test003(self):
        result = self.get_request_code('test003')
        self.assertEqual(result[0],result[1])

    """test011a——LYX"""
    def test_get_test011a(self):
        result = self.get_request_code('test011a')
        self.assertEqual(result[0],result[1])

    """test011b——LYX"""
    def test_get_test011b(self):
        result = self.get_request_value('test011b')
        self.assertEqual(str(result[0]),str(result[1]))

    """test011c——LYX"""
    def test_get_test011c(self):
        result = self.get_request_DB('test011c')
        self.assertEqual(result[0],result[1])

    """test016——LYX"""
    def test_get_test016(self):
        result = self.get_request_code('test016')
        self.assertEqual(result[0],result[1])

    """test021——LYX"""
    def test_get_test021(self):
        result = self.get_request_code('test021')
        self.assertEqual(result[0],result[1])

    """test004a——LJX"""
    def test004_a(self):
        result = self.get_request_code('test004a')
        self.assertEqual(result[0], result[1])

    """test004b——LJX"""
    def test004_b(self):
        result = self.get_response_value('test004b')
        for i in range(len(result)):
            if result[i]['type'] == 'android_uc':
                res = result[i]['value']
        self.assertEqual(android_uc, res)





    """test002——LCM——校验实际结果与预期结果值都为200"""
    def test_get_test002(self):
        # 直接调用结果返回code值的方法，但预期结果值（expect）必须是200，该方法得到的实际结果值是code=200
        result = self.get_request_code('test002')
        # 断言预期结果与实际结果是否相等
        self.assertEqual(result[0], result[1])


    """test007——LCM"""
    def test_get_test007(self):
        result = self.get_request_code('test007')
        self.assertEqual(result[0],result[1])

    """test009——LCM"""
    def test_get_test009(self):
        # getUserData接口返回的结果是从大数据那边拿去的数据
        result = self.get_request_code('test009')
        self.assertEqual(result[0], result[1])

    """test019——LCM"""
    def test_get_test019(self):
        result = self.get_request_code('test019')
        print(result)
        self.assertEqual(result[0], result[1])

