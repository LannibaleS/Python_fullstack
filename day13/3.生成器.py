'''生成器函数'''
'''
def generator():
    print(1)
    return 'a'

ret = generator()
print(ret)
'''

# 只要含有yield关键字的函数都是生成器函数
# yield不能和return共用，且需要写在函数内部
def generator():
    print(1)
    yield 'a'
    print(2)
    yield 'b'

# 生成器函数：执行之后会得到一个生成器作为一个返回值，生成器就是一个迭代器
ret = generator()
#print(ret)
#print(ret.__next__()) # 1 a
#print(ret.__next__()) # 2 b

for i in ret:
    print(i)

def ls():
    for i in range(20):
        yield 'ls%s'%i
ls = ls()
for i in ls:
    print(i)
