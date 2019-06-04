
''''''
'''
非常明显的处理一类事物，这些食物都具有相似的属性和功能
当有几个函数，需要反反复复传入相同的参数的时候，就可以考虑面向对象
这些参数都是对象的属性

'''
class work:
    def __init__(self, name, age, sex, do):
        self.name = name
        self.age = age
        self.sex = sex
        self.do = do

    def doing(self):
        # print(self.do)
        # print('{} is walking!'.format(self.name))

        # print('%s, %s岁, %s, %s'%(self.name, self.age, self.sex, self.do))
        print('{}, {}岁, {}, {}'.format(self.name, self.age, self.sex, self.do))

ls = work('ls', 27, 'male', 'favourite fucking')
print(ls.__dict__)
ls.doing()


'''circle 属性 半径'''
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return  pi*self.radius**2

    def perimeter(self):
        return  2*pi*self.radius

circla1 = Circle(3)
area1 = circla1.area()
perimeter1 = circla1.perimeter()
print(area1, perimeter1)

'''
定义类
init方法：
self是什么：self拥有的属性都属于对象
类中可以定义静态属性
类中可以定义方法，方法都有一个必须传的参数self
实例化
实例、对象
对象查看属性
对象调用方法
'''