import logging
import os


"""获取当前文件的目录"""
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



"""获取其他几个主目录"""
data_path = os.path.join(project_path, 'data')
test_case_path = os.path.join(project_path, 'test')
result_path = os.path.join(project_path, 'result')



"""指定相关文件路径"""
report_dir = os.path.join(result_path, 'report.html')
log_dir = os.path.join(result_path, 'output.txt')
excel_dir = os.path.join(data_path, 'data_list.xlsx')



"""数据库相关配置信息"""
db_host_master = '172.16.178.242'
db_username_master = 'mysqluser'
db_password_master = 'mmsmysqluser'
db_table_master = 'test'


"""邮箱相关配置信息"""
email_sender = '浏览器接口测试'
# email_receiver = ['liudawei@meizu.com', 'lijingxin@meizu.com']
email_receiver = ['liudawei@meizu.com']
email_subject = 'InterFace_test_report'

smtp_server = 'idcmail.meizu.com'
smtp_sender = 'account@meizu.com'

send_email_switch = False


"""配置log相关信息"""
logging.basicConfig(level = logging.INFO,
                    format = '[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt = '%Y-%m-%d %H:%M:%S',
                    filename = log_dir,
                    filemode = 'a')
