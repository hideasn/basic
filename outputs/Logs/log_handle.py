# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : log_handle.py
# @Software: PyCharm
# @time: 2022/7/8 19:05
# @description :
import logging
import os
import time

from common_utils.api_path import all_log_path, error_log_path


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    if not os.path.exists(all_log_path):
        os.makedirs(all_log_path)

    if not os.path.exists(error_log_path):
        os.makedirs(error_log_path)

    all_log_filename = all_log_path + time.strftime("%Y-%m-%d", time.localtime()) + ".log"
    error_log_filename = error_log_path + time.strftime("%Y-%m-%d", time.localtime()) + ".log"

    if not logger.handlers:
        fh = logging.FileHandler(filename=all_log_filename)
        fh.setLevel(logging.DEBUG)
        eh = logging.FileHandler(filename=error_log_filename)
        eh.setLevel(logging.ERROR)                             # 只有发生错误时才会写入error文件
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter("[%(asctime)s]  %(levelname)s %(filename)s [ line:%(lineno)d ] %(message)s",
                                      "%Y-%m-%d %H:%M:%S")
        fh.setFormatter(formatter)
        eh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(eh)
        logger.addHandler(ch)

    return logger


if __name__ == '__main__':
    logger = get_logger(os.path.basename(__file__))
    logger.info("ddddddd")