import logging
from logging.handlers import RotatingFileHandler

def log_test():
    logging.basicConfig(filename='tt.log', level=0,
                        format='%(asctime)s %(name)s %(levelname)s %(module)s %(lineno)s : %(message)s')
    # 过滤掉selenium等级为WARNING以下的日志
    logging.getLogger('selenium').setLevel(logging.WARNING)
    # 打印日志
    logging.debug('this is debug')
    logging.info('this is info')
    logging.warning('this is warning')
    logging.error('this is error')
    logging.critical('this is critical')


def log_rotate():
    # 设置输出日志格式
    format = '%(asctime)s %(name)s %(levelname)s %(module)s %(lineno)s : %(message)s'
    logging.basicConfig(level=0,
                        format='%(asctime)s %(name)s %(levelname)s %(module)s %(lineno)s : %(message)s')
    # 配置RotatingFileHandler
    rotate_handler = RotatingFileHandler(filename='tt.log', maxBytes=1024 * 0.01, backupCount=3)
    # 为handler指定输出格式
    rotate_handler.setFormatter(logging.Formatter(format))
    # 为logger添加的日志处理器
    logging.getLogger().addHandler(rotate_handler)
    # 是否继承父类log信息
    logging.getLogger().propagate=False

    logging.info('my log'*500)


if __name__ == '__main__':
    log_rotate()