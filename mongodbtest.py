# coding: UTF-8

import pymongo
from config import MongoDBConnectionString

print(MongoDBConnectionString)

myclient = pymongo.MongoClient(MongoDBConnectionString)
mydb = myclient["CashflowDB"]

coll = mydb.get_collection('Users')

# 寫入單筆資料
# UserA = { 'Id': f'steven--0001', 'Name': 'cchong0421', 'IsAdmin': True }
# x = coll.insert_one(UserA)

# 寫入多筆資料
# userlist = []
# for num in range(1,200):
#     UserA = { 'Id': f'steven--{num:04}', 'Name': 'cchong0421', 'IsAdmin': True }
#     userlist.append(UserA)
# x = coll.insert_many(userlist)

# 使用 Regex 查詢資料
myquery = { "Id": { "$regex": "38$" } }
records = coll.find(myquery)

for item in records:
    print(item)
myclient.close()