#coding: utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

# 图片下载器
class ImageDownload(object):

    def download(self,url,path):
        content = urllib2.urlopen(url)

        soup    = BeautifulSoup(content.read(),"html.parser")

        uls     = soup.find_all("img",class_="mb10")

        deepIndex = 0

        for item in uls:

            deepIndex += 1
            # 写入图片
            print item["src"]
            u    = urllib.urlopen(item["src"])
            data = u.read()
            f    = open(path+str(deepIndex)+".jpg", 'wb')
            f.write(data)
            f.close()



# 网址构造参数
index           = 0

basicUrl    = "http://www.zcool.com.cn/index!"

basicUrlTail    = ".html#mainList"

# 创建根文件夹
isExists = os.path.exists("zcool")

if not isExists:
    os.makedirs("zcool")

# 进入循环
for a in range(1,11):
    # 打印页码
    print a

    index   += 1

    url     = basicUrl + str(index)+basicUrlTail

    content = urllib2.urlopen(url)

    soup    = BeautifulSoup(content.read(),"html.parser")

    uls     = soup.find_all("img",height="188",width="250")

    deepIndex = 0

    for item in uls:

        deepIndex += 1

        # 构造文件夹名称
        title = "ImagesFile" + "section" + str(index) + "row" + str(deepIndex)

        # 创建文件夹和写入简介.text文件
        os.makedirs("zcool/"+title)
        file = open("zcool/"+title+"/introduction.text","a")

        # 写入改图片数组的标题和连接
        file.write(item.parent["title"] + "\n")
        file.write(item.parent["href"])

        # 创建图片下载器，去下载该item下的图片集合并保存到简介文件相同的目录下
        downloader = ImageDownload()
        downloader.download(item.parent["href"],"zcool/"+title+"/")






