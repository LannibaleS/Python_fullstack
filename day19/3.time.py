''''''
'''

字符串 --- 格式化时间：给人看的
时间戳时间 --- float时间，给计算机看的
结构化时间 --- 元组：计算用的

'''

'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
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
struct_time = time.localtime()
print(struct_time.tm_year)
print(time.localtime())
# time.struct_time(tm_year=2017, tm_mon=7, tm_mday=24,
# 　　　　　　　　　　tm_hour=13, tm_min=59, tm_sec=37, 
#                  tm_wday=0, tm_yday=205, tm_isdst=0)



''' 时间戳和结构化时间 '''
print('\n ====== 时间戳 --》 结构化时间 ======')

t = time.time()
print(t)
print(time.localtime()) # 本地时间
print(time.localtime(3000000000))
print(time.gmtime(t))  # 格林威治时间


''' 结构化时间用 time.localtime() 获取'''
print('\n ====== 结构化时间 --》 时间戳 ======')

print(time.mktime(time.localtime()))


''' 格式化时间用 time.strptime 转化为结构化时间'''
print('\n ====== 格式化时间 --》 结构化时间 ======')
print(time.strptime('2000-12.31', '%Y-%m.%d'))


''' 结构化时间用 time.strftime 转化为格式化时间'''
print('\n ====== 结构化时间 --》 格式化时间 ======')
print( time.strftime('%m/%d/%y %H:%M:%S',time.localtime()))
# print(time.strptime('2000-12.31', '%Y-%m.%d'))


'''
#结构化时间 --> %a %b %d %H:%M:%S %Y串
#time.asctime(结构化时间) 如果不传参数，直接返回当前时间的格式化串
'''
print('\n ====== asctime ======')
print(time.asctime(time.localtime()))
print(time.asctime())

print(time.ctime())


'''
#结构化时间 --> %a %b %d %H:%M:%S %Y串
#time.asctime(结构化时间) 如果不传参数，直接返回当前时间的格式化串
'''
print('\n ====== 练习题 ======')
import time
true_time=time.mktime(time.strptime('2017-09-11 08:30:00','%Y-%m-%d %H:%M:%S'))
time_now=time.mktime(time.strptime('2017-09-12 11:00:00','%Y-%m-%d %H:%M:%S'))
print(time.ctime(true_time))
time1 = time_now - true_time
print(time1)
# print(time.ctime(time))
print(time.gmtime(time1))

struct_time = time.gmtime(time1)
print(struct_time)
print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year-1970,struct_time.tm_mon-1,
                                       struct_time.tm_mday-1,struct_time.tm_hour,
                                       struct_time.tm_min,struct_time.tm_sec))

