# dict

# 数据类型划分： 可变数据类型、不可变数据类型
'''
不可变数据类型： 元祖， bool， int， str  可哈希
可变数据类型：   list， dict， set      不可哈希

dict的key必须是不可变数据类型，可哈希 （tuple int str bool）
value：任意数据类型

dict（二分查找）的优势：
    二分查找去查询，速度快
    存储大量的关系型数据

    特点：无序的
'''

# dic = {
#     'name':['大猛','小孟'],
#     'py9':[{'num':71,'avg_age':18,},
#            {'num': 71, 'avg_age': 18, },
#            {'num': 71, 'avg_age': 18, },
#            ],
#     True:1,
#     (1,2,3):'wuyiyi',
#     2:'二哥',
#
# }
#
# print(dic)

dic1 = {'age': 18, 'name': 'jin', 'sex': 'male',}
print(dic1)

#增：
dic1['height'] = 185  #没有键值对，添加
dic1['age'] = 27      #如果有键，则值覆盖
print(dic1)

dic1.setdefault('weight', 180)  # 有键值对，不做任何改变，没有才添加。
dic1.setdefault('name', 'ls')
print(dic1)

# delete
print(dic1.pop('name'))    # 有返回值，按键去删除
print(dic1.pop('ls', 'no keys'))  # 可设置返回值
print(dic1)

dic1.popitem()  # 随机删除 有返回值 元组里面是删除的键值。
# print(dic1.popitem())
print(dic1)

# del dic1['name'] # 尽量用pop，del会报错

# dic1.clear() #清空字典

print('&&&&&&&&&&&&&&&&&&&&&&&')
# update
dic = {"name":"jin","age":18,"sex":"male"}
dic2 = {"name":"alex","weight":75}
dic2.update(dic)
print(dic)
print(dic2)


print('&&&&&&&&&&&&&&&&&&&&&&&')
print()
# select
# print(dic1['name'])
# print(dic1['name1']) # error

print(dic1.get('name1', 'no keys'))

print(dic1.keys())
print(dic1.values())
print(dic1.items())  # 列表里面套元祖

print('&&&&&&&&&&&&&&&&&&&&&&&')
print()
for i in dic1:
    print(i)

for i in dic1.keys():
    print(i)

for i in dic1.values():
    print(i)


a, b = 1, 2
a, b = b, a
print(a, b)

c, d = [3, 4]
print(c, d)

for keys, values in dic1.items():
    print(keys, values)