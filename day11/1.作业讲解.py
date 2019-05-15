# 2、写函数，接受n个数字，求这些参数数字的和
def sun_func(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(sun_func(5,6,5,6,4))

# 3、读代码，写出a b c的值
a = 10
b = 20
def test5(a, b):
    print(a, b)  # 20, 10
c = test5(b, a)
print(c)  # None 因为test5没有返回值，所以c为None

# 4、3、读代码，写出a b c的值
a = 10
b = 20
def test5(a, b):
    a = 3
    b = 5
    print(a, b)
c = test5(b, a)  # test5(20,10) 3,5
print(c)  # None