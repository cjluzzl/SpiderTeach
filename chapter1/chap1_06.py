# -*- coding: utf-8 -*-
'''
Created on 2017年2月28日

@author: cjluzzl
'''

import robotparser
from pip.download import user_agent

rp = robotparser.RobotFileParser()
rp.set_url("http://www.cjluzzl.cn/robots.txt")
rp.read()
url = 'http://www.cjluzzl.cn'
user_agent = 'BadCrawler'
print rp.can_fetch(user_agent, url)

user_agent = 'GoodCrawler'
print rp.can_fetch(user_agent, url)