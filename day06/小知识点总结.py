# = 赋值 == 比较值是否相等   is 比较，比较的是内存地址  id(内容)
li1 = [1,2,3]
li2 = li1
li3 = li2
print(id(li1),id(li2))
print(li1,li2,li3)

li3 = [4,5,6]
print(li1,li2,li3)


li1 = [999,5,6]
print(li1,li2,li3)


#数字，字符串 小数据池
#数字的范围 -5 -- 256
#字符串：1，不能有特殊字符
#        2，s*20 还是同一个地址，s*21以后都是两个地址
# i1 = 6
# i2 = 6
# print(id(i1),id(i2))
# i1 = 300
# i2 = 300
# print(id(i1),id(i2))

#剩下的 list dict tuple set 没有小数据池的概念

