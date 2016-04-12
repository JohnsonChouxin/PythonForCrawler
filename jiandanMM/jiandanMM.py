#coding: utf-8
import urllib
import urllib2
import sys
import re
import os
import threading
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

# 新线程执行的代码:
def loop(urlstring,filepath):
    def gogo():
        u    = urllib.urlopen(urlstring)
        data = u.read()
        f    = open(filepath, 'wb')
        f.write(data)
        f.close()

    t = threading.Thread(target=gogo,name="gogoThread")
    t.start()
    t.join()

# 创建根文件夹
isExists = os.path.exists("jiandan")

if not isExists:
    os.makedirs("jiandan")

index = 1943

basicUrl    = "http://jandan.net/ooxx/page-"

for gdou in range(1,10):
    url = basicUrl + str(index-gdou) + "#comments"

    browser = webdriver.Firefox() # Get local session of firefox
    browser.get(url) # Load page

    soup    = BeautifulSoup(browser.page_source.encode("UTF-8"),"html.parser",from_encoding="UTF-8")

    uls     = soup.find_all("div",class_="text")

    deepIndex = 0

    for item in uls:
        deepIndex += 1
        try:
            print item.p.a["href"]
            vote = item.find_all("div",class_="vote")
            print vote[0].find_all("span")[1].string
            print vote[0].find_all("span")[2].string
            print "*"*20
            if int(vote[0].find_all("span")[1].string) <= 100:
                continue
            loop(item.p.a["href"],"jiandan/"+str(gdou)+str(deepIndex)+".jpg")
        except TypeError, e:
            continue

    browser.close()
