# dic = {'k':'v'}
# dic['l'] = 's'
# print(dic)

class Foo:
    def __init__(self, name, age, sex):
        self.name = name
        self.sex = sex
        self.age = age

    def __getitem__(self, item):
        if hasattr(self, item):
            return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]


f = Foo('ls', 27, 'male')
print(f['age'])

f['hobby'] = 'playing'
print(f.hobby, f['hobby'])
print(f.__dict__)
del f['hobby']
print(f.__dict__)


print('\n======= new =========')
'''
单例模式：一个 类 始终 只有一个实例
当你第一次实例化这个类的时候，就创建一个实例化的对象
当你之后再来实例化的时候，就用之前创建的对象
'''


