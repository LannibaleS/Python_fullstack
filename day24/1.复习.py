''''''
'''
面向对象编程
思想：角色的抽象，创建类，创建角色（实例化的过程），操作这些实例

面向对象的关键字：class
self是一个对象，里面存储的是字典

已经加载类的变量

class 类名
    静态属性 = 'asda'
    def __init__(self):pass
    
类名.静态属性  --- 存储在类的命名空间里
对象 = 类名() --- 实例化：创建了一个self对象，执行init方法，返回self对象给外部

类名.方法()
对象.属性
对象.方法()

对象可以使用静态变量吗？       True
类可以使用对象里的属性吗？  False

'''

'''
组合：一个类的对象是另外一个类对象的属性
'''
class A:
    def __init__(self):
        self.name = 'ls'

class B:
    def __init__(self, year, month ,day):
        self.year = year
        self.month = month
        self.day = day

b = B(1992,4,13)
a = A()
a.birth = b
print(a.birth.year)
