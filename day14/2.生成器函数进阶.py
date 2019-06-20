def generator():
    print(123)
    content = yield 1
    print('&&&',content)
    print(456)
    yield 2
    print(789)

g = generator()
ret = g.__next__()
print('**', ret)
# ret = g.__next__()
ret = g.send('ls')
print('**', ret)

'''
send的获取下一个值的效果和next基本一致
只是在获取下一个值的时候，给上一个yield的位置传递一个数据
使用send的注意事项
    第一次使用生成器的时候，使用next获取下一个值
    最后一个yield不能获取外部的值

'''

'''获取移动平均值'''
def average():
    sum = 0
    count = 0
    avg = 0
    while True:

        num = yield avg # 10
        sum += num   #10
        count += 1
        avg = sum/count

avg_g = average()
avg_g.__next__()
avg = avg_g.send(10)
avg = avg_g.send(20)
avg = avg_g.send(30)
print(avg)

'''带装饰器的生成器'''
print('''带装饰器的生成器''')
def init(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.__next__()
        return g
    return inner

@init
def average():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum/count

avg1 = average()
ret = avg1.send(10)
ret = avg1.send(20)
print('带预激活生成器的装饰器', ret)

print('''yield from''')
'''yield from'''
# def generator():
#     a = 'abcde'
#     b = '12345'
#     for i in a:
#         yield i
#     for i in b:
#         yield i

def generator():
    a = 'abcde'
    b = '12345'
    yield from a
    yield from b

g = generator()
for i in g:
    print(i)
