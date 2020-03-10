import pandas as pd
from sqlalchemy import create_engine
import pymysql
# 初始化資料庫連線，使用pymysql模組  root為使用者名稱 tibame為密碼  127.0.0.1:3306為連線ip以及port jamesdb 為裡面的database
engine = create_engine('mysql+pymysql://root:tibame@127.0.0.1:3306/jamesdb')
# 讀取CSV檔案
data = pd.read_csv("./row_data.csv")
# 將新建的DataFrame儲存為MySQL中的資料表，不儲存index列   jamesdb為資料表名稱
data.to_sql('jamesdb', engine, index= False, if_exists='replace')
print("Write to MySQL successfully!")


#######if_exists可帶的三個參數
# fail: Raise a ValueError.
# replace: Drop the table before inserting new values.
# append: Insert new values to the existing table.






