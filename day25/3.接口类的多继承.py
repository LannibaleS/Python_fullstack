''''''
'''
tiger 走路 有用
swan 走路 有用 飞
eagle 走路 飞

实现抽象类
from abc import abstractclassmethod, ABCMeta
'''

from abc import abstractclassmethod, ABCMeta
class swim_Animal(metaclass=ABCMeta):
    @abstractclassmethod
    def swim(self):
        pass

class walk_Animal(metaclass=ABCMeta):
    @abstractclassmethod
    def walk(self):
        pass

class fly_Animal(metaclass=ABCMeta):
    @abstractclassmethod
    def fly(self):
        pass

class Animal:
    def walk(self):
        pass
    def swim(self):
        pass
    def fly(self):
        pass

class tiger(walk_Animal, swim_Animal):
    pass

class swan(fly_Animal, walk_Animal, swim_Animal):
    pass

class eagle(fly_Animal, walk_Animal):
    pass

'''
1、多继承问题
在继承抽象类的过程中，我们应当尽量避免多继承
而在继承接口的时候，我们反而鼓励你来多继承接口

接口隔离原则：
使用多个专门的接口，而不使用单一的总接口。即客户端不应该依赖那些不需要的接口
接口类，刚好满足接口隔离原则，是面向对象开发的思想，规范
'''