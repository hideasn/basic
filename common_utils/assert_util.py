# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : assert_util.py
# @Software: PyCharm
# @time: 2022/7/20 17:09
# @description :
import os.path

from outputs.Logs.log_handle import get_logger
from common_utils.data_handle import json_extract, re_extract
from request_utils.after_handle_utils import response_type

logger = get_logger(os.path.basename(__file__))


def assert_result(res, expected):

    if expected is None:
        logger.info(f"当前用例无断言")
        return

    if isinstance(expected, str):
        expected_dict = eval(expected)
    else:
        expected_dict = expected

    index = 0
    for k, v in expected_dict.items():
        for _k, _v in v.items():
            if _k == "http_code":
                actual = res.status_code
            else:
                if response_type(res) == "json":
                    actual = json_extract(res.json(), _k)
                else:
                    actual = re_extract(res.text, _k)

            index += 1
            logger.info(f"第{index}断言数据, 实际结果:{actual}, 预期结果: {_v}, 断言方式：{k}")

            try:
                if k == "eq":
                    assert actual == _v
                elif k == "gt":   # 大于
                    assert actual > _v
                elif k == "lt":   # 小于
                    assert actual > _v
                elif k == "not":
                    assert actual != _v
                elif k == "in":
                    assert _v in actual
                else:
                    logger.exception(f"判断关键字：{k}错误")
            except AssertionError as e:
                raise AssertionError(f"第{index}个断言失败, 实际结果: {actual}, 预期结果: {_v}, 断言方式: {k}")


