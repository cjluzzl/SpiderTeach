# -*- coding: utf-8 -*-
'''
Created on 2017年3月1日

@author: cjluzzl
'''

from bs4 import BeautifulSoup

#不完整的html部分源码
bad_html = '<ul class=country><li>Area</li><li>Population</ul>'

#使用Beautiful Soup转化为soup格式
soup = BeautifulSoup(bad_html,'html.parser')

new_html = soup.prettify()

print '缺失标签的html文档转化后为:\n',new_html

ul = soup.find('ul',attrs={'class':'country'})
print 'find的查找结果为:',ul

ul = soup.find_all('ul',attrs={'class':'country'})
print 'find_all的查询结果为:',ul
