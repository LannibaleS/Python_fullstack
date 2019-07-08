''''''
'''
文件
 
找到模块
先从sys.module里查看是否已经被导入
如果没有被导入，就一句sys。path路径去寻找模块，
找到了就导入
创建这个模块的命名空间
把文件中的名字都放到命名空间里



'''

import demo

def read():
    print('local read')
money = 200

demo.read()
print(demo.money)

import sys
print(sys.modules.keys())
print(sys.path)