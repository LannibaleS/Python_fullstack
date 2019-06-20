# 迭代器
''''''
l = [1,2,3]
print(dir([]))  # 告诉我列表拥有的所有方法
# 双侠方法，已经用c语言写好的方法

set(dir([]))&set(dir({}))

# 总结一下我们现在所知道的：可以被for循环的都是可迭代的，要想可迭代，内部必须有一个__iter__方法。
print([1,2].__iter__()) # <list_iterator object at 0x1024784a8>
# 一个列表执行了__iter__()之后，返回值就是一个迭代器

print(set(dir([1,2].__iter__()))-set(dir([1,2])))
'''{'__length_hint__', '__next__', '__setstate__'}'''

iter_l = [1,2,3,4,5,6].__iter__()
#获取迭代器中元素的长度
print(iter_l.__length_hint__())

#根据索引值指定从哪里开始迭代
print('*', iter_l.__setstate__(4))

'''Iterable可迭代的  --> __iter__ 只要含有__iter__方法就是可迭代的
[].__iter__() 迭代器  --> __next__ 通过next就可从迭代器中一个一个取值

只要含有__iter__()方法的都是可迭代的  ---  可迭代协议
迭代器遵循迭代器协议：必须同时拥有__iter__方法和__next__方法。
'''

from collections import Iterable, Iterator
print(isinstance([], Iterator))
print(isinstance([], Iterable))
'''列表不是迭代器，但是列表可迭代'''

'''
迭代器协议和可迭代协议
可以for循环的都是可迭代的
可迭代的内部都有__iter__()方法
只要是迭代器，一定是可迭代的
可迭代的.__iter__()方法就可以得到一个迭代器
迭代器中的__next__()可以一个一个地获取值

for循环其实就是在使用迭代器
iterator

只有是可迭代对象的时候，才能用for
当我们遇到一个新的变量，不能确定能不能for循环的时候，就判断它是否可迭代
print(__iter__() in dir())

for循环的本质就是迭代器

迭代器的好处：
    1、从容器类型中一个一个的取值，会把所有的值都取到
    2、节省内存空间 range、f
        迭代器并不会在内存中再占用一大块内存
            而是随着循环，每次生成一个
            每次next，每次给我一个
'''

x = [1,2,3,4,5,6]
iter_x = x.__iter__()
while True:
    try:
        item = iter_x.__next__()
        print(item)
    except StopIteration:
        break


print(isinstance(range(10), Iterable))
print(isinstance(range(10), Iterator))

# 生成器 -- 本质是迭代器
# 生成器函数 -- 本质是我自己写的迭代器
# 生成器表达式