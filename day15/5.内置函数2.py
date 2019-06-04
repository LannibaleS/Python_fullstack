'''字符串代码的执行'''
exec('123123')
eval('print(2331212)')

print(eval('1+2+3+4')) # eval
print(exec('1+2+3+4')) # exec# 没有返回值

'''
eval和exec都可以执行，字符串类型的代码
exec没有返回值  --- 适合处理有结果的，简单的计算
eval有返回值 --- 适合处理简单的流程

eval一般情况下不让用
eval只能用在你明确知道你要执行的代码是什么，eval会让代码变得简单
'''

code = '''for i in range(10):
    print(i*'*')
'''
exec(code)

'''
compile 将字符串类型的代码编译，代码对象能够通过exec语句来执行，或者eval()进行求职
'''
code1 = 'for i in range(10):print(i)'
compile1 = compile(code1, '', 'exec')
exec(compile1)

code2 = '1+2+3+4'
compile2 = compile(code2, '', 'eval')
print(eval(compile2))


# code3 = 'name = input("please input your name:")'
# compile3 = compile(code3, '', 'single')
# # name
# exec (compile3)
# print(name)

'''
复数 --- complex
实数：有理数：整数，有限循环小数，无限循环小数
     无理数：无限不循环小数，pi
虚数：虚无缥缈的数
5 + 12j === 复合的数 = 复数
'''


''' 
浮点数（有限循环小数，无限循环小数） ！= 小数L：有限循环小数，无限循环小数，无限不循环小数
浮点数
    354.123 = 3.54123*10^2 = 35.4123*10
    


'''

f = 1.86416548763327486456467641314643
print(f)


'''
进制转换

'''
print(bin(10))  # 二进制
print(oct(10))  # 八进制
print(hex(10))  # 十六进制

'''
数学运算
'''
# 绝对值
print(abs(-5))

# divmod除余方法，作用：分页的时候
print(divmod(7,2))
print(divmod(9,5))

# round，取精确值，四舍五入
print(round(3.145986, 3))

# pow，做幂运算
print(pow(2,3))  # 2^3 = 8
print(pow(2,3,3))  # 2^3%3 = 2

# sum(iterable, start)
ret = sum([1,2,3,4], 10)
print(ret)

# min
print(min([1,2,3,4]))
print(min(1,3,4,5))
print(min(1,2,3,-4))
print(min(1,2,3,-4, key=abs))

# max

