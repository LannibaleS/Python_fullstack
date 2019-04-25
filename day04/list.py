li = ['alex',[1,2,3],'wusir','egon','女神','taibai']
l1 = li[0]
print(l1)

l2 = li[0:3]
print(l2)

li = ['alex','wusir','egon','女神','taibai']
#增加 append insert
li.append('ls')
print(li)

# li.insert(4,'春哥')
# print(li)
# li.extend('二哥')
# li.extend([1,2,3])

# while 1:
#     username = input('>>>')
#     if username.strip().upper() == 'Q': break
#     else : li.append(username)
# print(li)


#删
li = ['taibai','alex','wusir','egon','女神',]
name = li.pop(1)  # 返回值 ；alex
print(name, type(name))
print(li)

li.pop()  # 默认删除最后一个
print(li)

li.remove('wusir') # remove first occurrence of value. Raises ValueError if the value is not present.
print(li)

#li.clear() # remove all items from list
# print(li)

# del li
del li[0:2]
print(li)

#改
li = ['taibai','alex','wusir','egon','女神',]
print(li)
li[0] = 'ls'
li[0] = [1,2,3]
print(li)

# slice
li[0:3] = 'lshtz' #把前三个删除，加入新的可迭代元素
print(li)

#查
for i in li:
    print(i)
print(li[0:2])

#公共方法：
print(len(li))

num = li.count('l')
print(num)
print(li.index('s'))

li = [1,5,4,7,6,2,3]
# #正向排序
li.sort()
print(li)

#反向排序
li.sort(reverse=True)
print(li)

#反转
li = [1,5,4,7,6,2,3]
li.reverse()
print(li)

#列表的嵌套
li = ['taibai','武藤兰','苑昊',['alex','egon',89],23]
print(li[1][1])
print(li[0].capitalize())

li[2] = '反日天'
print(li)
print(li[2].replace('反','梁爽'))
li[2] = li[2].replace('反','梁爽')
print(li)

li[3][2] = 100
print(li)