'''
lambda 表达式的语法格式如下：
name = lambda [list] : 表达式
其中，定义 lambda 表达式，必须使用 lambda 关键字；
[list] 作为可选参数，等同于定义函数指定的参数列表；value 为该表达式的名称。
'''

add = lambda x,y:x+y
print(add(3,4))

func=lambda x,y:print(x+y)
a=func(3,4) #返回值为None
print(a)  #打印None