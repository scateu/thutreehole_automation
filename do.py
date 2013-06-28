# -*- coding:utf-8 -*-
import urllib2
import urllib
import cookielib
import httplib
import linecache
import random

def Say(words):
    print words
    cookieJar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
    opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.11) Gecko/20101012 Firefox/3.6.11'),
    ]
    f = opener.open("http://www.thutreehole.tk/")
    
    csrftoken = cookieJar._cookies['www.thutreehole.tk']['/']['csrftoken'].value
    print csrftoken
    
    h = httplib.HTTPConnection('www.thutreehole.tk') 
    b = {'csrfmiddlewaretoken':csrftoken,'content':words}
    data = urllib.urlencode(b)

    print opener.open("http://www.thutreehole.tk/",data).read()

def getPoem():
    poems = open('./poems')
    line = linecache.getline('./poems',random.randint(1,1500))
    return '今天走在路上我突然想到了一句诗，不知道有没有男生能理解我此刻的心情：'+line+'   真想有个肩膀依靠啊....'

if __name__ == '__main__':
    import time
    while True:
        poem =  getPoem() 
        Say(poem)
        time.sleep(1812)
