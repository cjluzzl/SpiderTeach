# -*- coding: utf-8 -*-
'''
Created on 2017年3月11日

@author: cjluzzl
'''

import re
import urllib
import urllib2
import time


def download(url):
    print u"正在打开",url
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    header = {'User-Agent':user_agent}
    request = urllib2.Request(url,headers=header)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print u'打开网址',url,' ',e.reason
    
    return html

if __name__ == "__main__":
    #url = raw_input('请输入网址链接')
    reg = r'<img (.*?)>'
    html = download('http://www.qiushibaike.com/pic')
    SourceURL = re.findall(reg,html)
    #image_url = []
    #image_title = []
    for i in range(len(SourceURL)-1):
        regUrl = r'src="(.+?\.jpg)"'
        image_url = re.findall(regUrl, SourceURL[i])
        if re.findall(regUrl, SourceURL[i]):
            reg_image_title =  r'alt="(.*?)"'   
            image_title = re.findall(reg_image_title, SourceURL[i])
            filename = "D:/Download/pic/" + image_title[0]+".jpg"
            print filename
            print image_url
            if image_url:
                try:    
                    time.sleep(3)
                    urllib.urlretrieve(image_url[0],filename=unicode(filename,'utf8'))
                except IOError as e:
                    print 'error'
    print '保存完毕'