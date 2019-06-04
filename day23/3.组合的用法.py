''''''
'''
面向对象的三大特性：继承 多态 封装
'''

''' 组合 '''
class Dog:
    def __init__(self, name, aggr, hp, kind):
        self.name = name
        self.aggr = aggr
        self.hp = hp
        self.kind = kind

    def bite(self, person):
        person.hp -= self.aggr



class Person:
    def __init__(self, name, aggr, hp, sex, money):
        self.name = name
        self.aggr = aggr
        self.hp = hp
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

    # def hand18(self, person):




ls = Person('ls', 100, 1000, 'male', 0)
dog = Dog('dog', 10, 500, 'teddy')
w = Weapon('打狗棒', 100, 100, 999)
print(ls.__dict__)
ls.money = 1000
ls.get_weapon(w)

print(ls.__dict__)

ls.attack(dog)
dog.bite(ls)

print(dog.__dict__)
print(ls.__dict__)


'''
组合：在一个对象的属性值，是另外一个类的对象
     ls.weapon 是 Weapon类的对象
'''