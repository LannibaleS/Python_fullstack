''''''
'''

'''

import re
'''
findall
search
match
'''

''' findall 返回所有的满足匹配条件的结果，放在列表中 '''
print('\n====== findall ======')

ret = re.findall('[a-z]+', 'eva egon dada')
print(ret)

''' search 从前往后，找到一个就返回，返回的变量需要调用group才能拿到结果；如果没有找到，那么返回None，调用group就会报错 '''
print('\n====== search ======')

ret1 = re.search('a', 'eva egon dada')
if ret1: print(ret1.group())

''' match 是从头开始匹配，如果正则规则从头开始就可以匹配上，就返回一个变量
    匹配的内容需要用group才能显示
    如果没匹配上，就返回None，调用group会报错 
'''
print('\n====== match ======')

ret2 = re.match('ev', 'eva egon dada')
if ret2: print(ret2.group())

ret3 = re.split('[ab]', 'abcd')
print('\n====== findall ======')

''' 先按'a'分割，得到' '和'bcd'；再对' '和'bcd'，按'b'分割，得到' ' ，' ' ，'cd' '''
print(ret3)


print('\n====== sub ======')
'''sub 将数字替换成'H'，参数1便是替换一个数字'''
ret4 = re.sub('\d', 'H', 'dawdawf56daw82d2', 1)
print(ret4)


print('\n====== subn ======')
'''subn 将数字替换成'H'，返回元组，（替换的结果，替换了多少次）'''
ret5 = re.subn('\d', 'H', 'dawdawf56daw82d2')
print(ret5)

print('\n====== compile ======')
''' compile讲正则表达式编译成一个正则表达式对象，规则要匹配的是三个数字
    正则表达式对象调用search，参数为待匹配的字符串
    
'''

obj = re.compile('\d{3}')
ret6 = obj.search('abc1234eee')
print(ret6.group())

print('\n====== finditer ======')
''' finditer 返回一个存放匹配结果的迭代器

'''
ret7 = re.finditer('\d', 'dawdaw4354fgv213')
print(ret7)
print(next(ret7).group())
print(next(ret7).group())

for i in ret7:print(i.group())

print('\n====== 匹配身份证号 ======')
''' 匹配身份证号 '''
ret8 = re.search('^[1-9](\d{14})(\d{2}[0-9x])?$', '110108199505073612')
if ret8: print(ret8.group())
print(ret8.group(1))
print(ret8.group(2))


print('\n====== findall的优先级查询 ======')
''' 匹配身份证号 
    这是因为findall会优先把匹配结果组里内容返回，如果想要匹配结果,取消权限即可
'''
ret10 = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
print(ret10)
ret9 = re.findall('www.(?:baidu|oldboy).com', 'www.oldboy.com')
print(ret9)

print('\n====== split的优先级查询 ======')
ret=re.split("\d+","eva3egon4yuan")
print(ret) #结果 ： ['eva', 'egon', 'yuan']

ret=re.split("(\d+)","eva3egon4yuan")
print(ret) #结果 ： ['eva', '3', 'egon', '4', 'yuan']

'''
在匹配部分加上（）之后所切出的结果是不同的，
没有（）的没有保留所匹配的项，但是有（）的却能够保留了匹配的项，
这个在某些需要保留匹配部分的使用过程是非常重要的。
'''

'''

'''