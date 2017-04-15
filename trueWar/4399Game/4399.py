# -*- coding: utf-8 -*-
'''
Created on 2017年4月9日

@author: cjluzzl
'''

import re
import urllib2
import urllib
import urlparse
import MySQLdb

host = 'http://www.4399.com'


class Sql(object):
    conn = MySQLdb.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '142857',
        db = 'test',
        charset = 'utf8'
        )
    def adddata(self,name,gameurl,imageurl):
        cursor = self.conn.cursor()
        sql = "insert into games (name,gameurl,imageurl) values('%s','%s','%s')" % (name,gameurl,imageurl)
        cursor.execute(sql)
        cursor.close()
        self.conn.commit()

def get_list(url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
    head = {"User-Agent":user_agent}
    req = urllib2.Request(url,headers=head)
    html = urllib2.urlopen(req).read()
    html = html.decode('gbk').encode('utf8')
    print html
    reg = r"<li><a href='(.+)'><img lzimg='1' lz_src='(.+)'  alt='(.+)'/>(.+)</a></li>"
    #reg = r'<li><a href="(.+)"><img alt="(.+)"  src="(.+)"><b>(.+)</b>'
    mylist = re.findall(reg, html)
    return mylist

def getswf(url):
    url = urlparse.urljoin(host, url)
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
    head = {"User-Agent":user_agent}
    req = urllib2.Request(url,headers=head)
    html = urllib2.urlopen(req).read()
    html = html.decode('gb2312').encode('utf8')
    reg_server = r'/js/server(.+?).js'
    server =  re.findall(reg_server, html)[0]
    reg_game = r'strGamePath="(.+?)"'
    game = re.findall(reg_game,html)[0]
    return "http://{0}.4399.com/4399swf{1}".format(server,game)
    
mysql = Sql()
for i in get_list('http://www.4399.com/flash_fl/more_2_2.htm'):
    try:
        swf_url = getswf(i[0])
        mysql.adddata(i[3], swf_url, i[1])
        print i[3],i[1],swf_url
    except Exception as e:
        open('log.txt','a+').write(i[0]+'\n')
    

print 'over'
