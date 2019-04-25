

''' list '''
lis = [11,22,33,44,55]
# for i in range(len(lis)):
#     del lis[i]

#  在循环一个列表时，最好不要删除列表中的元素，这样会使索引发生改变，从而报错。


dic = {'k1': 'v1', 'k2':'v2', 'a3':'v3' }

# dic1 = {}
# for i in dic:
#     if 'k' not in i:
#         dic1.setdefault(i, dic[i])
# dic = dic1
# print(dic)

l = []
for i in dic:
    if 'k' in i:
        l.append(i)
print(l)
for i in l:
    dic.pop(i)
print(dic)


# tuple
# tuple里面，只有一个元素，不加逗号，该是什么类型就是什么类型
tu1 = (1)
tu2 = (1,)
print(tu1, type(tu1))
print(tu2, type(tu2))