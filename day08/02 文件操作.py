# 读取文件
# f = open(r'模特主妇护士班主任', mode='r', encoding='utf-8')
# content = f.read()
# print(content, type(content))
# print(f, type(f))
# f.close()

# 二进制读取非文字的文件
# f = open(r'模特主妇护士班主任', mode='rb')
# content = f.read()
# print(content)
# f.close()


# 没有文件创建文件，有文件清除重写
# w = open('log', mode='w', encoding='utf-8')
# w.write('ls htz')
# w.close()
#
# s = open('log', mode='wb')
# s.write('dawdadadaw'.encode('utf-8'))
# w.close()

# a = open('log', mode='a', encoding='utf-8')
# a.write('1234')
# a.close()


# f = open('log', mode='r+', encoding='utf-8')
# print(f.read())
# f.write('lllllllll')
# f.close()

#
# f = open('log', mode='r+', encoding='utf-8')
# f.write('aaa')
# print(f.read())
# f.close()

# 功能详解
# f = open('log', mode='r+', encoding='utf-8')
# f.seek(3)  # seek是按照字节定光标的位置， utf-8中文，一个字三个字节，英文一个字母一个字节
# content = f.read(1)  # f.read()读出来的都是字符
# print(content)
# f.close()


# f.tell()  告诉你光标的位置
# f.seek(3) 按照字节定光标的位置

# f = open('log', mode='a+', encoding='utf-8')
# f.write('你好吗')
# count = f.tell()
# f.seek(count-9)
# print(f.read())
# f.close()
#
# f.readable() # 是否可读
# line = f.readline()  # 一行一行的读
# line = f.readlines() # 每一行当成列表中的一个元素，调价到list中
# f.truncate(5)   # 对源文件进行截取


# 可以通过for循环去读取，文件句柄是一个迭代器，他的特点就是每次循环只在内存中占一行的数据，非常节省内存。
# for line in f:
#     print(line)


# 咱们打开文件都是通过open去打开一个文件，其实Python也给咱们提供了另一种方式：with open() as .... 的形式，那么这种形式有什么好处呢？
# 1,利用with上下文管理这种方式，它会自动关闭文件句柄。
with open('log', mode = 'r+', encoding='utf-8') as f1:
    content = f1.read()
    print(content)

# 2，一个with 语句可以操作多个文件，产生多个文件句柄。
with open('log',encoding='utf-8') as f2,\
        open('Test', encoding='utf-8', mode = 'w') as f3:
    f2.read()
    f3.write('老男孩老男孩')
