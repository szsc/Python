#!/usr/bin/python
# -*- coding: UTF-8 -*-
#注意：使用python2.7的语法

def decorator(func):
    print("I am doing some boring work before executing func()")

    func()

    print("I am doing some boring work after executing func()")

def new_decorator(func):
    #以下函数是装饰器
    def wrapTheFunction():
        print("I am doing some boring work before executing func()")

        func()

        print("I am doing some boring work after executing func()")

    return wrapTheFunction

def simple_function():
    print("原函数自我介绍：我是一个简单的函数，名字叫做simple_function")

#未被装饰器修饰前
simple_function()
print "---------------------------------------------------------"

#被装饰器修饰后
"""1. 简单的装饰器, 以下语句等价于decorator(simple_function)"""
@decorator
def simple_function():
    print("原函数自我介绍：我是一个简单的函数，名字叫做simple_function")

print "---------------------------------------------------------"

"""2. 返回装饰器函数"""
@new_decorator
def simple_function():
    print("原函数自我介绍：我是一个简单的函数，名字叫做simple_function")
simple_function()

#等价于以下用法
# simple_function = new_decorator(simple_function)
# simple_function()
