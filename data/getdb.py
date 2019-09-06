from data.db import DB
from config.config import *



db1 = DB()


# db1.exec("update test set name = 2 where name = 1")

# db1.exec("insert into test values (1, 4, 1, 1, 1, 1, 1)")

# logging.info(db1.query("select * from test where sex = 1"))

android_uc = db1.query_0_0("SELECT VALUE FROM `base_data` WHERE TYPE = 'android_uc'")



