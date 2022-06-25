import urllib.request
import re
url="http://www.jd.com"
#1.数据爬到内存中
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
#从爬取到的数据中筛出需要的数据
pat="<title>(.*?)</title>"
rst=re.compile(pat,re.S).findall(data)

#2.数据爬取到硬盘中(爬取整个html源码)
urllib.request.urlretrieve(url,filename=r"C:\Users\Crist\Documents\爬虫数据\data.txt")

