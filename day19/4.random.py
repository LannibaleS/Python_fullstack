''''''
'''
random模块


'''

import random
''' #随机小数 大于0且小于1之间的小数'''
print('\n ====== 随机小数 大于0且小于1之间的小数 random.random() ======')
print(random.random())


''' #随机小数 大于1小于3的小数'''
print('\n ====== 随机小数 大于0且小于1之间的小数 random.uniform(1,3) ======')
print(random.uniform(1,3))


''' #随机整数 大于1小于3的小数'''
print('\n ====== 随机整数 大于等于1且小于等于5之间的整数 ======')
print(random.randint(1,5))

print('\n ====== 随机整数 大于等于1且小于10之间的奇数 ======')
print(random.randrange(1,10,2))

''' # 随机选择一个返回 大于1小于3的小数'''
print('\n ====== 随机选择一个返回 1或者23或者[4,5] ======')
print(random.choice([1, [4,5], '23']))

print('\n ====== 随机选择多个返回，返回的个数为函数的第二个参数 列表元素任意2个组合 ======')
print(random.sample([1, '23', [4,5], 'easy'], 3))


print('\n ====== #打乱列表顺序 random.shuffle(item) ======')
item = [1,3,5,7,9,11]
random.shuffle(item)
print(item)

print('\n ====== 生成随机验证码 ======')
'''
0 - 9
chr
[65-90]数字
字母= chr（数字）
随机数字
随意选一个【随机数字，随机字母】
'''
def code():
    code = ''
    for i in range(5):
        num = random.randint(0,9)
        alf = chr(random.randrange(65, 90))
        add = random.choice([num, alf])
        code = ''.join([code, str(add)])
    return code
print(code())


a = '**'.join(['abs', '789'])
print(a)













