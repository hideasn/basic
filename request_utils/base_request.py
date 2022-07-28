# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : base_request.py
# @Software: PyCharm
# @time: 2022/7/20 15:21
# @description :
import requests
from request_utils.pre_handle_utils import RequestPreDataHandle
from request_utils.after_handle_utils import after_extract


class BaseRequest:
    session = None

    @classmethod
    def get_session(cls):
        if cls.session is None:
            cls.session = requests.session()
        return cls.session

    @classmethod
    def send_request(cls, cases):
        request_data = RequestPreDataHandle(cases).pre_request_handle
        response = None
        if request_data:
            response = cls.send_api(
                url=request_data["url"],
                method=request_data["method"],
                pk=request_data["pk"],
                data=request_data.get("data"),
                header=request_data.get("header"),
                file=request_data.get("file")
            )
        after_extract(response, request_data.get("extract", None))
        return response

    @classmethod
    def send_api(cls, url, method, pk, data, header=None, file=None):

        session = cls.get_session()
        pk = pk.lower()
        if pk == "json":
            res = session.request(method=method, url=url, headers=header, files=file, json=data)
        elif pk == "data":
            res = session.request(method, url, data=data, headers=header, files=file)
        elif pk == "params":
            res = session.request(method, url, params=data, headers=header)
        else:
            raise ValueError(f"可选pk为json, data, params,请检查!!!")

        return res
