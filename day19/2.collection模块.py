''''''
'''
列表、元组
字典
集合、frozenset
字符串
堆栈：现金后出
队列：先进先出 FIFO first in first out
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


''' 队列：先进先出 '''
print('\n ====== queue ======')
import queue
q = queue.Queue()
q.put(10)
q.put(16)
q.put(8)
print(q.get())
print(q.get())
print(q.qsize())
print(q.get())
# print(q.get())   # 阻塞
# print(q.qsize())

''' 双端队列：先进先出 '''
'''
使用list存储数据时，按索引访问元素很快，但是'插入'和'删除'元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
'''
print('\n ====== deque ======')
from collections import deque
dq = deque([1,2])
dq.append('a')
dq.appendleft('b')
dq.insert(1,3)
dq.insert(0,9)
print(dq)
print(dq.pop())
print(dq.popleft())
# dq.pop()
# dq.popleft()

'''
deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
'''

''' OrderedDict '''
'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。

如果要保持Key的顺序，可以用OrderedDict：
'''
print('\n ====== OrderedDict ======')
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
# dict的Key是无序的
print(d)
# {'a': 1, 'c': 3, 'b': 2}

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

''' 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序： '''
od1 = OrderedDict()
od1['z'] = 12
od1['A'] = 66
od1['u'] = 3
print(od1.items())


''' defaultdict '''
'''
有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。

即： {'k1': 大于66 , 'k2': 小于66}
'''
print('\n ====== defaultdict ======')
from collections import defaultdict
values = [11, 22, 33,44,55,66,77,88,99,90]
my_dict = defaultdict(list)
for i in values:
    if i > 66:
        my_dict['k1'].append(i)
    else:
        my_dict['k2'].append(i)


d = defaultdict(lambda :5)
print(d.items())
print(d['k'])
print(d['123'])


''' Counter '''
'''
Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。Counter类和其他语言的bags或multisets很相似。
'''
print('\n ====== Counter ======')
from collections import Counter
c = Counter('abcdeabcdabcaba')
print(c)