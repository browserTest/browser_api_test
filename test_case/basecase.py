import requests
import json
import unittest

from common.get_excel_data import *
from common.cast_log import *

class BaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.get_data = get_excel_all_data(excel_dir, 'testcase')

    def get_case_data(self, case_name):
        return get_need_data(self.get_data, case_name)

    def get_expect_result(self, case_data):
        expect = case_data.get('expect')
        return expect

    def send_request(self, case_data):
        case_name = case_data.get('case_name')
        method = case_data.get('method')
        url = case_data.get('url')
        params = case_data.get('data')
        expect = self.get_expect_result(case_data)
        headers = case_data.get('headers')

        if method.upper() == 'GET':
            res1 = requests.get(url = url, params = json.loads(params))
            case_log_info(case_name, url, expect, res1)
        else:
            res1 = requests.post(url = url, data = json.loads(args), headers = json.loads(headers))
            case_log_info(case_name, url, expect, res1)
        res = [expect, res1]
        return res

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









