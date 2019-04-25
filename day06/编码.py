'''
ascii
            A : 00000010  8位 一个字节

unicode     A : 00000000 00000001 00000010 00000100 32位  四个字节
            中：00000000 00000001 00000010 00000110 32位  四个字节


utf-8      A :  00100000 8位 一个字节
          中 :  00000001 00000010 00000110 24位 三个字节


gbk        A : 00000110  8位 一个字节
         中  : 00000010 00000110 16位 两个字节

1，各个编码之间的二进制，是不能互相识别的，会产生乱码。
2，文件的储存，传输，不能是unicode（只能是utf-8 utf-16 gbk,gb2312,asciid等）


py3:
    str 在内存中是用unicode编码。
        bytes类型
        对于英文：
             str  ：表现形式：s = 'alex'
                    编码方式： 010101010  unicode
            bytes ：表现形式：s = b'alex'
                    编码方式： 000101010  utf-8 gbk。。。。

        对于中文：
             str  ：表现形式：s = '中国'
                    编码方式： 010101010  unicode
            bytes ：表现形式：s = b'x\e91\e91\e01\e21\e31\e32'
                    编码方式： 000101010  utf-8 gbk。。。。


'''
# s = 'alex'
# s1 = b'alex'
# print(s,type(s))
# print(s1,type(s1))

# s = '中国'
# print(s,type(s))
# s1 = b'中国'
# print(s1,type(s1))

s1 = 'alex'
# encode 编码，如何将str --> bytes, ()  内部将unicode --》 utf-8gbk
s11 = s1.encode('utf-8')
s12 = s1.encode('gbk')
print(s11)
print(s12)
s2 = '中国'
s22 = s2.encode('utf-8')  # b'\xe4\xb8\xad\xe5\x9b\xbd' 6个字节，每个字符用三个字节表示
s23 = s2.encode('gbk')    # b'\xd6\xd0\xb9\xfa' 4个字节 每个字符用两个字节表示
print(s22)
print(s23)
