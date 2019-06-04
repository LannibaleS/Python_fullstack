print(dict)
d = {'k':'v'}

print(d)

'''
class 类名：
    属性 = 'a'

print(类名.属性)
类名的作用：操作属性，查看属性
'''


class Person:
    country = 'China'   # 创造了一个只要是这个类就一定有的属性
                        # 类属性 静态属性

    def __init__(self, *args):  # init是初始化方法，self是对象，是一个必须传的参数
                                # self就是一个可以存储很多属性的大字典
        print(self.__dict__)    # 往字典里添加属性的方式发生了一些变化
        self.name = args[0]
        self.hp = args[1]
        self.aggr = args[2]
        self.sex = args[3]
        print(self.__dict__)
        print(id(self))


    def walk(self):             # 方法，类里面的函数一般叫方法。一般情况下必须穿self，且必须要写在第一个，后面还可以穿其他参数，是自由的
        print('{} is walking!'.format(self.name))

print(Person.country)           # 类名 可以查看类中的属性 不需要实例化即可看

ls = Person('ls', 100, 1, 'htz')  # 实例化
print(ls.__dict__)
print(id(ls))
print(ls.name)
Person.walk(ls)
ls.walk()
'''
对象 = 类名()
过程：
    类名()，首先会创建一个对象，创建一个self变量
    调用init方法，类名括号里的参数会被这里接受
    执行init方法
    返回self
    
对象能做的事：
    查看属性
    调用方法
    dict对于对象的属性的增删改查操作都可以用字典操作进行
类名能做的事：
    实例化
    调用方法  Person.walk(self)
    调用类中的属性，也就是调用静态属性
    __dict__ 对于类中的名字只能看，不能修改，不能修改的类的静态属性
    Person.__dict__['country'] = 'dadaw'
'''

print(Person.__dict__['country'])
print(ls.__dict__['name'])
ls.__dict__['name'] = 'sdad'
print(ls.__dict__['name'])


# Person.__dict__['country'] = 'dadaw'
