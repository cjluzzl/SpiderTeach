# -*- coding: utf-8 -*-
'''
Created on 2017年3月2日

@author: cjluzzl
'''
import re
import urllib2
import urlparse

def download(url):
    print '正在下载',url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print '下载错误',e.reason
        html = None
    return html
        


def link_crawler(seed_url, link_regex):
    """从给定的URL中按照正则去找链接
    """
    crawl_queue = [seed_url] #url的下载队列
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        #URL过滤器
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    #添加到下载队列中
                    crawl_queue.append(link)


def get_links(html):
    """返回从html文件中获取的链接列表 
    """
    # 从网页中获取所有链接
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # 返回所有符合规则的链接
    return webpage_regex.findall(html)


if __name__ == '__main__':
    link_crawler('http://www.cjluzzl.cn', '/(article)/')