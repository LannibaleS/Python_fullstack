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

class A:
    __instance = False
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        # if not hasattr(cls, '__instance'):
        cls.__instance = object.__new__(cls)
        return cls.__instance

ls = A('ls', 27)
htz = A('htz', 26)
ls.cloth = 'Armani'
print(ls, htz)
print(ls.name, htz.name)
print(ls.cloth, htz.cloth)

print('\n======= eq =========')
'''
eq：判断两个对象是否相等，默认比较两个对象的内存地址，可以重新定制
'''
class B:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else: return False

b1 = B('egg')
b2 = B('egg')
print(b1 == b2)


print('\n======= hash =========')
class C:
    def __init__(self, name, sex):
        self.name = name
        self.sex= sex

    def __hash__(self):
        return hash(self.name + self.sex)

c1 = C('ls', 'male')
c3 = C('ls', 'male')
# c2 = C('htz')
print(hash(c1))
print(hash(c3))
# print(hash(c2))