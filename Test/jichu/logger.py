import logging

# 创建logger，如果参数为空则返回root logger，设置logger日志等级
logger = logging.getLogger('selenium')
logger.setLevel(logging.DEBUG)

# 创建handler
fh = logging.FileHandler(filename='tt.log', encoding='utf-8')
ch = logging.StreamHandler()

# 设置输出日志格式
formater = logging.Formatter(fmt='%(asctime)s %(name)s %(levelname)s %(module)s %(lineno)s : %(message)s',
                             datefmt='%Y/%m/%d %X')

# 为handler指定输出格式，注意大小写
fh.setFormatter(formater)
ch.setFormatter(formater)

# 为logger添加的日志处理器
logger.addHandler(fh)
logger.addHandler(ch)

# 输出不同级别的log
logger.debug('this is debug')
logger.info('this is info')
logger.warning('this is warning')
logger.error('this is error')
logger.critical('this is critical')