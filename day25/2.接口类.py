''''''
'''
Java：面向对象编程
设计模式 ---- 接口类
《设计模式》
接口类：python原生不支持
抽象类：python原生支持的

'''
from abc import abstractclassmethod, ABCMeta
'''元类，默认的元类，type'''
class Payment(metaclass=ABCMeta):
    @abstractclassmethod
    def pay(self, money):
        raise  NotImplemented    # 没有实现这个方法

'''
规范：接口类或者抽象类都可以
必须继承ABCMeta
接口类：支持多继承，多继承使用接口类，接口类中所有的方法都必须不能实现 -- java
抽象类：不支持多继承，抽象类中的方法可以有一些代码的实现 --- java

'''

class Wechat(Payment):
    def pay(self, money):
        print('paid {}'.format(money))


class Alipay(Payment):
    def pay(self, money):
        print('paid with alipay {}'.format(money))

class Applepay(Payment):
    def fuqian(self, money):
        print('paid with alipay {}'.format(money))

def pay(pay_obj, money):
    pay_obj.pay(money)

wechat = Wechat()
# pay(wechat, 200)

apple = Applepay()
# pay(apple, 200)