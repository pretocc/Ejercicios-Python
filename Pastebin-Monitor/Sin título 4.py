# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:00:23 2015

@author: Preto
"""

import httplib2
from bs4 import BeautifulSoup

http = httplib2.Http()
status, response = http.request('http://pastebin.com/archive')

for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):

    if link.has_attr('href'):
        print link['href']
