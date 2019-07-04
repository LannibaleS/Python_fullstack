
''''''
''' 加盐，防止撞库'''
import  hashlib
md5 = hashlib.md5(bytes('salt', encoding='utf-8'))
md5.update(b'123456')
print(md5.hexdigest())

''' 动态加盐，防止撞库'''
import  hashlib
md5 = hashlib.md5(bytes('salt', encoding='utf-8') + b'')
md5.update(b'123456')
print(md5.hexdigest())


'''
做摘要计算的，把字节类型的内容进行摘要处理
md5，sha
md5：正常的md5算法、加盐、动态加盐

文件的一致性校验
文件的一致性校验这里不需要加盐

'''

md5 = hashlib.md5()
md5.update(b'ls')
md5.update(b'1234')
print(md5.hexdigest())