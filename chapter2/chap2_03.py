# -*- coding: utf-8 -*-
'''
Created on 2017年3月1日

@author: cjluzzl
'''

import lxml.html

bad_html = '<ul class=country><li>Area</li><li>Population</ul>'

tree = lxml.html.fromstring(bad_html)

new_html = lxml.html.tostring(tree,pretty_print=True)
print '缺失标签的html文档转化后为:\n',new_html