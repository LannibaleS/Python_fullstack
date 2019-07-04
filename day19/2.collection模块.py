''''''
'''
列表、元组
字典
集合、frozenset
字符串
堆栈：现金后出
队列：先进先出
'''
print('\n ====== namedtuple ======')
from collections import namedtuple
Point = namedtuple('point', ['x','y'])
p = Point(1,2)
print(p.x, p.y)
print(p)

card = namedtuple('card', ['suits', 'number'])
c1 = card('红桃', 2)
print(c1, c1.suits, c1.number)

print('\n ====== deque ======')

