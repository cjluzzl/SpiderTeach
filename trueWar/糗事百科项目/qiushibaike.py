# -*- coding: utf-8 -*-
'''
Created on 2017年3月4日

@author: cjluzzl
'''

import re
import urllib2
import urllib
import os

def download(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    header = {'User-Agent':user_agent}
    request = urllib2.Request(url,headers=header)
    print '正在下载',url
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print '打开网址 ',url,e.reason    
    
    return html
    
file = open(u"糗事百科.txt",'w+')#创建本地文件
html = download('https://www.qiushibaike.com') #执行download函数下载HTML
if html != None:
    con = re.findall('<span>(.*?)</span>',html)#获取段子内容
    total_count = len(con)#计算段子总数
    
    
    print '一共有',total_count,'条'
    file.write('一共有'+str(total_count)+'条\n')
    for i in range(1,total_count):
        print '\n这是第',i,'条'
        file.write('\n这是第'+str(i)+'条\n')
        if '<br/><br/>' in con[i]:#<br/>标签转换行
            con[i]=con[i].replace('<br/><br/>','\n')
        if '<br/>' in con[i]:#<br/>标签转换行
            con[i]=con[i].replace('<br/>','\n')
        print con[i]
        if "<img " in con[i]:#判断是否为图片段子
            print u'现在开始爬取图片'
            #imageUrl = con[i][con[i].find('src=')+5:con[i].find('.jpg')+4]
            imageUrl = re.findall('src="(.+?\.jpg)',con[i])
            title = re.findall('alt="(.*?)"',con[i])
            title = str(title[0])
            print title
            filename="D:/" + title +".jpg"
            #print filename
            try:
                urllib.urlretrieve(imageUrl[0],filename=unicode(filename,'utf8'))
            except IOError as a:
                print 'error'
        else:#文字段子写入文件
            file.write(con[i]+'\n')
    
    
else:
    print '未获取到指定内容，请检查网址无误后重试'
file.close()
