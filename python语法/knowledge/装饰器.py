def decorator(fn):
    print("-----------------调用装饰器函数decorator-----------------")
    fn()
    return "装饰器函数的返回值"

@decorator
def fun():
    print("执行fun()函数")

