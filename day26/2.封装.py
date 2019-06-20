class Room:
    def __init__(self, name, length, width):
        self.__name = name
        self.__length = length
        self.__width = width

    def get_name(self):
        return self.__name

    def set_name(self, newName):
        if type(newName) is str and newName.isdigit() == False:
            self.__name = newName
        else:
            print('不合法的名字 ')

    def area(self):
        return self.__length * self.__width

ls = Room('ls\'home', 100, 100)
print(ls.area())
ls.set_name('fff')
print(ls.get_name())

'''
假设父类的私有属性，能被子类调用吗
AttributeError: type object 'Foo' has no attribute '_Son__key'

父类的私有属性，不能被子类调用
'''
# class Foo:
#     __key = 123
#
# class Son(Foo):
#     print(Foo.__key)

'''
会用到私有的这个概念的场景
1、隐藏起来一个属性，不想让类的外部调用
2、我想保护这个属性，不想让属性被随意修改
3、我想保护这个属性，不想被子类继承
'''
