

'''
'''

'''
组合：表达的是，什么有什么的关系
    一个类的属性，是另一个类的对象
'''

class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

python = Course('python', 20000, '6 months')

class Classes:
    def __init__(self, name, course):
        self.name = name
        self.course = course

py9 = Classes('python_s9', python)
print(py9.course.name)


'''
命名空间：类和对象分别存在不同的命名空间中

继承：
    单继承：****
        父类（超类，基类）
        子类（派生类）：派生方法和派生属性
        子类的对象在调用方法和属性：先用自己的，自己没有，采用父类的
    多继承： ***
        不会超过三个父类，不要超过三层
        如果子类自己有就用自己的，如果没有就用离子类最近的那个父类的方法
        接口类和抽象类： **
        经典类和新式类的继承规则不同，经典类是深度优先，新式类是广度优先 *****（面试）
    super只能在python3中使用
        super是根据mro广度优先顺序找上一个类

多态： （面试）
    多态和鸭子类型
封装：*** 面试
    私有的
    __名字
    只能在类的内部调用，子类都无法调用
    
三个装饰器：
    @property       **** 规范，面试  @name.setter
    @staticmethod   ***
    @classmethod    *****  当一个方法只使用了类的静态变量时，就给这个方法加上@classmethod装饰器，默认传cls参数
    



'''