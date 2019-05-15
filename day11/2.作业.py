# 2、写函数，检查获取传入列表或元祖对象的所有奇数位索引对应的元素
def func(l):
    return l[1::2]
print(func([1,2,3,4,5,6]))

# 3、判断传入的值（str、list、dic）长度是否》5
def func1(x):
    return len(x)>5
ret = func1('dada')
print(ret)