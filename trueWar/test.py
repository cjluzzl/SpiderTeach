# -*- coding: utf-8 -*-
'''
Created on 2017年4月8日

@author: cjluzzl
'''
import re 
import urllib2
import urlparse
from bs4 import BeautifulSoup
import MySQLdb


def save_into(title,span,href):
    connection = MySQLdb.connect(host='127.0.0.1',user='root',
                            passwd='142857',db='test',charset='utf8')
    try:
            #获取回话指针
        cursor=connection.cursor() 
            #创建SQL语句
        sql = "insert into `movie`(title,content,link) values('%s',%s,'%s')" % (title,repr(str(span)),href)
            #执行SQL语句
        print sql
        cursor.execute(sql)
            #提交
        connection.commit()
    finally:
        cursor.close()
        
if __name__ == "__main__":
    span = """<span style="FONT-SIZE: 12px"><td>
<p>奇机少年][BD-RMVB.720p.中英双字][2017年科幻动作]<br/><br/><img alt="" border="0" onclick="if(this.width&gt;screen.width-461) window.open('http://image18.poco.cn/mypoco/myphoto/20170227/22/183365877201702272206003921147208108_000.jpg');" src="http://image18.poco.cn/mypoco/myphoto/20170227/22/183365877201702272206003921147208108_000.jpg"/><br/><br/>◎译　　名　奇机少年<br/>◎片　　名　iBoy<br/>◎年　　代　2017<br/>◎国　　家　英国<br/>◎类　　别　动作/科幻/犯罪/惊悚<br/>◎语　　言　英语<br/>◎字　　幕　中英双字幕<br/>◎IMDb评分  6.0/10 from 6,576 users<br/>◎文件格式　BD-RMVB<br/>◎视频尺寸　1280 x 720<br/>◎文件大小　1CD<br/>◎片　　长　90分钟<br/>◎导　　演　亚当·兰道 Adam Randall<br/>◎主　　演　比尔·米尔纳 Bill Milner<br/>　　　　　　麦茜·威廉姆斯 Maisie Williams<br/>　　　　　　米兰达·理查森 Miranda Richardson<br/>　　　　　　罗里·金奈尔 Rory Kinnear<br/>　　　　　　乔丹·博尔格 Jordan Bolger<br/>　　　　　　查理·帕尔默·罗斯韦尔 Charley Palmer Rothwell<br/>　　　　　　阿明·卡丽玛 Armin Karima<br/>　　　　　　麦凯尔·戴维 McKell David<br/>　　　　　　沙奎尔·阿里-耶布阿 Shaquille Ali-Yebuah<br/>　　　　　　艾蒙·汉道奇 Aymen Hamdouchi<br/>　　　　　　利昂·阿诺 Leon Annor<br/>　　　　　　佩踹斯·琼斯 Petrice Jones<br/>　　　　　　卡梅伦·杰克 Cameron Jack<br/><br/>◎简　　介<br/><br/>　　一次事故过后，汤姆从昏迷中醒来，发现他的智能手机的碎片已经嵌入他的头部，这也让他意外地获得了能够凭借意念黑入任何一个电子设备的奇异能力。想要回到原来的普通人的生活已经不可能，于是他化身网络黑客“iBOY”，用自己的超能力行使正义。<br/><br/><img alt="" border="0" onclick="if(this.width&gt;screen.width-461) window.open('http://image18.poco.cn/mypoco/myphoto/20170228/22/183365877201702282219563568887364362_002.jpg');" src="http://image18.poco.cn/mypoco/myphoto/20170228/22/183365877201702282219563568887364362_002.jpg"/></p>
<p> </p>"""
    print span
    title = '2016年动作喜剧《真田十勇士》BD日语中字迅雷下载_阳光电影_电影天堂'
    href = 'ftp://ygdy8:ygdy8@yg42.dydytt.net:7006/[阳光电影www.ygdy8.com].真田十勇士.BD.720p.日语中字.mkv'
    save_into(title, span, href)
    

