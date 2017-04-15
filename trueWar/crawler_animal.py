# -*- coding: utf-8 -*-
'''
Created on 2017年4月7日

@author: cjluzzl
'''
import urllib2
import urllib 
import re
import requests


def get_html(url):
    
    data = "User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
    page = urllib2.urlopen(url, data=data)
    html = page.read()
    return html
x = 0


def get_image_url(url , page_number):
    html = get_html(url)
    reg = r'<img src="(.*?)"'
    image_url_list = re.findall(reg, html)
    for image_url in image_url_list:
        print image_url
        global x
        x = x + 1
        urllib.urlretrieve(image_url, filename="D:/test/%s.jpg" % x)
    print u'%d下载任务完成' % page_number
if __name__ == "__main__":
    get_image_url("http://www.ivsky.com/tupian/tiankong_t811/",1)
    for i in range(2,40):
        get_image_url("http://www.ivsky.com/tupian/tiankong_t811/index_{0}.html".format(str(i)),i)



