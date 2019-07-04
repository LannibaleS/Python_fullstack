''''''
'''
method方法
staticmethod 静态方法
classmethod 类方法
类的操作行为
'''

class Goods:
    __discount = 0.5
    def __init__(self, name, price):
        self.name = name
        self.__price = price
    @property
    def price(self):
        return self.__price * Goods.__discount

    @classmethod   # 把一个方法，变成一个类中的方法，这个方法就直接可以被类，不需要依托任何对象
    def change_discount(cls, new_discount):
        cls.__discount = new_discount


apple = Goods('apple', 5)
print(apple.price)
Goods.change_discount(0.25)
print(apple.price)

'''
当这个方法只涉及静态属性的时候，就应该使用classmethod来装饰这个方法
'''

'''
java
'''

# class Login:
#     def __init__(self, name, password):
#




'''
在完全面向对象的过程中，
如果一个函数，既和对象没关系，也和类没关系，
那么就用staticmethod将这个函数变成一个静态方法
'''