''''''
''' [每一个元素或者是和元素相关的操作 for 元素 in 可迭代数据类型]  # 遍历之后挨个处理 '''
''' [ 满足条件的元素相关的操作 for 元素 in 可迭代数据类型 if 元素相关的条件]  # 筛选功能 '''

''' 30以内，能被3整除的数 '''
ret = [i for i in range(30) if i%3 == 0]
print(ret)

''' 30以内，能被3整除的数的平方 '''
ret1 = [i*i for i in range(30) if i%3 == 0]
print(ret1)

''' 找到嵌套列表中名字含有两个'e'的所有名字 '''
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
ret2 = [name for list in names for name in list if name.count('e') == 2]
print(ret2)


''' 字典推到式 '''
''' 例一：将一个字典的key和value对调 '''
mcase = {'a': 10, 'b': 34}
mcase_frequency = {mcase[k]: k for k in mcase}
print(mcase_frequency)


'''例二：合并大小写对应的value值，将k统一成小写'''
mcase1 = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
''' {'a':12, 'b':34, 'z':3} '''
mcase_frequency1 = { k.lower(): mcase1.get(k.lower(), 0) + mcase1.get(k.upper(), 0) for k in mcase1.keys() }
print(mcase_frequency1)



''' 集合推导式
例：计算列表中每个值的平方，自带去重功能 '''
squared = {x**2 for x in [1, -1, 2]}
print(squared)


'''
练习题：

例1:  过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
[ i.upper() for i in str if len(i)  >= 3]
[name.upper() for name in names if len(name)>3] 


例2:  求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
[ (x,y) for x in range(6) if x%2 == 0 for y in range(6) if y%2 == 1 ]

例3:  求M中3,6,9组成的列表M = [[1,2,3],[4,5,6],[7,8,9]]
'''

example2 = [ (x,y) for x in range(6) if x%2 == 0 for y in range(6) if y%2 == 1 ]
print(example2)

M = [[1,2,3],[4,5,6],[7,8,9]]
example3 = [ row[2] for row in M]
print(example3)


'''
各种推到式： 生成器、 列表、字典、集合
    # 便利操作
    # 筛选操作
'''

''' 
本章小结
可迭代对象：

　　拥有__iter__方法

　　特点：惰性运算

　　例如:range(),str,list,tuple,dict,set

迭代器Iterator：

　　拥有__iter__方法和__next__方法

　　例如:iter(range()),iter(str),iter(list),iter(tuple),iter(dict),iter(set),reversed(list_o),map(func,list_o),filter(func,list_o),file_o

生成器Generator：

　　本质：迭代器，所以拥有__iter__方法和__next__方法

　　特点：惰性运算,开发者自定义

使用生成器的优点：

1.延迟计算，一次返回一个结果。也就是说，它不会一次生成所有的结果，这对于大数据量处理，将会非常有用。

#列表解析
sum([i for i in range(100000000)])#内存占用大,机器容易卡死
 
#生成器表达式
sum(i for i in range(100000000))#几乎不占内存
 

2.提高代码可读性

生成器中的数据，只能取一次，取完就没有了
惰性运算，不找他，他就不工作
 
'''

'''
生成器相关的面试题
生成器在编程中发生了很多的作用，善用生成器可以帮助我们解决很多复杂的问题

除此之外，生成器也是面试题中的重点，在完成一些功能之外，人们也想出了很多魔性的面试题。
接下来我们就来看一看～

def demo():
    for i in range(4):
        yield i

g=demo()

g1=(i for i in g)
g2=(i for i in g1)

print(list(g1))
print(list(g2))

面试题1

'''
def demo():
    for i in range(4):
        yield i

g=demo()
print(g)
g1=(i for i in g)
for i in g:
    print(i)
print('g1:',g1)
print(list(g1))

for i in g1:
    print('****',i)

g2=(i for i in g1)
print(list(g2))