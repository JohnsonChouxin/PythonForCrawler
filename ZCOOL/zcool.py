#coding: utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

class ImageDownload(object):
    def download(self,url,path):
        content = urllib2.urlopen(url)

        soup = BeautifulSoup(content.read(),"html.parser")

        uls = soup.find_all("img",class_="mb10")

        deepIndex = 0

        for item in uls:

            deepIndex += 1

            print item["src"]
            u = urllib.urlopen(item["src"])
            data = u.read()
            f = open(path+str(deepIndex)+".jpg", 'wb')
            f.write(data)
            f.close()



# 网址
index = 0

basicUrl = "http://www.zcool.com.cn/index!"

basicUrlTail = ".html#mainList"

# 创建文件夹
isExists=os.path.exists("zcool")

if not isExists:
    os.makedirs("zcool")

# 进入循环
for a in range(1,100):
    print a

    index += 1

    url = basicUrl + str(index)+basicUrlTail

    content = urllib2.urlopen(url)

    soup = BeautifulSoup(content.read(),"html.parser")

    uls = soup.find_all("img",height="188",width="250")

    deepIndex = 0

    for item in uls:

        deepIndex += 1

        title = "ImagesFile" + "section" + str(index) + "row" + str(deepIndex)

        os.makedirs("zcool/"+title)
        file = open("zcool/"+title+"/introduction.text","a")

        file.write(item.parent["title"] + "\n")
        file.write(item.parent["href"])

        downloader = ImageDownload()
        downloader.download(item.parent["href"],"zcool/"+title+"/")






