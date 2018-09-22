#coding = utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = 'src="(.+?\.jpg)" alt='
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x+=1
    return imglist

html = getHtml("http://pic.yxdown.com/list/0_0_1.html")

print getImg(html)

https://blog.csdn.net/Cloudox_/article/details/53465923  
