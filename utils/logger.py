import logging


def get_logger(log_name, level=logging.INFO):
    """
    获取日志对象
    Args:
        :param log_name: string 日志对象名，即日志文件名
        :param level:  输出级别，写入级别为WARING
    Return:
        :return: 日志对象
    """
    # 创建一个logger
    logger = logging.getLogger(log_name)
    # 设置日志级别
    logger.setLevel(level)

    # 创建文件处理器
    file_handler = logging.FileHandler("../log/"+log_name.upper()+".log")
    file_handler.setLevel(logging.INFO)
    # 创建输出处理器
    stream_handler = logging.StreamHandler()

    # 定义输出格式
    formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s:%(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # 给logger添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

if __name__ == '__main__':
    logger = get_logger('log')
    logger.warning('warn message')
    logger.info('info message')
    logger.debug('debug message')