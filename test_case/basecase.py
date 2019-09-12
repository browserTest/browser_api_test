import requests
import json
import unittest


from common.get_excel_data import *
from common.cast_log import *
from data.db import DB   #引入数据库——LYX
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告——LYX
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from common.cast_log import *

from data.getdb import *

class BaseCase(unittest.TestCase):

    # 获取execl数据
    @classmethod
    def setUpClass(cls):
        cls.get_data = get_excel_all_data(excel_dir, 'testcase')
        cls.db = DB()

    # 获取当前用例数据
    def get_case_data(self, case_name):
        return get_need_data(self.get_data, case_name)

    # 获取当前用例的预期结果
    def get_expect_result(self, case_data):
        expect = case_data.get('expect')
        return expect

    # 获取当前用例的data——LYX
    def get_expect_data(self, case_name):
        case_data = self.get_case_data(case_name)
        data = case_data.get('data')
        return data

    # 获取当前用例的url——LYX
    def get_url(self, case_name):
        case_data = self.get_case_data(case_name)
        url = case_data.get('url')
        return url

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

        # 增加判断，请求参数中若含有access_token，则对其更新——LYX
        if 'access_token' in params:
            params = json.loads(params)
            params['access_token'] = self.get_token()
            params = json.dumps(params)
        if 'access_token' in headers:
            headers = json.loads(headers)
            headers['access_token'] = self.get_token()

        # 对接口类型进行判断
        if method.upper() == 'GET':
            # 发送请求后，将结果赋值给res1，注意，get请求传参是用params
            res1 = requests.get(url = url, params = json.loads(params),headers = headers, verify=False)
            case_log_info(case_name, url, expect, res1)
           # case_log_base(case_name, url,params)  #打印用例基础信息——LYX
        else:
            # post请求传参用data
            res1 = requests.post(url = url, data = json.loads(params), headers = headers, verify=False)
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


    """获取token"""
    def login_flyme(self):
        url = 'https://api.meizu.com/oauth/token'
        data = {"scope": "trust",
                "remember_me": "mBj1R9Dg2CHmaenrXxOnanvSNfywuVZ5hHb4i9dFa2O2ZgOk88-mT_WuKgB0Peo9r6eT1hy7smsg1ORAJBMG_g6rfm8dMoMgvUagl4M4KPXWN9n46Alt8ZHREfv4cVe9UTq_2zyZuT44F8vFQ9ESpW0I3Vcc_zKYVSH-OwiSZyw*Uf2WxAO8SFhGSAwSQWPTI-XtAJO1p4C8WihXwwANTl_CmOAGjs7zRmEri9-VNo4vO0Xup-5y6bNm6n5tIsNxvmbfOZJg3WT5ohs0rNJV4GpJNcZuKELN3jbOaLmLNmvbyAVvqGus4the2XnpWWxF1ElMpLHvB42Eah1wfg0_r7A",
                "client_id": "KzA76k3lBCYDqKTy6VYvb9WR6QSUWVGJ",
                "client_secret": "G22l4Wj22DT9tKawFqi5x13w0TTalxxv",
                "info": "base",
                "grant_type": "remember_me",
                "sn": "S25QACP56DK2M",
                "imei": "861936030053089",
                "device_model": "M68B0",
                "lang": "zh_CN"}

        res = requests.post(url=url, data=data, verify=False)
        res1 = json.loads(res.text)['access_token']
        return res1

    def get_token(self):
        url = 'https://api.meizu.com/oauth/clients/uberauth'
        data = {"scope": "basic",
                "client_id": "com.meizu.mzsyncservice",
                "sn": "S25QACP56DK2M",
                "imei": "861936030053089",
                "device_model": "M68B0",
                "access_token": self.login_flyme(),
                "lang": "zh_CN"}


        res = requests.post(url=url, data=data, verify=False)
        res1 = json.loads(res.text)['access_token']
        return res1

    """获取结果中的value——LYX"""
    def get_request_value(self,case_name):
        res = self.get_result(case_name)
        result_expect = res[0]
        result_actual = json.loads(res[1].text)['value']
        result = [result_expect,result_actual]
        return result

    """获取接口返回的value-LJX"""
    def get_response_value(self,case_name):
        res = self.get_result(case_name)
        result_actual = json.loads(res[1].text)['value']
        return result_actual

    """获取接口返回的value-WMW"""
    def get_request_value2(self,case_name):
        res = self.get_result(case_name)
        result_expect = visit_webpage
        result_actual = json.loads(res[1].text)['value'][0]['value']
        result = [result_expect,result_actual]
        return result

    """获取接口返回的值-WMW"""
    def get_request_value3(self,case_name):
        res = self.get_result(case_name)
        result_expect = res[0]       #取表中的预期结果值not null
        result_actual = json.loads(res[1].text)['value'][0]     #取实际结果中的value值得第一条数据
        if result_actual != "":        #当实际结果值不为空时,赋值not null
            result_actual = "not null"
        result = [result_expect,result_actual]
        return result

    """获取接口返回的value-WMW"""
    def get_request_value4(self,case_name):
        res = self.get_result(case_name)
        result_expect = browser_setting_1
        result_actual = json.loads(res[1].text)['value'][5]['key']
        result = [result_expect,result_actual]
        return result

    """获取数据库的期望值和实际结果中的value值————LCM"""
    def get_request_value_DB(self, case_name):
        # 调用get_db_data方法获取出该条用例的预期结果值
        result_expect = self.get_db_data(case_name)
        # 调用get_actual_data方法获取出该条用例的实际结果值
        result_actual = self.get_actual_data(case_name,result_expect)
        result = [result_expect, result_actual]
        case_log_info_result(case_name,result_expect, result_actual)
        return result


    """获取期望值和实际结果中的value值————LCM"""
    def get_request_value_expect(self, case_name):
        res = self.get_result(case_name)
        # 取出预期结果值转换为int类型并赋值
        result_expect = res[0]
        # 调用get_actual_data方法获取出该条用例的实际结果值
        result_actual = self.get_actual_data(case_name,result_expect)
        result = [result_expect, result_actual]
        case_log_info_result(case_name,result_expect, result_actual)
        return result

    """判断当前执行的用例是否存在，存在则给当前执行的用例赋数据库的期望值————LCM"""
    def get_db_data(self,case_name):
        for i in range(len(case_name)):
            if case_name == "test013b":
                # 使用sql查询语句得到的值直接赋值给预期结果值
                result_expect = nav
                return result_expect
            if case_name == "test007b":
                result_expect = search
                return result_expect
            if case_name == "test002b":
                result_expect = novel
                return result_expect


    """判断当前执行的用例是否存在，存在则给当前执行的用例赋实际结果值————LCM"""
    def get_actual_data(self, case_name, result_expect):
        # 通过用例名称查询当前返回的实际结果值，根据实际结果取出该条用例需要的实际结果值
        res = self.get_result(case_name)
        for i in range(len(case_name)):
            if case_name == "test013b" and result_expect == "网址导航":
                # 获取实际结果值中的title值
                result_actual = json.loads(res[1].text)['value'][0]['title']
                return result_actual
            elif case_name == "test013a":
                # 获取实际结果中value的第一个值，且返回的数据是字典格式
                actual = json.loads(res[1].text)['value'][0]
                # 通过循环获取actual中key的title值
                result_actual = str({key: value for key, value in actual.items() if key == "title"})
                return result_actual

            if case_name == "test007b" and result_expect == "sm.cn":
                # 获取实际结果值中的home_page值
                result_actual = json.loads(res[1].text)['value']['engines'][0]['home_page']
                return result_actual

            elif case_name == "test007a":
                # 获取实际结果中value指定的值
                actual = json.loads(res[1].text)['value']['engines'][0]
                # 通过循环获取actual中value的值
                result_actual = str({key: value for key, value in actual.items() if value == 'sm.cn'})
                return result_actual

            if case_name == "test002b" and result_expect == "热门小说":
                # 获取实际结果值中的title值
                result_actual = json.loads(res[1].text)['value'][2]['data'][0]['data'][3]['title']
                return result_actual
            elif case_name == "test002a":
                # 获取实际结果中value指定的值
                actual = json.loads(res[1].text)['value'][2]['data'][0]['data'][3]
                # 通过循环获取actual中key的title值
                result_actual = str({key: value for key, value in actual.items() if key == "title"})
                return result_actual




