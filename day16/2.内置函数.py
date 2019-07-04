# reversed（）  列表反转
l = [1,2,3,4,5]
l.reverse()
print(l)

l2 = reversed(l)
print(l2)
for i in l2:
    print(i)

'''
保留愿列表，产生一个反序的迭代器
'''

''' slice '''
l1 = (1,2,3,4,5,4,65,4,654,876,98765)
sli = slice(0,5,2)
print(l1[sli])
print(l1[0:5:2])


''' str '''


''' 内置函数——format 
说明：
　　1. 函数功能将一个数值进行格式化显示。

　　2. 如果参数format_spec未提供，则和调用str(value)效果相同，转换成字符串格式化。


'''

#字符串可以提供的参数,指定对齐方式，<是左对齐， >是右对齐，^是居中对齐
print(format('test', '<20'))
print(format('test', '>20'))
print(format('test', '^20'))

''' bytes 
1、转换成bytes类型 
2、网络编程，只能传二进制
3、打开文件，读写文件
4、照片和视频也是以二进制存储
5、html网页爬取到的也是编码
'''

bytes()

''' 拿到的是gbk编码的，我想转化成utf8   '''
print(bytes('你好', encoding='GBK'))
print(bytes('你好', encoding='GBK').decode('GBK'))   # unicode转化成Gbk的bytes
# print(bytes('你好', encoding='GBK').decode('utf-8'))
print(bytes('你好', encoding='utf-8'))    # unicode转化成utf-8的bytes


print(bytes(b'\xc4\xe3\xba\xc3').decode('GBK'))



''' bytearray '''
print('====== bytearray ======')
b_array = bytearray('你好', encoding='utf-8')
print(b_array)
print(b_array[0])



''' memoryview 
切片 --- 字节类型的切片 不占内存
字符串 --- 占空间
'''

''' ord 字符串按照unicode转数字 '''
print('\n====== ord ======')

print('A', ord('A'))
print('a', ord('a'))
print('1', ord('1'))

''' chr 数字按照unicode转字符 '''
print('\n====== chr ======')
print('97', chr(97))

''' ascii 只要是ascii码中的内容，就打印出来，不是就转化成\\u '''
print('\n====== ascii ======')
print(ascii('123'))


''' repr '''
print('\n====== repr ======')
name = 'dada'
print('你好%r'%name)
print(repr('13'))
print(repr(1231))

''' all 判断是否有bool值为 false 的值'''
print('\n====== all ======')
print(all(['a', '1', 123]))
print(all(['1', 123, False]))


''' any 判断是否有bool值为 True 的值'''
print('\n====== any ======')
print(any(['1', 0]))



