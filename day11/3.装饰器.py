# 装饰器形成的过程

# 装饰器的作用

# 原则：开放封闭原则

# 装饰器的固定模式
# os模块是和操作系统打交道的模块
# time是时间模块
import time
print(time.time()) # 从1970年到现在过了多少秒
# time.sleep(5)
# print('hello')


def func1():
    print('ls')

def timmer(f):    # 装饰器函数
    def inner():
        start = time.time()
        ret = f()       # 被装饰的函数 热接受f()的返回值'ls'
        end = time.time()
        print(end - start)
        return ret      # inner函数返回值ret

    return inner

@timmer        # 语法糖
def func():    # 被装饰的函数
    time.sleep(0.05)
    print('hello')
    return 'ls'

# func = timmer(func)   # 实际上是调用inner
# 这时候调用inner就有返回值了
ret = func()
print(ret)

# 不想修改函数的调用方式，但是还想在原来的函数前后添加功能
# timmer就是一个装饰器函数，只对一个函数，有一些装饰作用


# 原则： 开放封闭原则
# 开放：对扩展是开放的
# 封闭：对修改是封闭的

def outer():
    def inner():
        return 'inner'
    inner()
outer()


# 带参数的装饰器
print('带参数的装饰器')
def timmer(f):    # 装饰器函数
    def inner(a):
        start = time.time()
        ret = f(a)       # 被装饰的函数 热接受f()的返回值'ls'
        end = time.time()
        print(end - start)
        return ret      # inner函数返回值ret

    return inner

@timmer        # 语法糖
def func(a):    # 被装饰的函数
    time.sleep(0.05)
    print('hello', a)
    return 'ls'

# func = timmer(func)   # 实际上是调用inner
# 这时候调用inner就有返回值了
ret = func('htz')
print(ret)