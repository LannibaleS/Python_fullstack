class A:
    def func(self):
        print('A')

class B:
    def func(self):
        print('B')

class C:
    def func(self):
        print('C')

class D(A, B, C):
    pass
    # def func(self):
    #     print('D')

d = D()
d.func()

'''钻石继承问题'''
class A:
    def func(self):
        print('A')

class B(A):
    def func(self):
        print('B')

class C(A):
    def func(self):
        print('C')

class D(B, C):
    pass
    # def func(self):
    #     print('D')

d = D()
d.func()

print('\n小污龟继承问题')
'''小污龟继承问题'''
class F:
    def func(self):
        print('F')

class A(F):pass
    # def func(self):
    #     print('A')

class B(A):pass
    # def func(self):
    #     print('B')

class E(F):
    def func(self):
        print('E')

class C(E):
    def func(self):
        print('C')

class D(B, C):
    pass
    # def func(self):
    #     print('D')

d = D()
d.func()
print(D.mro())  # 继承顺序

'''
新式类中的继承顺序：广度优先
经典类中的继承顺序：深度优先
python2.7 新式类和经典类共存，新式类要继承object
python3 只有新式类，默认继承object
新式类和经典类还有一个区别，super mro方法只在新式类中存在
super只在python3中存在

super的本质：不是单纯的直接找父类，而是根据调用者的节点位置的广度优先顺序来的
'''