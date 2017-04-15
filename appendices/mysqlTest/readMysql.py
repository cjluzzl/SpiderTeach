# -*- coding: utf-8 -*-
'''
Created on 2017年3月12日

@author: cjluzzl
'''

import MySQLdb

con = MySQLdb.connect(host='127.0.0.1',
                      port = 3306,
                      user = 'root',
                      passwd = '142857',
                      db = 'user',
                      charset='utf8')

cursor = con.cursor()

sql = 'select * from user_table'

cursor.execute(sql)

info = cursor.fetchall()

for i in info:
    print i
    
print cursor.rowcount


cursor.close()
con.close()





















