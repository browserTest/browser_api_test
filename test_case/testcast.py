from test_case.basecase import BaseCase
import logging
import json
from data.getdb import *
from common.cast_log import *

class TestCase(BaseCase):

    # def test_get_http(self):
    #     result = self.get_request_code('test_get_http')
    #     self.assertEqual(result[0], result[1])
    #
    # def test_get_https(self):
    #     result = self.get_request_code('test_get_https')
    #     self.assertEqual(result[0], result[1])

    # 获取数据库查询结果——LYX
    def get_expect_db(self,sql):
        expect = self.db.query_all(sql)
        return expect

    # 获取数据库查询结果，取第一行第一个——LYX
    def get_expect_db_0_0(self,sql):
        expect = self.db.query_0_0(sql)
        return expect

    """test003黑白名单接口，code校验——LYX"""
    def test_get_test003(self):
        result = self.get_request_code('test003')
        self.assertEqual(result[0],result[1])

    """test003b黑白名单接口，数据库校验——LYX"""
    def test_get_test003b(self):
        result = self.get_response_value('test003b')  #取出接口返回结果的value值
        #查询数据库，找出政府白名单的第一个值
        db = self.get_expect_db_0_0("SELECT `value` FROM black_white_list WHERE `type` = 'from_zhengfu_white_list'")
        #对实际结果的value值做解析，找出政府白名单的值
        for i in range(len(result)):
            if result[i]['type'] == 'from_zhengfu_white_list':
                res = result[i]['value']
        case_log_result(db,res[0])
        self.assertEqual(db, res[0])

    """test011a网监黑名单，code校验——LYX"""
    def test_get_test011a(self):
        result = self.get_request_code('test011a')
        self.assertEqual(result[0],result[1])

    """test011b网监黑名单，value值校验——LYX"""
    def test_get_test011b(self):
        result = self.get_request_value('test011b')
        self.assertEqual(str(result[0]),str(result[1]))

    """test011c网监黑名单，db校验——LYX"""
    def test_get_test011c(self):
        # 取出接口返回结果的value值
        result = self.get_response_value('test011c')
        # 取出用例表中的data
        data = self.get_expect_data('test011c')
        #查询数据库，target=userId的所有值
        db = self.get_expect_db("select * from `wangjian_black_list` where target = '%s'" % (json.loads(data)['userId']))
        result_expect = 1 if db == () else 0
        case_log_result(result_expect, result['state'])
        self.assertEqual(result_expect, result['state'])

    """test016获取频道数据接口，code校验——LYX"""
    def test_get_test016(self):
        result = self.get_request_code('test016')
        self.assertEqual(result[0],result[1])

    """test021添加评论接口，code校验——LYX"""
    def test_get_test021(self):
        result = self.get_request_code('test021')
        self.assertEqual(result[0],result[1])

    """test020新消息提醒，code校验——LYX"""
    def test_get_test020(self):
        result = self.get_request_code('test020')
        self.assertEqual(result[0],result[1])

    """test004a——LJX"""
    def test004a(self):
        result = self.get_request_code('test004a')
        self.assertEqual(result[0], result[1])

    """test004b——LJX"""
    def test004b(self):
        result = self.get_response_value('test004b')
        print(result)
        for i in range(len(result)):
            if result[i]['type'] == 'android_uc':
                res = result[i]['value']
        self.assertEqual(android_uc, res)

    """test004b——LJX"""
    def test004c(self):
        result = self.get_response_value('test004c')
        for i in range(len(result)):
            if result[i]['type'] == 'android_360':
                res = result[i]['value']
        self.assertEqual(android_360, res)

    """test006a——LJX"""
    def test006a(self):
        result = self.get_request_code('test006a')
        self.assertEqual(result[0], result[1])

    """test006b——LJX"""
    def test006b(self):
        result = self.get_response_value('test006b')
        for i in range(len(result)):
            if result[i]['key'] == 'zhengfu_black_host':
                res = result[i]['value']
        self.assertEqual(zhengfu_black_host, res)

    """test010a——LJX"""
    def test010a(self):
        result = self.get_request_code('test010a')
        self.assertEqual(result[0], result[1])

    """test010b——LJX"""
    def test010b(self):
        result = self.get_response_value('test010b')
        res = tuple(result[0].values())
        self.assertEqual(search_suggest, res)

    """test002——LCM——校验实际结果与预期结果值都为200"""
    def test_get_test002(self):
        # 直接调用结果返回code值的方法，但预期结果值（expect）必须是200，该方法得到的实际结果值是code=200
        result = self.get_request_code('test002')
        # 断言预期结果与实际结果是否相等
        self.assertEqual(result[0], result[1])

    """test002a_LCM（校验实际结果与接口返回的参数预期结果值）"""
    def test_get_test002a(self):
        result = self.get_request_value_expect("test002a")
        print(result)
        self.assertEqual(str(result[0]), str(result[1]))

    """test002b_LCM（校验实际结果与数据库中查询的预期结果值）"""
    def test_get_test002b(self):
        result = self.get_request_value_DB("test002b")
        print(result)
        self.assertEqual(str(result[0]), str(result[1]))

    """test007——LCM"""
    def test_get_test007(self):
        result = self.get_request_code('test007')
        self.assertEqual(result[0],result[1])

    """test009——LCM"""
    def test_get_test009(self):
        # getUserData接口返回的结果是从大数据那边拿去的数据
        result = self.get_request_code('test009')
        self.assertEqual(result[0], result[1])

    """test013——LCM"""
    def test_get_test013(self):
        result = self.get_request_code('test013')
        self.assertEqual(result[0], result[1])

    """test019——LCM"""
    def test_get_test019(self):
        result = self.get_request_code('test019')
        self.assertEqual(result[0], result[1])

    """test012——WMW"""
    def test_get_test012(self):
        result = self.get_request_code('test012')
        self.assertEqual(result[0], result[1])

    """test018——WMW"""
    def test_get_test018(self):
        result = self.get_request_code('test018')
        self.assertEqual(result[0],result[1])

    """test014——WMW"""    #查询数据库
    def test_get_test014(self):
            result = self.get_request_code('test014')
            self.assertEqual(result[0], result[1])

    """test005——WMW"""    # 查询数据库
    def test_test005a(self):
        result = self.get_request_value2('test005')
        self.assertEqual(result[0], result[1])

    """test001——WMW"""    # 查询数据库
    def test_get_test001(self):
        result = self.get_request_value4('test001')
        self.assertEqual(result[0], result[1])

    """test023——WMW"""    #post请求
    def test_get_test023(self):
        result = self.get_request_code('test023')
        self.assertEqual(result[0],result[1])




