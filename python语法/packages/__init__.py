'''
这里可以编写一些 Python 初始化代码，比如预先导入包内常用的类，方便通过包名调用！！
则当有其它程序文件导入learn包时，会自动执行__init__.py文件中的代码！
本模块使用了相对路径的导入语法，就不能直接运行本模块了，会报错！
'''
import pandas as pd
from .Module import Animal
from .testModule import TestClass
from .Module import func
print("导入learn包自动触发__init__.py模块的执行！")
print("-------------------------------------------")

def printDF():
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
    print(df)
if __name__=="__main__":
    printDF()