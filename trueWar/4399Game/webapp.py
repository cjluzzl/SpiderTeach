# -*- coding: utf-8 -*-
'''
Created on 2017年4月9日

@author: cjluzzl
'''
import web

urls = (
    '/','Index',
    '/(\d+)','Id',
)

db = web.database(
    dbn='mysql',
    host='127.0.0.1',
    port = 3306,
    user = 'root',
    pw = '142857',
    db = 'test',
    charset='utf8'
    )

render = web.template.render('templates')
class Index(object):
    def GET(self):
        data = db.query('select * from games')
        return render.index2(data)



class Id(object):
    def GET(self, myid):
        data = db.query('select * from games where id = %s' % myid)[0]
        return render.swf(data)
    
    
if __name__ == "__main__": 
    web.application(urls,globals()).run()
    
    
    