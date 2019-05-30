''''''
'''1、处理文件，用户指定要查找的文件和内容，将文件中包含要查找内容的每一行都输出到屏幕'''
def check_file(filename, argument):
    with open(filename, encoding='utf-8') as f: # 句柄：英文翻译来的，handler，拿着这个东西，就可以操作，就叫句柄；文件操作符，文件句柄，文件对象
        for i in f:
            if argument in i:
                yield i

g = check_file('1.复习.py', '迭代器')
for i in g:
    print(i.strip())

print('********************')


'''2、写生成器，从文件中读取内容，在每一次读取到的内容之前加上'***'之后再返回给用户'''
def read_file(filename):
    with open(filename, encoding='utf-8') as f: # 句柄：英文翻译来的，handler，拿着这个东西，就可以操作，就叫句柄；文件操作符，文件句柄，文件对象
        for i in f:
            yield '***'+i

g = read_file('1.复习.py')
for i in g:
    print(i.strip())

