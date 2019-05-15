# 1、编写装饰器，为多个函数加上认证的功能（用户账号密码来源于文件）
# 要求登陆成功一次，后续的函数都无需再输入用户名密码

# def login(func):
#     def inner(*args, **kwargs):
#         '''登陆程序'''
#         username = input('username:')
#         password = input('password:')
#         if username == 'ls' and password == '123':
#             ret = func(*args, **kwargs)  # func是被装饰的函数
#             return ret
#         else: print('登陆失败')
#     return inner
#
# def shoplist_add():
#     print('add a good')
#
# def shoplist_del():
#     print('del a good')






# 2、编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用函数的名称写入文件
def log(func):
    def inner(*args, **kwargs):
        with open('log', 'a', encoding='utf-8') as f:
            f.write(func.__name__+'\n')
        ret = func(*args, **kwargs)
        return ret
    return inner

@log
def shoplist_add1():
    print('add a good')

@log
def shoplist_del2():
    print('del a good')

# shoplist_add1()


# 进阶作业
'''
1、编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
2、为1编写创时期，实现缓存网页内容的功能
具体：实现下载的页面存放于文件中，如果文件内有值（文件大小部位0），就有先从文件中读取
     网页内容，否则就去下载，然后保存在文件中
'''

import os # 查看大小
from urllib.request import urlopen
def cache(func):
    def inner(*args, **kwargs):
        if os.path.getsize('web_cache'):
            with open('web_cache', 'rb') as f:
                return f.read()

        ret = func(*args, **kwargs)
        with open('web_cache', 'wb') as f:
            f.write(b'****'+ret)
        return ret
    return inner
@cache
def get(url):
    code = urlopen(url).read()
    return code

ret = get('http://www.baidu.com')
print(ret)
ret = get('http://www.baidu.com')
print(ret)
ret = get('http://www.baidu.com')
print(ret)