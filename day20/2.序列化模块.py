''''''
'''
什么叫序列化——将原本的字典、列表等内容转换成一个字符串的过程就叫做序列化。

序列化 --- 都是转向一个字符串数据类型
序列 --- 就是字符串

序列化的目的

1、以某种存储形式使自定义对象持久化；
2、将对象从一个地方传递到另一个地方。
3、使程序更具维护性。

从数据结构 --》 字符串的过程：序列化
从字符串 --》 数据类型的过程：反序列化

json *****
pickle ****
shelve ***

json 
    # 通用的序列化模块
    # 只有很少的一部分数据类型能够通过json转化成字符串

pickle
    # 所有的python中的数据类型都可以转化成字符串类型
    # pickle序列化的内容只有python能理解
    # 且反序列化依赖代码
    
shelve
    # 序列化句柄
    # 使用句柄直接操作，非常方便
    

'''

''' json '''
print('\n ===== json =====')
import json
''' json dumps序列化方法，反序列化loads'''
dic = {'k1':'v1', 1:'中国'}
print(type(dic), dic)
str_d = json.dumps(dic)  # 序列化
print(type(str_d), str_d)

dic_d = json.loads(str_d)
print(type(dic_d), dic_d)

''' 数字、字符串、列表、字典、元祖； 集合不能用json序列化'''

''' json dump load '''
f = open('fff','w', encoding='utf-8')
json.dump(dic, f, ensure_ascii=False)
f.close()


f = open('fff', encoding='utf-8')
res = json.load(f)
f.close()
print(res)

l = [{'k':111}, {'k1':23}, {'k3':456}]
f = open('file', 'w')
for dic in l:
    str_dic = json.dumps(dic)
    f.write(str_dic+'\n')
f.close()

f = open('file')
k = []
for line in f:
    dic = json.loads(line.strip())
    k.append(dic)
f.close()
print(k)


''' pickle dumps loads dump load'''
print('\n ===== pickle 可以序列化任何类型，可以分布dumps =====')
import pickle
dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = pickle.dumps(dic)
print(str_dic)  #一串二进制内容

dic2 = pickle.loads(str_dic)
print(dic2)    #字典

import time
struct_time  = time.localtime(1000000000)
print(struct_time)
f = open('pickle_file','wb')
pickle.dump(struct_time,f)
f.close()

f = open('pickle_file','rb')
struct_time2 = pickle.load(f)
print(struct_time2.tm_year)


''' shelve dumps loads dump load'''
print('\n ===== shelve =====')

'''
shelve也是python提供给我们的序列化工具，比pickle用起来简单一些
shelve只提供给我们一个open方法，使用key来访问的，使用起来和字典类似

这个模块有个限制，就是它不支持多个应用同一时间往同一个DB进行写操作。所以当我们知道我们的应用如果只进行读操作，我们可以让shelve通过只读的方式打开DB


writeback方式有有点也有缺点，有点事减少了我们出错的概率，并且让对象的持久化对用户更加透明了；但是这种方式并不是所有的情况下都需要，首先，使用writeback后，shelve
在open()的时候会增加额外的内存消耗，并且当DB在close()的时候会将缓存中的每一个对象都写入到DB中，这也会带来额外的等待时间。因为shelve没有办法知道缓存中的那些对象修改了，
哪些对象没有修修改，因此所有的对象都会被写入。
'''

import shelve
f = shelve.open('shelve_file')
f['key'] = {'int':10, 'float':9.5, 'string':'Sample data'}  # 直接对文件句柄操作，就可以存入数据
f.close()

f = shelve.open('shelve_file')
existing = f['key']
f.close()
print(existing)


''' 由于shelve在默认情况下是不会纪录待持久化对象的任何修改的，所以我们在shelve.open()的时候需要修改默认参数，否则对象的修改不会保存 '''
# f = shelve.open('shelve_file')
# print(f['key'])
# f['key']['new_value'] = 'ls'
# f.close()

f2 = shelve.open('shelve_file', writeback=True)
print(f2['key'])
# f2['key']['new_value'] = 'ls'
f2.close()