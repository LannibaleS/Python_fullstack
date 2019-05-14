# 1、编写装饰器，为多个函数加上认证的功能（用户账号密码来源于文件）
# 要求登陆成功一次，后续的函数都无需再输入用户名密码

def login(func):
    def inner(*args, **kwargs):
        '''登陆程序'''
        username = input('username:')
        password = input('password:')
        if username == 'ls' and password == '123':
            ret = func(*args, **kwargs)  # func是被装饰的函数
            return ret
        else: print('登陆失败')
    return inner

def shoplist_add():
    print('add a good')

def shoplist_del():
    print('del a good')






# 2、编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用函数的名称写入文件
