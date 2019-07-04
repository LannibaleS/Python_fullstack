''''''
'''
字符：
元字符
 
    匹配内容
    . 	匹配除换行符以外的任意字符
    \w	匹配字母或数字或下划线
    \s	匹配任意的空白符
    \d	匹配数字
    \n	匹配一个换行符
    \t	匹配一个制表符
    \b	匹配一个单词的结尾
    ^	匹配字符串的开始
    $	匹配字符串的结尾
    \W	
    匹配非字母或数字或下划线
    \D	
    匹配非数字
    \S	
    匹配非空白符
    a|b	
    匹配字符a或字符b
    ()	
    匹配括号内的表达式，也表示一个组
    [...]	
    匹配字符组中的字符
    [^...]	
    匹配除了字符组中字符的所有字符

量词
    用法说明
    *	重复零次或更多次  0~
    +	重复一次或更多次  1~
    ?	重复零次或一次    0~1
    {n}	重复n次          n
    {n,}	重复n次或更多次  n~
    {n,m}	重复n到m次   n~m

惰性匹配
    量词后面加？
        .*？abc 一直取遇到abc就停
    
    
ret = search('\d(\w)+', 'dawdafa')
ret = search('\d(?P<name>\w)+', 'dawdafa')

找整个字符串，遇到匹配上的就返回，遇不到就none
如果有返回值 ret.group()就可以取到值
区分组中的内容：ret.group(1)、 ret.group('name')


match
从头开始匹配，匹配到了就返回，匹配不到就是None
如果匹配上了 .group()取值

分割split
替换sub，subn
finditer 返回迭代器
compile 编译，正则表达式很长且多次使用

    
    
'''

'''1、匹配标签'''
print('\n ====== 1、匹配标签 ======')
import re


ret = re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>")
#还可以在分组中利用?<name>的形式给分组起名字
#获取的匹配结果可以直接用group('名字')拿到对应的值
print(ret.group('tag_name'))  #结果 ：h1
print(ret.group())  #结果 ：<h1>hello</h1>


ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
#如果不给组起名字，也可以用\序号来找到对应的组，表示要找的内容和前面的组内容一致
#获取的匹配结果可以直接用group(序号)拿到对应的值
print(ret.group(1))
print(ret.group())  #结果 ：<h1>hello</h1>