''''''
'''
logging
我能够一键控制
拍错的时候需要打印很多细节来帮助我排错
严重的错误记录下来
有一些用户行为，有没有都要记下来
'''

# import logging
# logging.debug('debug message')          # 低级别 排错信息
# logging.info('info message')            # 正常信息
# logging.warning('warning message')      # 警告信息
# logging.error('error message')          # 错误信息
# logging.critical('critical message')    # 高级别 严重错误信息
#
''' basiccongif 简单 能做的事情相对少
        解决不了中文的乱码问题
        不能同时往屏幕上输出
         
'''
''' 配置log对象 稍微 '''

import logging
from logging import handlers
import time

file_handler = logging.FileHandler(filename='x1.log', mode='w', encoding='utf-8',)
logging.basicConfig(
    # level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    handlers=[file_handler,],
    level=logging.DEBUG
)

logging.debug('logger debug message')
logging.info('logger info message')
logging.warning('logger warning message')
logging.error('logger error message')
logging.critical('logger critical message')
logging.error('你好')