''''''
'''
property
内置装饰器函数，只在面向对象中使用
伪装作用，把方法伪装成属性，让代码看起来更合理

'''
from math import pi
class Circle:
    def __init__(self, r):
        self.r = r

    @property
    def perimeter(self):
        return 2*pi*self.r

    @property
    def area(self):
        return pi*self.r**2

c1 = Circle(5)
print(c1.area)
print(c1.perimeter)


class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    @property
    def bmi(self):
        return self.weight / self.height**2

ls = Person('ls', 1.8, 84.4)
print(ls.bmi)


'''对对象的修改'''
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name + 'sb'

    @name.setter
    def name(self, newName):
        self.__name = newName

tiger = Person('tiger')
print(tiger.name)
tiger.name = 'quanban'
print(tiger.name)

''''''
class Goods:
    discount = 0.5
    def __init__(self, name, price):
        self.name = name
        self.__price = price
    @property
    def price(self):
        return self.__price * Goods.discount

apple = Goods('apple', 5)
print(apple.price)


'''
属性 查看 修改 删除
'''
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.deleter
    def name(self):
        print('deleting')
        del self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

ls = Person('ls')
print(ls.name)
del ls.name
ls.name = 'htz'

print(ls.name)
''' AttributeError: 'Person' object has no attribute '_Person__name' '''