''''''
'''

字符串 --- 格式化时间：给人看的
时间戳时间 --- float时间，给计算机看的
结构化时间 --- 元组：计算用的

'''

import time

#时间戳
print(time.time())
# 1500875844.800804

#时间字符串
print(time.strftime("%Y-%m-%d %X"))
# '2017-07-24 13:54:37'
print(time.strftime("%Y-%m-%d %H-%M-%S"))
# #'2017-07-24 13-55-04'

#时间元组:localtime将一个时间戳转换为当前时区的struct_time
print(time.localtime())
# time.struct_time(tm_year=2017, tm_mon=7, tm_mday=24,
# 　　　　　　　　　　tm_hour=13, tm_min=59, tm_sec=37, 
#                  tm_wday=0, tm_yday=205, tm_isdst=0)



''' 时间戳和结构化时间 '''
t = time.time()
print(time.localtime(3000000000))
print(time.gmtime(t))
