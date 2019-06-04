

a = {'1':1, '2':2}
b = a
a['1'] = 5
sum = a['1']+b['1']
print(sum)


# not and or
# acsii A=65 a=97 小写的一定比大写的大
print(True and True)  # True
print(True and 1)     # 1


print('abc'>'xyz')   # 字符串可以比大小，以首字母的大小为准
print(0x56>56)
# 元祖不能比较大小


'''
复数：
    语法real+imagj
    实部和虚部都是浮点数
    虚部必须后缀为j且j不区分大小写
    方法conjugate返回附属的共轭复数
'''
z = 4+5j
print(z)
print(z.conjugate())
print(z.real,z.imag)

