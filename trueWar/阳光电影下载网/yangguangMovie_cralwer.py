# -*- coding: utf-8 -*-
'''
Created on 2017年4月8日

@author: cjluzzl
'''
import urllib2
import re
import urlparse
from bs4 import BeautifulSoup
import MySQLdb
def save_into(title,span,href):
    connection = MySQLdb.connect(host='127.0.0.1',user='root',
                            passwd='142857',db='test',charset='utf8')
    try:
            #获取回话指针
        cursor=connection.cursor() 
            #创建SQL语句
        span = str(span).replace('\'','\"')
        print span 
        sql = "insert into `movie`(title,content,link) values('%s','%s','%s')" % (title,span,href)
            #执行SQL语句
        print sql
        cursor.execute(sql)
            #提交
        connection.commit()
    finally:
        cursor.close()

def get_index_all_url(url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
    header = {"User-Agent": user_agent}
    req = urllib2.Request(url, headers=header)
    html = urllib2.urlopen(req).read()
    #reg_new_170 = r'<div class="co_content2">(.*?)</div>'
    reg_url = r'<a (.*?)</a>'
    all_url = re.findall(reg_url, html)
    true_url = []
    for i in all_url:
        if "game" not in i and 'index' not in i:
            true_url.append(i)
    
    reg_name = r'>(.+)'
    reg_href = r'href="(.+)"'
    crawler_queue = []
    for i in true_url:
        #print i.decode('gbk').encode('utf8')
        name = re.findall(reg_name, i)
        href = re.findall(reg_href, i)
        if href == []:
            href = re.findall(r"href='(.+)'", i)
        #print '视频名:',name[0].decode('gbk').encode('utf8'),'视频链接',href
        crawler_queue.append(href[0])
    
    return crawler_queue    
    print 'over2'
    #print html.decode("gbk").encode("utf8")


def download_movie_url(base,url):
    try:
        url = urlparse.urljoin(base, url)
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
        header = {"User-Agent": user_agent}
        req = urllib2.Request(url, headers=header)
        html = urllib2.urlopen(req).read()
        html = html.decode('gbk').encode('utf8')
        soup = BeautifulSoup(html, 'html.parser')
        title = re.findall(r'<title>(.+?)</title>', str(soup.find('title')))
        span = soup.find_all("span", attrs={'style':'FONT-SIZE: 12px'})
        ftp = soup.find('td', attrs={'style':'WORD-WRAP: break-word','bgcolor':'#fdfddf'})
        href = re.findall(r'<a href="(.+?)"', str(ftp))
        if href:
            #print 'title is:',title[0], 'span is ', span[0],'href is ',href[0]
            save_into(title=title[0],span=span[0],href=href[0])
    except Exception as e:
        print e

if __name__ == "__main__":
    url = "http://www.ygdy8.com"
    download_queue = get_index_all_url(url)
    for i in download_queue:
        if 'com' in i and 'net' in i and 'index.html' in i:
            continue
        else:
            download_movie_url(base=url, url=i)
        
    