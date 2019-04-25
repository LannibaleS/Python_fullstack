s = 'wangouxubi'
s1 = s[0]
print(s1)
print(s[2], s[-1], s[-2])

#wang 切片：故头不顾尾
s2 = s[0:4]
print(s2)

s3 = s[0:-1]
print(s3)

s4 = s[:]
print('s4:',s4)

s5 = s[0:]
print('s5:', s5)
# s[:] == s[0:]

s6 = s[0:0]  # 空的
print('s6:', s6)

# wangouxubi
# s[首：尾：步长]
s7 = s[0:5:2]  #wango
print('s7:', s7, 's[0:5]:',s[0:5])

s8 = s[4:0:-1]
print('s[4:0]:', s[4:0], 's8:', s8)

s9 = s[3::-1]
print('s[3:]:', s[3:0], 's9:', s9)

s10 = s[3::-2]
print('s[3:]:', s[3:0], 's10:', s10)

# ibuxuognaw 倒顺序
s11 = s[-1::-1]
print('s[-1::-1]:', s11)

s12 = s[::-1]
print('s[::-1]:', s12)
# s11 = s12 s[-1::-1] == s[::-1]

# str操作
ls = ['12', 'dawdaw', '666']
print('*'.join(ls))

a = 'alexWUsir'
a1 = a.capitalize() # 首字母大写，其他全部格式为小写
print(a1)

a2 = a.upper()
print(a2)

a3 = a.lower()
print(a3)

# s_str = 'qwER1'
# you_input = input('输入验证码，不区分大小写：')
# if s_str.upper() == you_input.upper():
# 	print('success')
# else:
# 	print('error')


a4 = a.swapcase()
print(a4)

# 每个隔开(特殊字符或者数字)的单词首字母大写
a99 = 'alex*egon-wusir'
a5 = a99.title()
print(a5)

a98 = 'fade,crazy*w4rri0r_songsong node_3'
a6 = a98.title()
print(a6)

#居中，空白填充
a7 = a.center(15, '^')
print(a7)

a97 = 'alex\tsir'
a8 = a97.expandtabs()
print(a8)

#以什么开头结尾 endswith
a9 = a.startswith('alex')
print(a9)

a10 = a.startswith('e', 2, 5)
print(a10)

# find 通过元素找索引，找不到返回-1
#
# index通过元素找索引，找不到报错
a11 = a.find('A')
print(a11, type(a11))
# a12 = a.index('A')
# print(a12)

#strip rstrip lstrip
# strip 默认删除前后空格
a96 = 'alexWUsir%'
a13 = a96.strip('%')
print(a13)

a95 = ' *a%lexWUsi* r%'
a14 = a95.strip(' *%')
print(a14)


a94 = 'alexaa wusirl'
a15 = a94.count('al')
print(a15, type(a15))

# split   str ---->list
a93 = ';alex;wusir;taibai'
a16 = a93.split(';')
print(a16)


#format的三种玩法 格式化输出
b = '我叫{}，今年{}，爱好{}，再说一下我叫{}'.format('太白',36,'girl','太白')
print(b)
name = 'ls'
b1 = '我叫{0}，今年{1}，爱好{2}，再说一下我叫{0}'.format(name,36,'girl')
print(b1)
name = 'ls'
b2 = '我叫{name}，今年{age}，爱好{hobby}，再说一下我叫{name}'.format(age=18,name=name,hobby='girl')
print(b2)


k = '1231'
# l = 123s
print(k.isdigit())

# s为字符串
# s.isalnum() 所有字符都是数字或者字母
# s.isalpha() 所有字符都是字母
# s.isdigit() 所有字符都是数字
# s.islower() 所有字符都是小写
# s.isupper() 所有字符都是大写
# s.istitle() 所有单词都是首字母大写，像标题
# s.isspace() 所有字符都是空白字符、\t、\n、\r

# 判断是整数还是浮点数
# a=123
# b=123.123

# >>>isinstance(a,int)
# True
# >>>isinstance(b,float)
# True
# >>>isinstance(b,int)
# False







