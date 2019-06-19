
# 父类，基类，超类
class A:
    pass

class B:
    pass

# 子类，派生类
class A_son(A, B):
    pass


class AB_son(A, B):
    pass

'''
一个类可以被多个类继承
一个类，可以继承多个类 --- python里独有的多继承
'''
# 查看继承
# __base__只查看从左到右继承的第一个子类，__bases__则是查看所有继承的父类
print(A_son.__bases__)

'''
(<class 'object'>,)
python3里，所有的类都有父类，默认继承object，任何没有父类的类，都继承与(<class 'object'>,)，object是所有类的祖宗
python3中的类，叫做新式类
'''
print(A.__bases__)

class Animal:
    def __init__(self, name, aggr, hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp

class Dog(Animal):
    def bite(self, person):
        person.hp -= self.aggr

class Person(Animal):
    pass

jin = Dog('kim', 200, 500)
ls = Person('ls', 1000, 999)
jin.bite(ls)
print(ls.hp)

'''
狗类 吃、喝、看门
鸟类 吃、喝、下蛋
'''
class Animal:
    def __init__(self):
        print('执行Animal.__init__')
        self.func()
    def eat(self):
        print('{} eating'.format(self.name))
    def drink(self):
        print('{} drink'.format(self.name))
    def func(self):
        print('Animal.func')

class Dog(Animal):
    def guard(self):
        print('guarding')
    def func(self):
        print('Dog.func')

dog = Dog()


''''''
class Animal:
    def __init__(self, name, aggr, hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp

    def eat(self):
        print('{} huixue!'.format(self.name))

class Dog(Animal):
    def __init__(self, name, aggr, hp, kind):
        Animal.__init__(self, name, aggr, hp)
        self.kind = kind   # 派生属性

    def bite(self, person): # 派生方法
        person.hp -= self.aggr

    def eat(self):
        Animal.eat(self)
        super().eat()
        '''如果既想实现新的功能，也想使用父类原本的功能，还需要在子类中再调用父类'''
        self.tooth = 2



class Person(Animal):
    def __init__(self, name, aggr, hp, sex, money):
        Animal.__init__(self, name, aggr, hp)
        self.sex = sex
        self.money = money

    def attack(self, dog):
        dog.hp -= self.aggr

    def get_weapon(self, weapon):
        if self.money >= weapon.price:
            self.money -= weapon.price
            self.weapon = weapon
            self.aggr += weapon.aggr
        else:
            print('money is not enough!')


class Weapon:
    def __init__(self, name, aggr, njd, price):
        self.name = name
        self.aggr = aggr
        self.price = price
        self.njd = njd

    def hand18(self, person):
        if self.njd > 0:
            person.hp -= self.aggr*2
            self.njd -= 1

abc = Dog('abc', 20, 99, 'teddy')
print(abc.name)

ls = Person('ls',30,999,'male', 10)
ls.eat()

abc.eat()
print(abc.tooth)

'''
父类中没有的属性，在子类中出现叫做派生属性
父类中没有的方法，在子类中出现，叫做派生方法
只要是子类的对象调用，子类中有得名字，一定用子类的，子类中没有才用父类的，如果父类也没有报错
如果父类，子类都有，用子类的
    如果想用父类的，单独调用父类，
    1、父类名.方法名 需要传自己的self参数
    2、super().方法名 不需要穿自己的self
    
正常的代码中，单继承 == 减少了代码的重复，用单继承
继承表达式是一种，子类是父类的关系
'''
print()
print('super')
class Animal:
    def __init__(self, name, aggr, hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp

    def eat(self):
        print('{} huixue!'.format(self.name))

class Dog(Animal):
    def __init__(self, name, aggr, hp, kind):
        super().__init__(name, aggr, hp)   # 只在新式类中才有，python3中所有的类都是新式类
        self.kind = kind   # 派生属性

    def bite(self, person): # 派生方法
        person.hp -= self.aggr

    def eat(self):
        Animal.eat(self)
        super().eat()
        '''如果既想实现新的功能，也想使用父类原本的功能，还需要在子类中再调用父类'''
        self.tooth = 2
        print('dog eating')

jin = Dog('jin', 1, 5, 'teddy')
jin.eat()
super(Dog, jin).eat()