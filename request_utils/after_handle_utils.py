# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : after_handle_utils.py
# @Software: PyCharm
# @time: 2022/7/20 16:36
# @description :
import os.path

from outputs.Logs.log_handle import get_logger
from common_utils.data_handle import json_extract, re_extract
from common_utils.global_vars import GLOBAL_VARS

logger = get_logger(os.path.basename(__file__))


def after_extract(response, expr):
    if expr:
        if response_type(response) == "json":
            response = response.json()
            for k, v in expr.items():
                GLOBAL_VARS[k] = json_extract(response, v)
        else:
            response = response.text
            for k, v in expr.items():
                GLOBAL_VARS[k] = re_extract(response, v)


def response_type(response):
    try:
        response.json()
        return "json"
    except ValueError as e:
        return "str"