import logging

def log(msg):

    # 创建logger，如果参数为空则返回root logger，设置logger日志等级
    logger = logging.getLogger('selenium')
    logger.setLevel(logging.DEBUG)

    # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not logger.handlers:
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

    # return logger

    # 输出不同级别的log
    logger.info(msg)

    # 添加removeHandler语句，每次用完之后移除Handler
    # logger.removeHandler(fh)
    # logger.removeHandler(ch)


# log().debug('this is debug')
# log().info('this is info')
# log().warning('this is warning')
# log().error('this is error')
# log().critical('this is critical')