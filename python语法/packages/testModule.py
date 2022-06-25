from packages.Module import Animal  # 导入平行模块Module.py里的Animal类
print("导入了testModule")
class TestClass():
    def __init__(self):
        self.__attr1=1
    @property
    def fisrt_func(self):
        print("调用了对象的第一个方法")
        return self

    def second_func(self):
        print("调用了对象的第二个方法")

    def getAttr1(self):
        return self.__attr1
    def setAttr1(self,x):
        self.__attr1=x
    def delAttr1(self):
        del self.__attr1
    Attr = property(getAttr1, setAttr1,delAttr1)

if __name__== "__main__":
    obj = TestClass()
    #使用Property可以把方法设置成属性来访问
    obj.fisrt_func.second_func()
    #获取、设置和删除私有属性
    # print(obj.Attr)
    # obj.Attr=2
    #del obj.Attr
    #调用平行模块的类
    dog = Animal("Dog", "Male", 3)
    dog.getAge()
