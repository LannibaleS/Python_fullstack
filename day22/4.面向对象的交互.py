class Dog:
    def __init__(self, name, blood, aggr, kind):
        self.name = name
        self.hp = blood
        self.aggr = aggr
        self.kind = kind


    def bite(self, person):
        person.blood -= self.aggr


class Person:
    def __init__(self, name, blood, aggr, sex):
        self.name = name
        self.blood = blood
        self.aggr = aggr
        self.sex = sex

    def attack(self):
        pass


ls = Dog('ls', 100, 20, 'teddy')
htz = Person('htz', 1000, 99, 'female')
print(htz.blood)
ls.bite(htz)
print(htz.blood)

