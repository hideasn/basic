# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : run.py
# @Software: PyCharm
# @time: 2022/7/22 19:28
# @description :
import os
import shutil

import pytest

from common_utils.api_path import auto_generate_path
from common_utils.case_handle import get_case_data


def run():
    # 1.先生成case路径
    if os.path.exists(auto_generate_path):
        shutil.rmtree(auto_generate_path)

    # 2.读取测试数据
    get_case_data()

    # 3.先删除上一次执行生成的报告json临时文件
    if os.path.exists("outputs/reports/"):
        shutil.rmtree(path="outputs/reports/")

    # 4.执行测试用例
    pytest.main(["-vs", "--alluredir=outputs/reports"])

    # 5.本地生成html报告
    os.system('allure generate outputs/reports -o outputs/html --clean')

    # 6.最后删除auto_generate_path路径
    shutil.rmtree(auto_generate_path)


if __name__ == '__main__':
    run()
