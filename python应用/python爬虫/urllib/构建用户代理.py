import random
import urllib.request

url="http://m.biancheng.net/"
# opener=urllib.request.build_opener()
# UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
# opener.addheaders=[UA]
# urllib.request.install_opener(opener)
# data=urllib.request.urlopen(url).read().decode("utf-8","ignore")

#构建用户代理池
uapools=["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44",
         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"]
def UA():
    opener=urllib.request.build_opener()
    thisua=random.choice(uapools)
    ua=("User-Agent",thisua)
    opener.addheaders=[ua]
    urllib.request.install_opener(opener)
    print("当前使用UA："+str(thisua))
for i in range(0,4):
    UA()
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")