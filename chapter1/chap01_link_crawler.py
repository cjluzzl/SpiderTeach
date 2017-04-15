# -*- coding: utf-8 -*-
'''
Created on 2017年3月2日

@author: cjluzzl
'''
import re
import urllib2
def download(url):
    print '正在下载',url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print '下载错误',e.reason
        html = None
    return html
        


def link_crawler(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url] # the queue of URL's to download
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        # filter for links matching our regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                # add this link to the crawl queue
                crawl_queue.append(link)


def get_links(html):
    """Return a list of links from html 
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)


if __name__ == '__main__':
    link_crawler('http://www.cjluzzl.cn', '/(article)/')