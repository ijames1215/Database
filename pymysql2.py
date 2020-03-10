import pymysql
import pandas as pd
import numpy as np
data = pd.read_csv("./YoutubeMerge.csv")
data_set = []
#########取得個欄位資料至list字串data_set########
for i in range(len(data['channelName'])):
    mydata = (data['channelName'][i],data['class'][i],data['fans'][i],data['channel'][i],data['like'][i])
    data_set.append(mydata)
########連線mysql 127.0.0.1 為連線ip root為使用者名稱  tibame為帳號 jamesdb為資料集名稱
db = pymysql.connect("127.0.0.1","root","tibame",'jamesdb')
#########cursor為使用SQL語法~~~~~~~~~~~
cursor = db.cursor()

cursor.execute("CREATE DATABASE testdb")
cursor.execute("CREATE TABLE testdb (channelName VARCHAR(255),class VARCHAR(255),fans VARCHAR(255),channel VARCHAR(255))")

sqlStuff = "INSERT INTO testdb (channelName,class,fans,channel) VALUES (%s,%s,%s,%s)"
cursor.executemany(sqlStuff, data_set)
######開始執行
db.commit()