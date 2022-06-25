import packages    #使用import和from import会触发__init__.py中的代码执行
import packages.Module as mod  #给模块Module起个别名
from packages import Module  #使用包名导入模块
from packages import printDF  #使用包名导入函数

#使用包名调用函数和类
packages.func()
obj=packages.Animal("狗", "公", 3)
print("-----------------------------------------------")
#使用模块别名和模块名调用函数
mod.func()
Module.func()
#使用模块名调用类(创建对象)
animal=Module.Animal("猫","母",4)
print("这是类变量的值：%s" %Module.Animal.category)
animal.Behavior()#使用对象调用类方法
print("-------------------------------------------------")
#使用函数名调用函数
printDF()


