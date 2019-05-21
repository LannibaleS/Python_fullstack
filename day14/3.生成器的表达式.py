


egg_list = []
for i in range(10):
    egg_list.append(i)
print(egg_list)

# 列表推倒式
egg_list1 = ["egg{}".format(i) for i in range(10)]
egg_list2 = ["egg%s"%i for i in range(10)]
print('egg_list1:', egg_list1)
print('egg_list2:', egg_list2)

'''生成器表达式'''
g = (i for i in range(10))  # 生成器
print(g)
for i in g:print(i)

'''
列表推到式和生成器表达式的区别
括号不一样
返回的值不一样
    生成器表达式几乎不占用内存
'''

chicken = ("egg{}".format(i) for i in range(10))
print(chicken)
for egg in chicken:
    print(egg)


g1 = (i*i for i in range(10)) # g1还没执行呢
print(g1)
'''for循环是一个一个取值，内部相当于调用__next__，每取一次next，for循环才执行一次'''
for i in g1:
    print(i)