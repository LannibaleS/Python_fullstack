
from functools import wraps

def wrapper(func):   # func = holiday
    @wraps(func)     #
    def inner(*args, **kwargs):
        print('在被装饰的函数执行前做的事')
        ret = func(*args, **kwargs)
        print('在被装饰的函数执行后做的事')
        return ret
    return inner

@wrapper  # 内部做的事：holiday = wrapper(holiday)  holiday = inner
def holiday(day):
    '''放假通知'''
    print('全体放假{}天'.format(day))
    return 'happy'

ret = holiday(10)  # holiday(10) = inner(10)
print(ret)

print('__holiday_name__')
print(holiday.__name__)
print(holiday.__doc__)

def ls():
    '''
    ls htz
    '''
    print('ls')

print(ls.__name__)
print(ls.__doc__)