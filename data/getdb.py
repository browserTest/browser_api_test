from data.db import DB
from config.config import *



db1 = DB()


# db1.exec("update test set name = 2 where name = 1")

# db1.exec("insert into test values (1, 4, 1, 1, 1, 1, 1)")

# logging.info(db1.query("select * from test where sex = 1"))








#visit_webpage = db1.query_0_0("select value from `base_data` where TYPE = 'visit_webpage'")

#browser_setting_1 = db1.query_0_0("SELECT VALUE FROM `browser_setting` WHERE `key`='useConfigReaderJs'")



title = db1.query_all("select * from card_item where title='热门小说'")
novel = title[0][3]
home_page = db1.query_all("select * from search_engine_unit where home_page='sm.cn'")
search = home_page[0][4]
navigation = db1.query_all("select * from site_square_group LEFT JOIN site_square_unit on site_square_group.id = site_square_unit.group_id where title = '网址导航' and group_id = 5")
nav = navigation[0][7]


