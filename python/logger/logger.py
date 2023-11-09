# -*- coding=utf-8 -*-
""" 
日志记录Logging配置
"""
from logging import basicConfig
from logging import log, debug, info, warn, error, critical

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0


def open_logger():
    """
    开启日志记录器
    设置了基础配置
    """
    level = {
        'log': NOTSET,
        'debug': DEBUG,
        'info': INFO,
        'warn': WARN,
        'error': ERROR,
        'critical': CRITICAL,
    }
    log_file = open('./RECORD.LOG', mode='a', encoding='utf-8')
    basicConfig(stream=log_file, level=level['info'],  # 不应同时指定“stream”和“filename”
                format='%(asctime)s #%(levelname)s#: %(message)s', datefmt='[%Y-%m-%d %A %H:%M:%S]')
    # logging.debug('测试bug记录')
    # logging.info('记录信息')
    # logging.warning('报错警告')
    # logging.error('错误')
    # logging.critical('严重问题')
    # logging.log(2, 'log内容')


def show_msg(msg):
    print(msg)


def set_log(lev, msg):
    """ 等级：0 """
    show_msg(msg)
    return log(lev, msg)


def set_debug(msg):
    """ 等级：10 """
    show_msg(msg)
    return debug(msg)


def set_info(msg):
    """ 等级：20 """
    show_msg(msg)
    return info(msg)


def set_warn(msg):
    """ 等级：30 """
    show_msg(msg)
    return warn(msg)


def set_error(msg):
    """ 等级：40 """
    show_msg(msg)
    return error(msg)


def set_critical(msg):
    """ 等级：50 """
    show_msg(msg)
    return critical(msg)


def test():
    """ 开启日志记录器并设置记录，否则仅有展示效果 """
    open_logger()
    set_info('测试2023-03-13')
