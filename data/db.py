import pymysql
from config.config import *


class DB():

    """连接db"""
    def __init__(self):
        self.conn = pymysql.connect(host = db_host_master,
                                    user = db_username_master,
                                    passwd = db_password_master,
                                    db = db_table_master,
                                    charset = 'utf8')

        self.cur = self.conn.cursor()


    """关闭其连接"""
    def __del__(self):
        self.cur.close()
        self.conn.close()


    """获取查询结果"""
    def query(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result[0][1]


    """提交sql"""
    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logging.info(str(e))









