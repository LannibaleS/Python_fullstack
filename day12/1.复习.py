# 复习

# 装饰器进阶
    # functools.wraps
    # 带参数的装饰器
    # 多个装饰器，装饰同一个函数

# 周末作业

# 装饰器
# 开发原则：开放封闭原则
# 装饰器的作用：在不改变原函数调用方式的情况下，在函数的前后添加功能
# 装饰器的本质：闭包函数
def wrapper(func):
    def inner(*args, **kwargs):
        print('在被装饰的函数执行前做的事')
        ret = func(*args, **kwargs)
        print('在被装饰的函数执行后做的事')
        return ret
    return inner

@wrapper  # 内部做的事：holiday = wrapper(holiday)  holiday = inner
def holiday(day):
    print('全体放假{}天'.format(day))
    return 'happy'

ret = holiday(10)  # holiday(10) = inner(10)
print(ret)


'''动态参数'''
''' 接受参数的时候聚合，以元祖的形式
    调用的时候打散
'''
print()
print('动态参数')
def outer(*args):
    print(args)
    print(*args)

    def inner(*args):
        print('inner:', args)
    inner(*args)
outer(1,2,3,4)