# -*- coding: utf-8 -*-

"""
# @Time　 : 2021/12/29 20:52
# @Author : king
# @File　 : conftest.py
# @project: ApiPytestFramework
# @QQ     : 772084279
# @Email  : 772084279@qq.com
# @blog   : https://ceshizhilu.blog.csdn.net/
"""

import pytest

from common_utils.case_handle import get_case_data


def pytest_collection_modifyitems(items):
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")


# @pytest.fixture(params=get_case_data())
# def data(request):
#     """用例数据，测试方法参数入参该方法名 excel_cases 即可，实现同样的参数化
#     """
#     return request.param
