# 导包
import logging.handlers
import logging
from time import strftime

import pytest

"""
TimedRotatingFileHandler:
   filename:日志文件保存的目录及文件名
   when：时间单位，参考该方法的底层实现，比如D表示按天存，S按秒存
   interval：时间间隔
   backupCount：保存的日志文件数量
   """


class LogUtil:

    logger = None

    @classmethod
    def get_logger(cls):
        # 获取日志器
        if cls.logger is None:
            cls.logger = logging.getLogger()  # 必须写入airtest,否则无法过滤airtest模块的日志，但是设定后，无法输出其他模块的日志
            cls.logger.setLevel(logging.DEBUG)  # 设置日志级别
            get_time = strftime("%Y-%m-%d-%H-%M")  # 获取当前时间
            log_name = './log/' + get_time + ' test.log'
            # 获取控制台处理器
            sh = logging.StreamHandler()
            # 设置日志级别
            # sh.setLevel(logging.DEBUG)
            # 获取文件-以时间分隔的处理器
            th = logging.handlers.TimedRotatingFileHandler(filename=log_name,
                                                           when="M",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')
            # 设置日志级别
            # th.setLevel(logging.DEBUG)
            # 设置格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s"
            # 添加格式器
            formatter = logging.Formatter(fmt)
            # 将格式器添加到 处理器 控制台
            sh.setFormatter(formatter)
            # 将格式器添加到 文件-以时间分隔
            th.setFormatter(formatter)
            # 将处理器添加到 日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger

    def write_log(self, message, level):
        """输出日志"""
        logger = self.get_logger()  # 获取日志器
        if level == 'debug':
            logger.debug(message)
        elif level == 'info':
            logger.info(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        elif level == 'critical':
            logger.critical(message)

# if __name__ == '__main__':
#     pytest.main()
#     Log().write_log("22222", "critical")

