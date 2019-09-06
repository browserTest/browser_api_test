from data.db import DB
from config.config import *


db1 = DB()


# db1.exec("update test set name = 2 where name = 1")

# db1.exec("insert into test values (1, 4, 1, 1, 1, 1, 1)")

#logging.info(db1.query("select * from test where sex = 1"))


# 查询数据库表card_item 从DB中获取首页导航网站在数据库中title的值
title = db1.query_NOVEL("select * from card_item where title = '热门小说'")
print(title)




