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
        android_uc = self.db.query_0_0("SELECT VALUE FROM `base_data` WHERE TYPE = 'android_uc'")
        for i in range(len(result)):
            if result[i]['type'] == 'android_uc':
                res = result[i]['value']
        self.assertEqual(android_uc, res)

    """test004b——LJX"""
    def test004c(self):
        result = self.get_response_value('test004c')
        android_360 = self.db.query_0_0("SELECT VALUE FROM `base_data` WHERE TYPE = 'android_360'")
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
        zhengfu_black_host = self.db.query_0_0("SELECT VALUE FROM `bloom_config` WHERE `KEY` = 'zhengfu_black_host'")
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
        search_suggest = self.db.query_0("SELECT keyword,url,weight FROM search_suggest")
        res = tuple(result[0].values())
        self.assertEqual(search_suggest, res)

    """test015a——LJX"""
    def test015a(self):
        result = self.get_request_code('test015a')
        self.assertEqual(result[0], result[1])

    """test015b——LJX"""
    def test015b(self):
        result = self.get_response_value('test015b')
        self.assertIsNotNone(result)

    """test017a——LJX"""
    def test017a(self):
        result = self.get_request_code('test017a')
        self.assertEqual(result[0], result[1])

    """test017b——LJX"""
    def test017b(self):
        result = self.get_response_value('test017b')
        self.assertIsNotNone(result)

    """test024a——LJX"""
    def test024a(self):
        result = self.get_request_code('test024a')
        self.assertEqual(result[0], result[1])

    """test024b——LJX"""
    def test024b(self):
        result = self.get_response_value('test024b')
        self.assertIsNotNone(result)


    """test012——WMW"""      #校验--获取城市信息--实际结果与接口返回的参数预期结果值
    def test_get_test012(self):
        result = self.get_request_code('test012')
        self.assertEqual(result[0], result[1])

    """test018——WMW"""    #校验--推荐频道资讯流--实际结果与接口返回的参数预期结果值
    def test_get_test018(self):
        result = self.get_request_code('test018')
        self.assertEqual(result[0],result[1])

    """test014——WMW"""    #未查询数据库---搜索热词,直接校验接口返回的数据是否为空
    def test_get_test014(self):
            result = self.get_request_value3('test014')
            self.assertEqual(result[0], result[1])

    """test005——WMW"""    # 查询数据库--基础数据的value值与实际结果value值对比
    def test_test005(self):
        result = self.get_request_value2('test005')
        self.assertEqual(result[0], result[1])

    """test001——WMW"""    # 查询数据库--配置项--有待更改
    def test_get_test001(self):
        result = self.get_request_value4('test001')
        self.assertEqual(result[0], result[1])

    """test023——WMW"""    #校验--获取我的消息--post请求接口返回的code值与期望结果值
    def test_get_test023(self):
        result = self.get_request_code('test023')
        self.assertEqual(result[0],result[1])




    """test002_LCM————校验首页导航\背景图\个人中心banner(http://bro.flyme.cn/card/get)实际结果和预期结果中的code值"""
    def test_get_test002(self):
        result = self.get_request_code("test002")
        self.assertEqual(result[0],result[1])

    """test002a_LCM————校验首页导航\背景图\个人中心banner实际结果与接口返回的参数预期结果值"""
    def test_get_test002a(self):
        result = self.get_request_value_expect("test002a")
        self.assertEqual(str(result[0]), str(result[1]))

    """test002b_LCM————校验校验首页导航\背景图\个人中心banner实际结果与数据库中查询的预期结果值"""
    def test_get_test002b(self):
        result = self.get_request_value_DB("test002b")
        self.assertEqual(str(result[0]), str(result[1]))

    """test007_LCM————校验搜索引擎接口实际结果和预期结果中的code值"""
    def test_get_test007(self):
        result = self.get_request_code("test007")
        self.assertEqual(result[0], result[1])

    """test007a_LCM————校验搜索引擎接口实际结果与接口返回value中搜索引擎的预期结果值"""
    def test_get_test007a(self):
        result = self.get_request_value_expect("test007a")
        self.assertEqual(result[0], result[1])

    """test007b_LCM————校验搜索引擎接口实际结果与数据库中查询的预期结果值"""
    def test_get_test007b(self):
        result = self.get_request_value_DB("test007b")
        self.assertEqual(result[0], result[1])

    """test009_LCM————校验负一屏的list.do接口实际结果和预期结果中的code值"""
    def test_get_test009(self):
        result = self.get_request_code("test009")
        self.assertEqual(result[0], result[1])

    """test013_LCM————校验负一屏的list.do接口实际结果和预期结果中的code值"""
    def test_get_test013(self):
        result = self.get_request_code("test013")
        self.assertEqual(result[0], result[1])

    """test013a_LCM————校验负一屏的list.do接口实际结果与接口返回的value预期结果值"""
    def test_get_test013a(self):
        result = self.get_request_value_expect("test013a")
        self.assertEqual(result[0], result[1])

    """test013b_LCM————校验负一屏的list.do接口实际结果与数据库中查询的预期结果值"""
    def test_get_test013b(self):
        result = self.get_request_value_DB("test013b")
        self.assertEqual(result[0], result[1])

    """test019_LCM————校验非推荐频道资讯流接口实际结果和预期结果中的code值"""
    def test_get_test019(self):
        result = self.get_request_code("test019")
        self.assertEqual(result[0], result[1])

    """test022_LCM————校验我的评论接口实际结果和预期结果中的code值"""
    def test_get_test022(self):
        result = self.get_request_code("test022")
        self.assertEqual(result[0], result[1])

