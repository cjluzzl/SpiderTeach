# -*- coding: utf-8 -*-
'''
Created on 2017年4月9日

@author: cjluzzl
'''

import urllib
url = "http://szhong.4399.com/4399swf/upload_swf/ftp21/gamehwq/20170401/7.swf"

urllib.urlretrieve(url,"地城勇士冒险2中文版.swf".decode('utf8').encode('gbk'))
print 'over'