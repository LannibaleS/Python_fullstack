''''''
'''
【封装】

         隐藏对象的属性和实现细节，仅对外提供公共访问方式。

【好处】 

1. 将变化隔离； 

2. 便于使用；

3. 提高复用性； 

4. 提高安全性；

【封装原则】

      1. 将不需要对外提供的内容都隐藏起来；

      2. 把属性都隐藏，提供公共方法对其访问。
      
广义上面向对象的封装：代码的保护，面向对象的思想背身就是一种
只让自己的对象能调用自己类中的方法

狭义上的封装 --- 面向对象的三大特性之一
属性 和 方法都藏起来，不让别人看见

'''

class Person:
    __key = 123   # 私有静态属性
    def __init__(self, name, password):
        self.name = name
        self.__password = password  # 私有属性

    def get_pwd(self):      # 私有方法
        print(self.__dict__)
        return self.__password  # 只要在类的内部使用私有属性，就会自动的带上"_类名"

    def login(self):    # 正常的方法调用私有方法
        self.__get_pwd()

ls = Person('ls', '2131')
print(ls._Person__password)   # _类名__属性名
print((ls.get_pwd()))


'''
所有的私有，都是在变量的左边加上双下划线
    对象的私有属性
    类中的私有方法
    类中的静态属性
所有的私有的，都不能再类的外部使用

public protect private
'''

