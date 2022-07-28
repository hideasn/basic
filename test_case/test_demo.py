# -*- coding: utf-8 -*-

"""
# @Time　 : 2021/12/29 21:12
# @Author : king
# @File　 : test_demo.py
# @project: ApiPytestFramework
# @QQ     : 772084279
# @Email  : 772084279@qq.com
# @blog   : https://ceshizhilu.blog.csdn.net/
"""
import allure
import pytest

from common_utils.allure_step import allure_title
from common_utils.assert_util import assert_result
from request_utils.base_request import BaseRequest
from common_utils.excel_handle import ExcelHandle
from common_utils.api_path import data_path


@allure.feature("登录")
class TestLogin:

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("data", ExcelHandle(data_path + "test_demo1.xlsx").read_excel())
    def test_login(self, data):
        allure_title("正常登录")
        print(data)
        print('sssss')
        # data = {
        #     "title": "正常登录",
        #     "url": "bank/api/login",
        #     "method": "post",
        #     "pk": "data",
        #     "data": {"password": "123456", "userName": "king"}
        # }
        #
        # expected = {
        #     'eq': {'$.code': '0', '$.message': 'success'}
        # }
        # 发送请求
        response = BaseRequest.send_request(data)
        # 断言操作
        assert_result(response, data["validate"])
