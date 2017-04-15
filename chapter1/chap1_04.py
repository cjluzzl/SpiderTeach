# -*- coding: utf-8 -*-
'''
Created on 2017年2月28日

@author: cjluzzl
'''
import urllib2
import re
from chap1_03 import download

def crawl_sitemap(url):
    sitemap = download(url)
    
    links = re.findall('<loc>(.*?)</loc>',sitemap)
    for link in links:
        html = download(link)

if __name__ == '__main__':
    crawl_sitemap('http://www.cjluzzl.cn/sitemap.xml')