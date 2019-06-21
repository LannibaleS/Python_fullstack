''''''
'''
内置的类方法，和内置的函数之间有着千丝万缕的联系

双下方法
obj.__str__  ===  str(obj)
obj.__repr__ ===  repr(obj
'''
print('\n======= str repr =========')
class Teacher:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "Teacher's object : {}".format(self.name)

    def __repr__(self):
        return str(self.__dict__)
        # return self.__dict__

ls = Teacher('ls', '50k')
# a = A()
'''打印一个对象的时候，就是调用a.__str__方法'''
print(ls)

print(repr(ls))
print('>>%r'%ls)

'''
a.__str__ --》 object
object，里面有一个__str__，一旦被调用，就返回调用这个方法的对象的内存地址 

'''

# print('%s:%s'%('A',a))
''' %s str() 直接打印，实际上都是走的__str__'''
''' %r repr() 直接打印，实际上都是走的__rper__'''
''' repr() 是str的备胎，str没有就找repr；str不能是repr的备胎 '''
'''
print（obj）| %s | str（obj）的时候，实际上是内部调用了obj.__str__方法，如果str方法有，那他返回的必定是一个字符串
如果没有str方法，会先找本类中的repr方法，再没有就找父类中的str方法
repr（），只会找__repr__，如果没有找父类
'''

print('\n======= len =========')
class Classes:
    def __init__(self, name):
        self.name = name
        self.student = []

    def __len__(self):
        return len(self.student)

py = Classes('python')
py.student.append('ls')
py.student.append('htz')
py.student.append('122')
print(len(py))


print('\n======= del =========')
class A:
    def __del__(self):
        print('delete')
a = A()
del a
# print(a)

print('\n======= call =========')
class A:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('call')
        for k in self.__dict__:
            print(k, self.__dict__[k])

'''一个对象+()，相当于执行了call()方法'''
a = A('ls')
a()