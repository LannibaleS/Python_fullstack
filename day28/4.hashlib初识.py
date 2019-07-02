''''''
'''
登录认证
加密 --》 解密
摘要算法
连个字符串

'''
import hashlib
md5 = hashlib.md5()
md5.update(b'ls1234')
print(md5.hexdigest())

'''
不管算法多么不同，摘要的功能始终不变
对于相同的字符串使用同一个算法进行摘要，得到的值总是不变的
使用不同算法对相同的字符串进行摘要，得到的值应该不同
不管使用什么算法，hashlib的方式永远不变

'''

sha = hashlib.sha1()
sha.update(b'ls14141225')
print(sha.hexdigest())


'''sha算法，随着算法复杂程度的增加，我摘要的时间成本和空间成本都会增加'''

'''
摘要算法的
    1、密码的密文存储
    2、文件的一致性认证
        在下载的时候，检查我们下载的文件和远程服务器上的文件是否一致
        两台机器上的两个文件，你想检查这两个文件是否相等
'''

'''
用户注册
用户 输入用户名、密码
明文的密码进行摘要，拿到一个密文的迷药
写入文件
'''
'''用户登录'''
usr = input('username:')
pwd = input('password:')
with open('userinfo') as f:
    for line in f:
        user, password, role = line.split('|')
        print(user, password, role)
        md5 = hashlib.md5()
        md5.update(bytes(pwd, encoding='utf-8'))
        md5_pwd = md5.hexdigest()
        if usr == user and md5_pwd == password:
            print('success!')


