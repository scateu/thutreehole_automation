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

    #return '刚在C楼门口与身着黑色连衣裙高贵冷艳的女子擦身而过，现在仍心神向往。我明明已经有可爱美丽的女朋友了，为什么还会这样把持不住！！烦啊！！突然想起了一句诗:'+line
    #return '今天走在路上我突然想到了一句诗，不知道有没有男生能理解我此刻的心情：'+line+'   真想有个肩膀依靠啊....'
    return '我艹艹艹艹艹！%s居然只有%d？！！！尼玛！气得我想起了一句诗：'%(getWords(['微积分','大物','高代','普物','基物实验','马克思主义新闻观','高级新闻采写','数理逻辑','概率论','量子力学','信号与系统','高等电动力学']),random.randint(60,75))+line

def getWords(wordlist):
    if len(wordlist) == 0:
        return ' '
    i = random.randint(0,len(wordlist)-1)
    return wordlist[i]

if __name__ == '__main__':
    import time
    while True:
        poem =  getPoem() 
        Say(poem)
        time.sleep(1812)
