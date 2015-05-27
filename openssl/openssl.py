# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:00:23 2015

@author: Preto
"""

import os

filect = 'text.out'
filept = ''
pwd = 'abc123'


fo = open('cifrados', 'r')

for c in fo:
    filept = c[0:-1]+".txt"
    cmd = 'openssl %s -d -in %s -out %s -k %s' % (c[0:-1], filect, filept, pwd)
    os.system(cmd)
