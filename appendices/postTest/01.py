# -*- coding: utf-8 -*-
'''
Created on 2017年3月12日

@author: cjluzzl
'''
import urllib
import urllib2


url = 'http://www.thsrc.com.tw/tw/TimeTable/SearchResult'

header = {'Origin':'http://www.thsrc.com.tw',
          'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
postData = urllib.urlencode([
               ('StartStation', '2f940836-cedc-41ef-8e28-c2336ac8fe68'),
               ('EndStation', '38b8c40b-aef0-4d66-b257-da96ec51620e'),
               ('SearchDate','2017/03/12'),
               ('SearchTime','19:30'),
               ('SearchWay','DepartureInMandarin')             
                             ])
req = urllib2.Request(url,headers=header,data=postData.encode('utf8'))

html = urllib2.urlopen(req).read()
print unicode(html,'utf8')
