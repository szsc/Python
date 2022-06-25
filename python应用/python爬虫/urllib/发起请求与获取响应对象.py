import urllib.request
#1.获取响应对象
# urlopen()向URL发请求,返回响应对象,注意url必须完整
response=urllib.request.urlopen('http://www.baidu.com/')
print(response)

#2.输出HTML信息
#提取响应内容
html = response.read().decode('utf-8')#该方法返回的结果是字节串类型(bytes)，因此需要使用 decode() 转换为字符串
#打印响应内容
print(html)