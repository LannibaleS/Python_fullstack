'''
'''
'''
什么是抽象类

    与java一样，python也有抽象类的概念但是同样需要借助模块实现，抽象类是一个特殊的类，它的特殊之处在于只能被继承，不能被实例化

为什么要有抽象类

    如果说类是从一堆对象中抽取相同的内容而来的，那么抽象类就是从一堆类中抽取相同的内容而来的，内容包括数据属性和函数属性。

　 比如我们有香蕉的类，有苹果的类，有桃子的类，从这些类抽取相同的内容就是水果这个抽象的类，你吃水果时，要么是吃一个具体的香蕉，要么是吃一个具体的桃子。。。。。。你永远无法吃到一个叫做水果的东西。

    从设计角度去看，如果类是从现实对象抽象而来的，那么抽象类就是基于类抽象而来的。

　 从实现角度来看，抽象类与普通类的不同之处在于：抽象类中有抽象方法，该类不能被实例化，只能被继承，且子类必须实现抽象方法。这一点与接口有点类似，但其实是不同的，即将揭晓答案

在python中实现抽象类
'''

# 对于操作系统来说一切皆文件
import abc #利用abc模块实现抽象类

class All_file(metaclass=abc.ABCMeta):
    all_type='file'
    @abc.abstractmethod #定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        pass

    @abc.abstractmethod #定义抽象方法，无需实现功能
    def write(self):
        '子类必须定义写功能'
        pass

# class Txt(All_file):
#     pass
#
# t1=Txt() #报错,子类没有定义抽象方法

class Txt(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')

class Sata(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')

class Process(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的读取方法')

wenbenwenjian=Txt()

yingpanwenjian=Sata()

jinchengwenjian=Process()

#这样大家都是被归一化了,也就是一切皆文件的思想
wenbenwenjian.read()
yingpanwenjian.write()
jinchengwenjian.read()

print(wenbenwenjian.all_type)
print(yingpanwenjian.all_type)
print(jinchengwenjian.all_type)

'''
抽象类：多继承
一般情况下，单继承，能实现的功能是一样的，所以在父类中可以有一些简单的基础功能
多继承的情况，由于功能比较复杂，所以不容易抽象出相同功能的具体实现，所以写在父类中
'''

'''
抽象类与接口类
抽象类的本质还是类，指的是一组类的相似性，包括数据属性（如all_type）和函数属性（如read、write），而接口只强调函数属性的相似性。

抽象类是一个介于类和接口直接的一个概念，同时具备类和接口的部分特性，可以用来实现归一化设计 

在python中，并没有接口类这种东西，即便不通过专门的模块定义接口，我们也应该有一些基本的概念。

java：
java里所有的类的继承都是单继承，所以抽象类完美的解决了单继承需求中的规范问题
但对于多继承的需求，由于java本身语法的不支持，所以创建了接口Interface这个概念，因为java没有多继承

python
python中没有接口类：
    python当中自带多继承，所以我们直接用class来实现了接口类
    python中支持抽象类：一般情况下，单继承，且能实现python代码
    接口类和抽象类都不能实例化，


'''