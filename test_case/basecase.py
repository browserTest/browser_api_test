import requests
import json
import unittest

from common.get_excel_data import *
from common.cast_log import *

class BaseCase(unittest.TestCase):

    # 获取execl数据
    @classmethod
    def setUpClass(cls):
        cls.get_data = get_excel_all_data(excel_dir, 'testcase')

    # 获取当前用例数据
    def get_case_data(self, case_name):
        return get_need_data(self.get_data, case_name)

    # 获取当前用例的预期结果
    def get_expect_result(self, case_data):
        expect = case_data.get('expect')
        return expect

    # 发送request请求
    def send_request(self, case_data):
        # 获取当前用例的相关参数
        case_name = case_data.get('case_name')
        method = case_data.get('method')
        url = case_data.get('url')
        params = case_data.get('data')
        expect = case_data.get('expect')

        # expect = self.get_expect_result(case_data)
        headers = case_data.get('headers')

        # 对接口类型进行判断
        if method.upper() == 'GET':
            # 发送请求后，将结果赋值给res1，注意，get请求传参是用params
            res1 = requests.get(url = url, params = json.dumps(params))
            case_log_info(case_name, url, expect, res1)
        else:
            # post请求传参用data
            res1 = requests.post(url = url, data = json.dumps(params), headers = json.loads(headers))
            case_log_info(case_name, url, expect, res1)
        res = [expect, res1]
        return res


    """封装通过用例名称获取到接口返回数据"""
    def get_result(self, case_name):
        case_data = self.get_case_data(case_name)
        res = self.send_request(case_data)
        return res



    """获取所有返回结果"""
    def get_request_all(self, case_name):
        res = self.get_result(case_name)
        result_expect = int(res[0])
        result_actual = json.loads(res[1].text)
        result = [result_expect, result_actual]
        return result



    """获取结果中的code"""
    def get_request_code(self, case_name):
        res = self.get_result(case_name)
        result_actual = int(json.loads(res[1].text)['code'])
        result_expect = int(res[0])
        result = [result_expect, result_actual]
        return result









