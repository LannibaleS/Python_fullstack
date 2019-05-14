# 带参数的装饰器
import time

print('带参数的装饰器')
def timmer(f):    # 装饰器函数
    def inner(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)       # 被装饰的函数 热接受f()的返回值'ls'
        end = time.time()
        print(end - start)
        return ret      # inner函数返回值ret

    return inner

@timmer        # 语法糖
def func(a):    # 被装饰的函数
    time.sleep(0.05)
    print('hello', a)
    return 'ls'

@timmer
def func1(a, b):    # 被装饰的函数
    time.sleep(0.05)
    print('hello', a, b)
    return 'ls'

# func = timmer(func)   # 实际上是调用inner
# 这时候调用inner就有返回值了
ret = func('htz')
print(ret)

ret1 = func1('ls', 'htz')
print(ret1)

# 装饰器的规定模式
def wrapper(f):   # 装饰器函数， f是被装饰的函数
    def inner(*args, **kwargs):
        # 函数之前想做的事情，在这里加代码
        ret = f(*args, **kwargs)  # 动态参数原封不动的传递给被装饰的函数，这句话是在真正的执行被装饰的函数
        # 函数之后想做的事情，在这里加代码
        return ret # 被装饰函数的返回值，要返回给外面
    return inner

@wrapper
def func(a, b):
    print('ls', a, b)
    return 'hello'


'''
def wrapper():
    def inner():
        pass
    return inner
    
'''

def wrapper(func):   # ls当作wrapper的参数
    def inner(*args, **kwargs):
        # print('inner')
        ret = func(*args, **kwargs)  # 被装饰的函数
        return ret
    return inner

@wrapper  # ls = wrapper(ls) 把被装饰的函数，以参数的形式传给装饰器，返回值还叫ls，返回值就是inner函数，调用ls实际上就是调用inner
def ls():
    print('123')
    # return 'htz'

ret = ls()  # inner
# print(ret)