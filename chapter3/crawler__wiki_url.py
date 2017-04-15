# -*- coding: utf-8 -*-
'''
Created on 2017年3月15日

@author: cjluzzl
'''
# -*- coding: utf-8 -*-
'''
Created on 2017年3月12日

@author: cjluzzl
'''
import re
import MySQLdb
from bs4 import BeautifulSoup as bs
import urllib2

url = "https://en.wikipedia.org/wiki/Main_Page"

html = urllib2.urlopen(url).read().decode('utf8')

soup = bs(html,'html.parser')

listURL = soup.findAll("a",href=re.compile(r"^/wiki/"))

#获取数据库连接
connection = MySQLdb.connect(host='127.0.0.1',user='root',
                            passwd='142857',db='wikiurl',charset='utf8')
#遍历爬取到的所有链接，剔除图片链接
for url in listURL:
    if not re.search(r"\.(jpg|JPG)$",url['href']):
        print url.get_text(),'<=====>','https://en.wikipedia.org' + url['href']
        
        try:
            #获取回话指针
            cursor=connection.cursor() 
            #创建SQL语句
            sql = 'insert into `urls`(urlname,urlhref) values(%s,%s)'
            url_write = 'https://en.wikipedia.org' + url['href']
            #执行SQL语句
            cursor.execute(sql,(url.get_text(),url_write))
            #提交事务
            connection.commit()
        except Exception as e:
            print '出现错误',e
            #出现异常后事务的回滚
            connection.rollback()
        finally:
            cursor.close()
print '下载完成'