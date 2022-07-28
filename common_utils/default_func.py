# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : default_func.py
# @Software: PyCharm
# @time: 2022/7/20 18:56
# @description :
import hashlib
import time


# 当前时间戳
def current_highest():
    """获取当前时间戳"""
    return int(time.time())


# 唯一手机号码
def uniq_phone_num():
    return str(round(time.time()*1000))[:11]


# MD5加密
def md5(string):
    m = hashlib.md5()
    m.update(string.encode("utf-8"))
    # 返回十六进制加密结果
    return m.hexdigest()