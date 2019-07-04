''''''
'''
递归函数
    了解什么是递归：在函数中调用自身函数就是递归函数
    能看懂递归
    能知道递归的应用场景
    初始递归
    算法 - 二分查找法
    三级菜单 - 递归实现
'''

''' 修改最大递归限制 '''
import sys
# sys.setrecursionlimit(10000000)

# n = 0
# def story():
#     global n
#     n += 1
#     print(n)
#     story()
#
# story()
''' RecursionError: maximum recursion depth exceeded while calling a Python object 递归错误，超出了最大递归深度'''

''' 
如果递归次数太多，就不适合用递归来解决问题

递归的缺点：占内存
递归的有点：会让代码变简单
 
'''

def age(n):
    if n == 4:
        return 40
    elif n>0 and n<4:
        return age(n+1)+2
print(age(1))

'''

def age(1):
    if 1 == 4:
        return 40
    elif 1>0 and 1<4:
        return age(1+1)+2    # 44+2=46
        
def age(2):
    if 2 == 4:
        return 40
    elif 2>0 and 2<4:
        return age(2+1)+2    # 42+2=44
        
def age(3):
    if 3 == 4:
        return 40
    elif 3>0 and 3<4:
        return age(3+1)+2    # 40+2=42
        
def age(4):
    if 4 == 4:
        return 40
    elif 1>0 and 1<4:
        return age(1+1)+2

'''