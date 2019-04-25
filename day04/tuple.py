#元祖 只读列表，可循环查询，可切片。
#儿子不能改，孙子可能可以改。
tu = (1,2,3,'alex',[2,3,4,'taibai'],'egon')

print(tu[3])
print(tu[0:4])

for i in tu:
    print(i)

tu[4][3] = 'ls'
tu[4].append('htz')
print(tu)

# str ----->list   split()
# list -----> str  join()
# join可迭代对象都可以操作，最终返回字符串
# S.join(iterable) -> str
# iterable:str, list, tuple, set 有多个对象的元素，除了int、bool
# Return a string which is the concatenation of the strings in the iterable.
# The separator between elements is S.
s = 'alex'
print('*'.join(s))
# print('$'.join(tu[4]))
print(' love '.join(['ls', 'htz']))


#range 取头不取尾
# for i in range(2, 10):
#     print(i)

# for i in range(2, 10, 2):
#     print(i)
#
# for i in range(10, 0, -1):
#     print(i)

# 什么都没有
# for i in range(0, 10, -1):
#     print(i)
print('*************************************')
# 循环打印列表
li = [1, 2, 3, 5, 'alex', [2, 3, 4, 5, 'taibai'], 'afds']
for i in range(len(li)):    # 7
    if type(li[i]) == list:
        for j in li[i]:
            print(j)

    print(li[i], type(li[i]))


lis = [2,3,'k',['qwe',20,['k',['tt',3,'1']],89],'ab','adv']