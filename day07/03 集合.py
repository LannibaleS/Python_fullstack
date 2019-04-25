'''
集合：可变的数据类型，他里面的元素必须是不可变的数据类型，无序，不重复。
     {}



'''
# set1 = {1,2,3}
#
# set2 = {1,2,3, [2,3], {'name':'ls'}}
# # TypeError: unhashable type: 'list' 集合中必须放可哈希的数据类型，不可变的数据类型
# print(set1)
# print(set2)

set1 = {'alex','wusir','ritian','egon','barry','barry'}

# add
set1.add('ls')
print(set1)

#update
set1.update('abc')
set1.update([1,2,3])
print(set1)


#删除
# set1.pop()  # delete random
# print(set1)
# print(set1.pop())  # 有返回值
# print(set1)
#
# set1.remove('alex')  # 按元素
# print(set1)

# set1.clear()
# print(set1)  # set() 空集合

# del set1
# print(set1)

#查
for i in set1:
    print(i)

print('-------------------------------')

# 交集 {4, 5}
set11 = {1,2,3,4,5}
set22 = {4,5,6,7,8}
print(set11.intersection(set22))
print(set11 & set22)

print('-------------------------------')

# 并集 {1, 2, 3, 4, 5, 6, 7,8}
print(set11 | set22)  # {1, 2, 3, 4, 5, 6, 7,8}
print(set22.union(set11))  # {1, 2, 3, 4, 5, 6, 7}
print(set11.union(set22))


print('-------------------------------')
# 反交集 {1, 2, 3, 6, 7, 8}
print(set11 ^ set22)  # {1, 2, 3, 6, 7, 8}
print(set11.symmetric_difference(set22))  # {1, 2, 3, 6, 7, 8}


# #set11独有的
print(set11 - set22)  # {1, 2, 3}
print(set11.difference(set22))  # {1, 2, 3}

# #set22独有的
print(set22 - set11)  # {8, 6, 7}
print(set22.difference(set11)) # {8, 6, 7}


set111 = {1,2,3,}
set222 = {1,2,3,4,5,6}
print(set111 < set222)
print(set111.issubset(set222))  # 这两个相同，都是说明set1是set2子集
print(set222 > set111)
print(set222.issuperset(set111))  # 这两个相同，都是说明set2是set1超集。

print('-------------------------------')
#去重
li = [1,2,33,33,2,1,4,5,6,6]
set1 = set(li)
print(set1)
print(1 in li)

li1 = []
for i in li:
    if i not in li1:
        li1.append(i)
print(li1)


s = frozenset('ls')  # 将set变成不可变的set
print(s, type(s))