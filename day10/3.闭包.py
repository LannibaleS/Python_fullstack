# 闭包：嵌套函数，内部函数"调用"外部函数的变量
# 最简单的闭包
# def outer():
#     a = 1
#     def inner():
#         print(a)
#     inner()
# outer()
# 这样会频繁建立、消除新的内存空间

def outer():
    a = 1
    def inner():
        print(a)
    # print(inner.__closure__)
    ''' (<cell at 0x101dc9348: int object at 0x100984a00>,) '''
    return inner


inn = outer()
inn()

# inn是全局变量，保护了a变量，延长了a的生命周期

# 闭包最常见的形式，在函数的外部使用内部的函数

# print(outer.__closure__)
''' None '''


# 闭包的应用
import urllib
import ssl
from urllib.request import urlopen
ssl._create_default_https_context = ssl._create_unverified_context
def get_url():
    url = 'https://nba.hupu.com'
    def get():
        ret = urlopen(url).read()
        print(ret)
    return get

get_func = get_url()
get_func()


