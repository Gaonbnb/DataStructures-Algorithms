
"""
# 今日目标学习装饰器与元类
# first
def foo(num):
    return num + 1

value = foo(3)
print(value)

def bar():
    print("bar")

foo = bar
foo()
# 函数当作返回值
def foo():
    return 1
def bar():
    return foo
print(bar())
print(bar()())
print(foo())

# 函数当作参数
# 断点显示return fun时，先执行完foo函数，再返回return，再return
def foo(num):
    return num + 1
def bar(fun):
    return fun(3)
value = bar(foo)
print(value)

# 函数嵌套
def outer():
    x = 1
    def inner():

        print(x)
    inner()
outer()

# 闭包
def outer(x):
    def inner():
        print(x)
    return inner
closure = outer(1)
closure()

# 装饰器
def foo():
    print("foo")
def foo():
    print("日记开始")
    print("foo")
    print("日记结束")

def outer(func):
    def inner():
        print("日记开始")
        print("foo")
        print("日记结束")
    return inner
def foo():
    print("foo")
foo = outer(foo)
foo()

@outer
def foo():
    print("foo")
foo()

# 对多个函数统计运行时间

from time import time, sleep

def fun_one():
    start = time()
    sleep(2)
    end = time()
    cost_time = end - start
    print("func one run time {}".format(cost_time))

def fun_two():
    start = time()
    sleep(1)
    end = time()
    cost_time = end - start
    print("func two run time {}".format(cost_time))
def fun_three():
    start = time()
    sleep(3)
    end = time()
    cost_time = end - start
    print("func three run time {}".format(cost_time))


def run_time(func):
    def wrapper():
        start = time()
        func()
        end = time()
        cost_time = end - start
        print("func three run time {}".format(cost_time))
    return wrapper

@run_time
def fun_one():
    sleep(1)

@run_time
def fun_two():
    sleep(2)
@run_time
def fun_three():
    sleep(3)
  

# 带参数
def logger(msg=None):
    def run_time(func):
        def wrapper(*args, **kwargs):
            start = time()
            func()
            end = time()
            cost_time = end - start
            print("{0} func time run time {1}".format(msg, cost_time))
        return wrapper
    return run_time


@logger(msg="One")
def fun_one():
    sleep(1)
@logger(msg="Two")
def fun_two():
    sleep(2)
@logger(msg="Three")
def fun_three():
    sleep(3)
    
   
# 假如要输出不同的等级，这个函数只有info等级，但无其他等级，因此若要输出其他的等级如的debug和warning，
# 可以用带入参数或者利用自定义属性来修改日志等级

from time import time, sleep
import logging
# 日志输出很重要
def logger_info(func):
    logmsg = func.__name__
    def wrapper():
        func()
        log.log(logging.INFO, "{}".format(logmsg))
    return wrapper
 
### 给装饰器添加属性

import logging
from functools import partial

# 把func变成一个对象obj的属性，再通过调用，为装饰器添加了两个属性，分别用于改变输出日志内容和改变输出日志等级
def wrapper_property(obj, func=None):
    #没传入函数func,返回一个固定住obj的参数的wrapper_property函数
    if func is None:
        return partial(wrapper_property, obj)
    #将给定对象上的命名属性设置为指定值，obj.(func.name) = func.把func变成一个对象obj的属性
    setattr(obj, func.__name__, func)
    return func

def logger_info(level, name=None, message=None):
    
    def decorate(func):
        # 如果message为真，则message，否则func的name
        logmsg = message if message else func.__name__

        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @wrapper_property(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @wrapper_property(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper
        
    return decorate

@logger_info(logging.WARNING)
def main(x, y):
    return x + y

main(3, 3)

main.set_level(logging.ERROR)
main(5, 5)

# 函数的元信息
# 用户可以通过注释等方式为函数添加元信息,但是通过装饰器，函数的元信息都丢失了
from time import time 
def run_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        func()
        end = time()
        cost_time = end - start
        print("{}".format(cost_time))
    return wrapper
@run_time
def fun_one():
    #hhhhhhhh
    print("hhhhhhhhhhhhhhhh")
fun_one()
print(fun_one.__name__)
print(fun_one.__doc__)
 """

from time import time
from functools import wraps 
# 保留元信息
def run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        func()
        end = time()
        cost_time = end - start
        print("{}".format(cost_time))
    return wrapper
@run_time
def fun_one():
    #hhhhhhhh
    print("hhhhhhhhhhhhhhhh")
fun_one()
print(fun_one.__name__)
print(fun_one.__doc__)