# -*- coding:utf-8 -*-
'''
Created on 2017年2月28日

@author: cjluzzl
'''
import urllib2

def download(url):
    print "正在下载:",url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print '下载错误：',e.reason
        html = None
    return html
