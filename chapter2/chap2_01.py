# -*- coding: utf-8 -*-
'''
Created on 2017年3月1日

@author: cjluzzl
'''
import re
import urllib2

def download(url):
    print "正在下载:",url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print '下载错误：',e.reason
        html = None
    return html 
url = "http://www.cjluzzl.cn"

html = download(url)

a = re.findall('<p class="x-box-summary">(.*?)</p>', html)
for i in a:
    print i