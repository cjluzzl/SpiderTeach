# -*- coding: utf-8 -*-
'''
Created on 2017年2月28日

@author: cjluzzl
'''
import itertools
from chap1_03 import download


def iteration():
    for page in itertools.count(120):
        url = 'http://www.cjluzzl.cn/article/{}'.format(page) + '.html'
        html = download(url)
        if html is None:
            # received an error trying to download this webpage
            # so assume have reached the last country ID and can stop downloading
            break
        else:
            # success - can scrape the result
            # ...
            pass


if __name__ == '__main__':
    iteration()