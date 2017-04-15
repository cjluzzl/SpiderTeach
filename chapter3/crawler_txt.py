# -*- coding: utf-8 -*-
'''
Created on 2017年3月11日

@author: cjluzzl
'''
import re
import urllib2
import time

def download(url):
    print u'正在下载',url
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    header = {'User-Agent':user_agent}
    request = urllib2.Request(url,headers=header)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print e.reason
    
    return html

reg = r'<span>(.*?)</span>'

file = open("D:/Download/20170311.txt",'wb')

html_content = download("http://www.qiushibaike.com")

con = re.findall(reg, html_content)

con_len = len(con)

for i in range(con_len):
    print con[i]
    file.write(con[i])
    file.write('\n')


file.close()
print u'写入文件完毕'    
    
    

