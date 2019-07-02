'''
'''
'''
只要写递归函数，就必须要有结束条件

返回值
不要只看到return就认为已经返回了。要看返回操作实在递归到第几层的时候发生的，然后返回给了谁
如果不是返回给最外层的函数，调用者就接收不到
需要在分析，看如何把结果返回回来

循环

'''

''' 斐波那契数列 问第n个斐波那契数是多少
    1，1，2，3，5，8
'''
def fib(n):
    if n==1 or n==2:return 1
    return fib(n-1)+fib(n-2)

# print(fib(5))

def fib1(n, l=[0]):
    l[0] += 1
    if n == 2:
        l[0] -= 1
        return 1,1
    else:
        a, b = fib1(n - 1)
        l[0] -= 1
        if l[0] == 0:
            return a+b
        return b, a+b
print(fib1(5))

''' 斐波那契数列 问第n个斐波那契数是多少
    1，1，2，3，5，8
'''
def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)
print(fac(3))