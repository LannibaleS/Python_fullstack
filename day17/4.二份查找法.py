''''''
'''
二分查找法：
    必须处理有序的列表
    
'''
l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,67,72,76,82,83,88]
print(len(l))
print(len(l)//2)
# 代码实现
# def find(l, aim):
#     mid_index = len(l)//2
#     if l[mid_index] < aim:
#         new_l = l[mid_index+1 :]
#         find(new_l, aim)
#     elif l[mid_index] > aim:
#         new_l =l[:mid_index]
#         find(new_l, aim)
#     else:
#         print('find!', mid_index, l[mid_index])
#
#
# find(l, 66)

def find(l, aim, start = 0, end = None):
    end = len(l) if end is None else end
    mid_index = (end - start)//2 + start
    if start <= end:
        if l[mid_index] < aim:
            return find(l, aim, start=mid_index+1, end=end)
        elif l[mid_index] > aim:
            return find(l, aim, start=start, end=mid_index-1)
        else:
            # print('find!', mid_index, l[mid_index])
            return mid_index
    else:return 'can not find'
ret = find(l, 44)
print(ret)
# 默认参数用变量，不好
# 67 两次
# 66 好几次
# 44 找不到
# age，二分查找，三级菜单的代码看一遍
# 斐波那契数列 第n个斐波那契数列是多少
# 阶乘 5！= 5*4*3*2*1
# 附加题 用递归实现