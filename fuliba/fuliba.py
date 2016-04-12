#coding: utf-8
import urllib
import urllib2
import sys
import re
import os
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

basicUrl    = "http://fuliba.net/page/"


class Processor(object):

    def download(self,index):

        url = basicUrl + str(index)

        content = urllib2.urlopen(url)

        soup    = BeautifulSoup(content.read(),"html.parser",from_encoding="UTF-8")

        uls     = soup.find_all("article",class_="entry-common clearfix")

        item0 = uls[0]

        if index == 1:
            result = self.checkNew(str(item0.p.a.img["alt"]))
            if not result:
                return

        for item in uls:
            title = item.p.a.img["alt"]
            strinfo = re.compile('/')
            changeTitle = strinfo.sub('_',title)
            print title

            result = self.checkRepeat(title)
            if not result:
                break

            if os.path.exists("fuliba/"+changeTitle) :
                continue

            os.makedirs("fuliba/"+changeTitle)
            file = open("fuliba/"+changeTitle+"/"+changeTitle+".text","a")

            file.write(item.p.a.img["alt"] + "\n")
            b = str(item.p)
            c = b.split(r"</a>")[1].split(r"</p>")[0].strip()
            file.write(c + "\n")
            file.write(item.p.a["href"])

            u    = urllib.urlopen(item.p.a.img["src"])
            data = u.read()
            f    = open("fuliba/"+changeTitle+"/content.jpg", 'wb')
            f.write(data)
            f.close()

    def checkNew(self,fileName):
        file = open("fuliba/TheNewOne/TheNewOne.text","r")
        title = file.read().split("\n")[0]
        if len(title)==0:
            theFile = open("fuliba/TheNewOne/TheNewOne.text","w")
            theFile.write(fileName)
            return True

        if title == fileName:
            print "Not new"
            return False
        else:
            theFile = open("fuliba/TheNewOne/TheNewOne.text","w")
            theFile.write(fileName + "\n")
            theFile.write(title)
            return True

    def checkRepeat(self,fileName):
        file = open("fuliba/TheNewOne/TheNewOne.text","r")
        listTitle = file.read().split("\n")
        title = ""
        if len(listTitle) == 2:
            title = listTitle[1]
            if fileName == title:
                return False
            else:
                return True
        else:
            return True


# 创建根文件夹
isExists = os.path.exists("fuliba")

if not isExists:
    os.makedirs("fuliba")

# 创建记录文件夹
isExists = os.path.exists("fuliba/TheNewOne/TheNewOne.text")

if not isExists:
    os.makedirs("fuliba/TheNewOne")
    file = open("fuliba/TheNewOne/TheNewOne.text","a")


# 进入循环
for a in range(1,2):
    # 打印页码
    print "\n"
    print "This is page " + str(a)
    print "\n"

    processor = Processor()
    processor.download(a)
