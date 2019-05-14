# 函数进阶

# 命名空间和作用域


# 内置命名空间 ---- python解释器
    # 就是python解释器一启动就可以使用的名字，存储在内置命名空间中
    # 内置的名字在启动解释器的时候，被加载进内存里

# 全局命名空间 ---- 我们写的代码但不是函数中的代码
    # 是在程序从上到校被执行的过程中依次加载进内存的
    # 放置了我们设置的所有变量名和函数名

# 局部命名空间 ---- 函数
    # 就是函数内部定义的名字
    # 当调用函数的时候，才会产生这个名称空间，随着函数执行的结束，这个命名空间又消失了

# 在局部：可以使用全局、内置命名空间中的名字
# 在全局：可以使用内置命名空间，但不是能使用局部
# 在内置：不能使用全局和局部的

def max(l):
    print('in max func')
print(max([1,2,3]))
# 在正常情况下，直接使用内置的名字
# 当我们在全局定义了和内置命名空间中同名的名字时，会使用全局的命名
# 当我自己有的时候，就不找我的上级要了
# 如果自己没有，就找上一级要，上一级没有再找上一级，如果内置的命名空间都没有，就报错


# func --》 函数的内存地址
# 函数名（） == 函数的调用
# 函数的内存地址（） == 函数的调用
# 本质：通过函数名找到内存地址，调用内存地址的函数代码



# 作用域
# 全局作用域 --- 作用在全局 --- 内置和全局命名空间的名字全属于全局作用域 ---- globals()可以查看内置，全局，局部
# 局部作用域 --- 作用在局部 --- 函数（局部命名空间中的名字属于局部作用域） --- 使用loclas()就能查看所有局部变量

a = 1
def func():
    global a # 尽量避免使用global，代码不安全
    a += 1
func()
print(a)

# 对于不可变数据类型，在局部可以查看全局作用域中的变量
# 但是不能直接修改
# 想要直接修改，需要在程序的一开始添加global变量
# 如果在一个局部函数内部声明了一个global变量，那么这个变量在局部的所有操作将对全局变量有效

a = 1
b = 2
def func1():
    x = 'aaa'
    y = 'bbb'
    print(locals())

func1()
print(globals())  # 永远打印全局的名字
print(locals())   # locals在什么位置，就打印什么；本地的，locals在全局，打印的和globals一样
'''
    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x103155860>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/lannibales/Downloads/学习视频/Python全栈9期/Python练习/day10/1.函数的命名空间.py', '__cached__': None, 'max': <function max at 0x103614620>, 'a': 1, 'func': <function func at 0x103621158>, 'b': 2, 'func1': <function func1 at 0x1036211e0>}
'''

x = 1
y=5
c = x if x>y else y
print(c)
