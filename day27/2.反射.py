''''''
'''
isinstance和issubclass

isinstance(obj,cls)检查是否obj是否是类 cls 的对象

issubclass(sub, super)检查sub类是否是 super 类的派生类 


'''

class A:pass
a = A()
print(isinstance(a, A))

class B:pass
class C(B):pass
print(issubclass(C,B))
print('=========================\n')

'''
反射：使用字符串类型的名字，去操作变量
反射没有安全问题
'''

'''反射对象中的属性和方法，四个方法：hasattr，getattr，setattr，delattr，'''
class A:
    def func(self):
        print('in func')
a = A()
a.name = 'ls'
'''反射对象的属性'''
ret = getattr(a, 'name')
print(ret)

'''反射对象的方法'''
func = getattr(a, 'func')
func()

'''反射类的属性'''
class Z:
    price = 20
    @classmethod
    def func(cls):
        print('ZZZZZZ')

print(getattr(Z, 'price'))

'''
反射类的方法：classmethod staticmethod
类名.方法名
'''
if hasattr(Z, 'func'):
    zz = getattr(Z, 'func')
    zz()

'''模块'''
'''反射模块的属性'''
import my
print(getattr(my, 'day'))

'''反射模块的方法'''
getattr(my, 'func')()

print('\n=================')
'''反射自己模块中的变量'''
def ls():
    print('反射自己模块中的变量: htz')
year = 2019
import  sys
print(sys.modules['__main__'].year)

'''反射自己模块中的函数'''
print(getattr(sys.modules['__main__'], 'ls'))
getattr(sys.modules['__main__'], 'ls')()

#
# 变量 = input('>>>')
# print(getattr(sys.modules[__name__], 变量))

print('\n=================')
'''反射自己模块中的函数'''
import time
'''要反射的函数有参数怎么办'''
print(getattr(time,'time')())
print(getattr(time, 'asctime')())
print(time.strftime('%Y-%m_%d %H:%M:%S'))
print(getattr(time,'strftime')('%Y-%m_%d %H:%M:%S'))

print('\n=================')
'''一个模块中的类能不能反射到'''
print(getattr(my, 'X')())

if hasattr(my,'day'):
    print(getattr(my, 'day'))

print('\n=================')
''' setattr 设置修改变量 '''
class A:
    pass
a = A()
setattr(A, 'name', 'htz')
setattr(a, 'name', 'ls')

print(A.name)
print(a.name)

''' delattr 设置修改变量 '''
delattr(a, 'name')
print(a.name)
delattr(A, 'name')
# print(a.name)
