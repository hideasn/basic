# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : data_handle.py
# @Software: PyCharm
# @time: 2022/7/20 16:02
# @description :
import json
import os.path
import re

from jsonpath import jsonpath
from outputs.Logs.log_handle import get_logger

logger = get_logger(os.path.basename(__file__))


# jsonpath提取器
def json_extract(response, expr="."):          # .默认全部提取
    try:
        result = jsonpath(response, expr)[0]
        logger.info(f"提取响应内容成功,提取表达式为: {expr}, 提取值为: {result}")
    except Exception as e:
        logger.exception(e)
        logger.info(f"未提取到内容,请检查表达式是否错误,提取表达式为: {expr}")
        result = None

    return result


# 正则提取器
def re_extract(response, expr="."):
    try:
        result = re.findall(expr, response)[0]
        logger.info(f"提取响应内容成功,提取表达式为: {expr}, 提取值为: {result}")
    except Exception as e:
        logger.exception(e)
        logger.info(f"未提取到内容,请检查表达式是否错误,提取表达式为: {expr}")
        result = None

    return result
