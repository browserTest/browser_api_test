from config.config import *

def case_log_info(name, url,expect_result, actual_result,date = {}):
    logging.info("测试用例：{}".format(name))
    logging.info("url:{}".format(url))
    logging.info("请求参数：{}".format(date))
    logging.info("期望结果：{}".format(expect_result))
    logging.info("实际结果：{}".format(actual_result))
    logging.info("")


#打印用例基本信息——LYX
def case_log_base(name, url,date = {}):
    logging.info("测试用例：{}".format(name))
    logging.info("url:{}".format(url))
    logging.info("请求参数：{}".format(date))

#打印用例期望值和实际结果——LYX
def case_log_result(expect_result, actual_result):
    logging.info("期望结果：{}".format(expect_result))
    logging.info("实际结果：{}".format(actual_result))
    logging.info("")


"""打印当前执行用例的期望值和实际结果值——LCM"""
def case_log_info_result(name, result_expect, result_actual):
    logging.info("测试用例：{}".format(name))
    logging.info("期望结果：{}".format(result_expect))
    logging.info("实际结果：{}".format(result_actual))
    logging.info("")