from config.config import *

def case_log_info(name, url,expect_result, actual_result,date = {}):
    logging.info("测试用例：{}".format(name))
    logging.info("url:{}".format(url))
    logging.info("请求参数：{}".format(date))
    logging.info("期望结果：{}".format(expect_result))
    logging.info("实际结果：{}".format(actual_result))
    logging.info("")
