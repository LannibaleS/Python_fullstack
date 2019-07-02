

import logging
import time
from logging import FileHandler
logger = logging.getLogger()

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('log.log', encoding='utf-8')

# 再创建一个handler，用于输出到控制台
sh = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [line:%(lineno)d] : %(message)s')


# 文件操作符和格式关联
fh.setFormatter(formatter)
sh.setFormatter(formatter1)

# logger对象和文件操作符 关联
logger.addHandler(fh)
logger.addHandler(sh)

logging.debug('logger debug message')
logging.info('logger info message')
logging.warning('logger warning message')
logging.warning('警告错误')
logging.error('logger error message')
logging.critical('logger critical message')

'''
程序的充分解耦
让程序变得高可定制
zabbix

有五种级别的日志记录模式
两种配置方式：basicconfig、log对象

'''