# -*- coding: utf-8 -*-
'''
Created on 2017年4月9日

@author: cjluzzl
'''

# -*- coding:utf-8 -*-

import urllib
import urllib2
import json
from Tkinter import *
import sys
reload(sys)


print sys.getdefaultencoding()

def translation():
    content=text1.get(1.0,END)   #获取输入的输入
    text2.delete(0.0, END)
    if content=='':
        content=u"简约"
    
    print content
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    # '''
    # head={}
    # head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
    # '''
    data={}
    data['type']='AUTO'
    data['i']=content.decode('utf8')
    data['doctype']='json'
    data['xmlVersion']='1.8'
    data['keyfrom']='fanyi.web'
    data['ue']='UTF-8'
    data['action']='FY_BY_CLICKBUTTON'
    data['typoResult']='true'
    data=urllib.urlencode(data).encode('utf-8')

    req=urllib2.Request(url,data)
    req.add_header('User_Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')

    response=urllib2.urlopen(req)
    html=response.read().decode('utf-8')
    target=json.loads(html)#target['translateResult'][0][0]['tgt']
    cloum=1
    for i in target['translateResult']:
        for j in i:
            #y = target['smartResult']['entries'][2]
            #print y
            text2.insert(INSERT,j['tgt']+'\n')
            #text2.insert(END,'\n'+'-'*20)
            text2.insert(INSERT,target['smartResult']['entries'][1])
            #print j['tgt']
        cloum+=1
    #text2.insert(INSERT,target['translateResult'][0][0]['tgt'])

root = Tk()
label=Label(root,text=u"忘仙中英文翻译软件V1.0",fg= "blue",font=(u"黑体", 13, "bold"))
text1=Text(root,width=20,height=5,font=(u"黑体", 13, "bold"))
text2=Text(root,width=20,height=5,font=(u"黑体", 13, "bold"))
text2.insert(INSERT, u"请再上面的文本框输入您想翻译的文字")
button=Button(text= u"开始翻译",fg="black",command=translation)
label.pack()
text1.pack()
text2.pack()
button.pack()

mainloop()
