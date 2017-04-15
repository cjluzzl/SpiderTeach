# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import requests


#url = "https://www.hanhanfilm.com/film/source"

url2 = 'https://www.baidu.com'
data = "User-Agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36'"


html = urllib2.urlopen(url2,data=data).read()

print html