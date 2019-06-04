# 迭代器.__next__()
# next(迭代器)
def next(迭代器):
    迭代器.__next__()

[].__len__()
len([])

'''
iter(可迭代的)
可迭代的 = 可迭代对象
可迭代的.__iter__()
迭代器 = iter(可迭代的)

'''

range(10)
range(1,11)
range(1,11,2)
# range是可迭代的，但不是迭代器
print('__next__' in dir(range))

# dir 查看一个变量的所有方法
print(dir(1))
print(dir([]))

# help
# help(str)

# callable 只能查变量，查一个变量到底是一个变量还是一个值，函数返回True，值返回False；用来检测是不是函数
# 变量
print(callable(print))
a = 1
print(callable(print(a)))
print(callable(globals))
def func():pass
print(callable(func))

'''
某个方法属于某个数据类型的变量，就用.调用
如果某个方法，不依赖于任何数据变量，就直接调用 --- 内置函数 和 自定义函数
'''

import time

# f = open('')
# print(f.writable())  # 可读的


''' 内存相关 '''
'''id'''
'''hash'''
print(hash(123214))
print(hash('dawdad'))
print(hash('dawdadaa'))
print(hash(('1', 'aaa')))
# print(hash([])) #TypeError: unhashable type: 'list'

''' 对于相同可hash数据的hash值，在一次程序的执行过程中总是不变的 '''

print('dawdawd', end='') # end= 指定结尾
print()
print(1,2,3,4,5, sep='|') # sep= 指定分隔符
# print('aaaa', file=)   # 讲print打印到文件中

