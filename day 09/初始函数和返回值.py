s = 'dawkdoakd;a'


# 定义函数 声明函数
def my_len(str):
    i = 0
    for k in str:
        i += 1
    print(i)

# 调用函数
my_len(s)
my_len('sss')

# 函数
# 定义了之后，可以在任何需要它的地方调用

def my_len(str):
    i = 0
    for k in str:
        i += 1
    # print(i)
    return i

length = my_len(s)
print(my_len(s))


# 返回值的3种情况
'''
 #没有返回值 —— 返回None
    1、不写return
    2、只写return：结束一个函数的继续
    3、return None -- 不常用
 
 #返回一个值
    1、可以返回任何数据类型
    2、只要返回就可以接收到
    3、如果在一个程序中有多个return，那么只执行一个
 
 
 #返回多个值
    1、用多个变量接收：有多少返回值就用多少变量接收
    2、用一个变量接收：得到一个元组
'''

def func():
    l = ['ls', 'htz']
    for i in l:
        print(i)
        # if i == 'ls': return
result = func()
print(result)


def func1():
    return 1
print(func1())

def func2():
    return 1,2,3
r1 = func2()
print(r1)

r2,r3,r4 = func2()
print(r2,r3,r4)