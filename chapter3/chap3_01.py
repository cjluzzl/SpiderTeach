# -*- coding: utf-8 -*-
'''
Created on 2017年3月4日

@author: cjluzzl
'''
from pymongo import MongoClient

client = MongoClient('localhost',27017)

url = "http://www.cjluzzl.cn"

html = '...'

db = client.cache
collection = db.cache

collection.insert({'url':url,'html':html})

for item in collection.find():
    print item
