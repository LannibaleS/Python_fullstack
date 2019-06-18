''''''
'''
类里 可以定义两种属性
静态属性
动态属性

'''

class Course:
    language = 'Chinese'

    def __init__(self, teacher, course_name, period, price):
        self.teacher = teacher
        self.name = course_name
        self.period = period
        self.price = price

Course.language = 'English'
python = Course('ls', 'python', '6 months', 20000)
linux = Course('ls', 'linux', '6 months', 20000)

print(Course.__dict__)

python.language = 'dada'
del python.language

Course.language = 'chinese'
''''''

print(python.language)
print(Course.language)

'''
类中的静态变量 可以被对象和类调用 
对于不可变的数据类型来说，类变量最好用类名操作
对于可变数据类型来说，对象名的修改是共享的，重新赋值是独立的
'''

'''模拟人生'''
class Person:
    money = 0

    def work(self):
        Person.money += 1000

mother = Person()
father = Person()
mother.work()
father.work()
print(Person.money)


'''
创建一个类，每实例化一个对象就记录下来
最终所有的对象都共享这个数据
'''
class Foo:
    count = 0
    def __init__(self):
        Foo.count += 1

f1 = Foo()
f2 = Foo()
print(f1.count)
print(f2.count)
f3 = Foo()
print(f3.count)


print('====认识绑定方法====')
''' 认识绑定方法 '''
def func():pass
print(func)

class ls:
    def func1(self):
        print('ls')
f1 = ls()
print(ls.func1)
# print(f1)
print(f1.func1)  # bound method ls.func1 of <__main__.ls object at 0x1036ffdd8
f1.func1()
''' 绑定方法：当对象使用方法的时候，就是把对象的值传给这个方法，f1传给self，形成了一种绑定关系'''

'''
包 --- init
import package -- 类的实例化过程
'''
import time
print(time.time())