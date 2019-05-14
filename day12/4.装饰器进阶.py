# 带参数的装饰器，三层嵌套的装饰器
# 500个函数
import time
# FLAG = True
FLAG = False
def timmer_out(flag):
    def timmer(func):
        def inner(*args, **kwargs):
            if flag:
                start = time.time()
                ret = func(*args, **kwargs)
                end = time.time()
                print(end - start)
                return ret
            else:
                ret = func(*args, **kwargs)
                return ret
        return inner
    return timmer

# timmer = timmer_out(FLAG)
@timmer_out(FLAG)
def ls():
    time.sleep(0.1)
    print('ls')

@timmer_out(FLAG)
def htz():
    time.sleep(0.5)
    print('htz')

ls()
htz()

print('************************')
# 多个装饰器装饰一个函数
def wrapper1(func):   # func -> f
    def inner1():
        print('wrapper1, before func')
        ret = func()
        print('wrapper1, after func')
        return ret
    return inner1

def wrapper2(func):   # func -> inner1
    def inner2():
        print('wrapper2, before func')
        ret = func()    # func() -> inner1()
        print('wrapper2, after func')
        return ret
    return inner2

def wrapper3(func):   # func -> inner1
    def inner3():
        print('wrapper2, before func')
        ret = func()    # func() -> inner1()
        print('wrapper2, after func')
        return ret
    return inner3

@wrapper3
@wrapper2      # f = wrapper2(f) -> wrapper2(inner1) == inner2
@wrapper1      # f = wrapper1(f) = inner1
def f1():
    print('in f')
    return 'hello world'
print(f1())            # f() -> inner2()



# 使用环境
# 记录用户的登陆情况
# 计算函数执行时间