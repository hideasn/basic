# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : gen_case.py
# @Software: PyCharm
# @time: 2022/7/20 17:04
# @description :
import os.path
from string import Template
from common_utils.api_path import auto_generate_path

code_template = """
import pytest
import allure

from request_utils.base_request import BaseRequest
from common_utils.assert_util import assert_result
from common_utils.allure_step import allure_title

@pytest.fixture(params=${case_data})
def data(request):
    return request.param

class ${class_name}:

    def ${func_name}(self, data):
        allure_title(data["title"])
        allure.dynamic.feature(data["feature"])
        res = BaseRequest.send_request(data)
        assert_result(res, data["validate"])
"""


def gen_case(case_data, class_name, func_name):
    my_case = Template(code_template).safe_substitute(
        {"case_data": case_data, "class_name": class_name, "func_name": func_name})

    if not os.path.exists(auto_generate_path):
        print(auto_generate_path)
        os.makedirs(auto_generate_path)

    with open(auto_generate_path + func_name + ".py", mode="w", encoding="utf-8") as f:
        f.write(my_case)