# coding: UTF-8
"""
需求要點：
1. 在 mac mini 的 Ubuntu 虛擬機安裝 MongoDB , 與建立一個登入使用者帳號 cchong0421
2. 在 mongodb 建立一個 Cashflow database
3. 建立一個 Tags Collection
4. 使用 insert_one 新增一個 document ，資料內容為 {'TagId': 'A01', 'TagName': 'DOTNET'}
5. 查詢 Tags Collection 的所有資料並顯示
6. 將 Collection 中的資料刪除
7. 關閉 mongodb 連線
"""

import pymongo
import time


def ShowRecord(records):
    for item in records:
        print(item)


# Connect to MongoDB
mongoClient = pymongo.MongoClient("mongodb://cchong0421:sit@10.211.55.6:27017")

# open db and select collection
mydb = mongoClient.get_database('CashflowDB')
tags = mydb.get_collection('Tags')

# insert document to collection
tags.insert_one({'TagId': 'A01', 'TagName': 'DOTNET',
                'Timestamp': time.time()})

tags.insert_one({'TagId': 'B01', 'TagName': 'PYTHON',
                'Timestamp': time.time()})
tags.insert_one({'TagId': 'C01', 'TagName': 'JAVA',
                'Timestamp': time.time()})

# display all documents
ShowRecord(tags.find())

# 測試完畢，將 Collection 中的資料刪除
tags.drop()

# 關閉 mongodb 連線
mongoClient.close()
