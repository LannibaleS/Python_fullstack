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
print(Course.__dict__)

python.language = 'dada'
del python.language
''''''

print(python.language)
print(Course.language)
'''
类中的静态变量 可以被对象和类调用 
对于不可变的数据类型来说，类变量最好用类名操作
对于可变数据类型来说，修改时共享的，重新赋值是独立的
'''



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
print(Foo.count)
f3 = Foo()
print(Foo.count)


''' 认识绑定方法 '''
def func():pass
print(func)

class ls:
    def func1(self):
        print('ls')
f1 = ls()
print(ls.func1)
print(f1)
print(f1.func1)
f1.func1()
''' 绑定方法：当对象使用方法的时候，就是把对象的值传给这个方法，形成了一种绑定关系'''

'''
包 --- init
import package -- 累的实例化过程
'''
import time
print(time.time())