
''' any 判断是否有bool值为 True 的值'''

''' zip '''
print('\n====== zip ======')
l = [1,2,3]
l2 = ['a', 'b', 'c', 'b']
l3 = ('*', '**', [1,23])
l4 = {'k1':1, 'k2':2 }
for i in zip(l,l2,l3,l4 ):
    print(i)


''' filter '''
import time
print('\n====== filter ======')

def is_odd(x):
    return x%2 ==1

begin = time.time()
z = range(100)
ret = filter(is_odd, z)
# for i in ret:print(i)
end = time.time()
print(end-begin)

begin1 = time.time()
ret1 = [i for i in z if i%2 == 1]
# for i in ret1:print(i)
end1 = time.time()
print(end1-begin1)
print(ret1)

''' 利用filter()，可以完成很多有用的功能，例如，删除 None 或者空字符串 '''
print('\n====== filter 删除 None 或者空字符串 ======')
def is_not_empty(s):
    return s and len(s.strip()) > 0
print(list(filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])))


''' 利用filter()，过滤出开平方是整数的 
tips：一个数对1取余，如果余数为0就是整数
'''
print('\n====== filter 过滤出开平方是整数的 ======')

from math import sqrt
def is_int(x):
    return sqrt(x)%1 == 0
print(list(filter(is_int, range(101))))


''' map '''
import time
print('\n====== map ======')
ret2 = map(abs, [1,-9,2,-20])
for i in ret2:print(i)


'''
filter 
1、执行了filter之后的结果集合 《= 执行前的个数
2、filter只管筛选，不会改变原来的值


map：
1、执行前后元素个数不变
2、值可能发生变化 
        
'''

''' sort 原列表的基础上进行排序 '''
import time
print('\n====== sort ======')
k = [1,-4,6,5,-10]
k.sort(key=abs)
print(k)


''' sorted 生成了一个新的列表，不改变原列表，但是占内存，慎用，已知列表不大的情况下用 '''
import time
print('\n====== sorted ======')
k1 = [1,-4,6,5,-10]
print(k1)
print(sorted(k1))

print(sorted(k1, key=abs, reverse=False))
print(sorted(k1, key=abs, reverse=True))

k2 = ['dasd','1','213','vvfedcv']
print(sorted(k2, key=len, reverse=False))


''' lambda '''
print('\n====== lambda ======')
add = lambda x,y : x + y
print(add(1,2))