# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:41:18 2015

@author: Preto
"""

from bs4 import BeautifulSoup
import urllib
import os.path


def pastebin():
    """Search the archive of pastebin.com and get all the download links"""

    fdirpb = "/media/preto/DESCARGAS/pastebins/"
    urlpbd = "http://pastebin.com/download.php?i="
    contents = urllib.urlopen("http://pastebin.com/archive")
    bs = BeautifulSoup(contents, "lxml")
    link = bs.find_all('table', {'class': 'maintable'})

    for l in link:
        href = l.find_all('a')
        for h in href:
            if 'href' in h.attrs:
                if 'archive' not in h['href']:
                    filepb = h['href'][1:]
                    if filterurl(urlpbd+filepb) is True:
                        download(urlpbd+filepb, filepb, fdirpb)


def download(url, fname, fdir):
    """"Write the file to a folder only if don't exist."""

    if os.path.isfile(fdir+fname) is not True:

        try:
            fa = open(fdir+fname, "a")
            fileurl = urllib.urlopen(url)
            for f in fileurl:
                fa.write(f)
            fa.close()

        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
            pass
        except:
            pass


def filterurl(urlf):
    """Check if a word is in the file."""

    words = ["password", "passwd", "root", "@gmail.com", "DATABASE:", "login", "DB DUMP"]
    filterurl = urllib.urlopen(urlf)
    for f in filterurl:
        for w in words:
            if w in f:
                print f
                return True


#download("http://pastebin.com/download.php?i=qhCjGFhe","qhCjGFhe","./pastebins/")
#filterurl("http://pastebin.com/download.php?i=qhCjGFhe")
pastebin()
