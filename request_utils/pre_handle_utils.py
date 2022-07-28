# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : pre_handle_utils.py
# @Software: PyCharm
# @time: 2022/7/8 19:01
# @description :
import os
import re
from outputs.Logs.log_handle import get_logger
from common_utils.yaml_handle import YamlHandle
from common_utils.api_path import config_yaml_path
from common_utils.excel_handle import ExcelHandle
from string import Template
from common_utils.global_vars import GLOBAL_VARS
from common_utils.exec_default_func import eval_func
logger = get_logger(os.path.basename(__file__))


def pre_expr_handle(content):      # content: {"session-token":"$token"}
    if content is None:
        return

    if len(content) != 0:
        logger.info(f"开始进行字符串替换,替换字符串为:{content}")
        content = Template(content).safe_substitute(GLOBAL_VARS)       #  content: {"session-token":"$token"} 没有匹配到$后面的字段名的则不替换，匹配到%字段名的则进行替换
        for func in re.findall(r"\${.*?}", content):                   #  content: {"session-token":"${token}"}
            try:
                content.replace(f"${func}", eval_func(func))
            except Exception as e:
                logger.exception(e)

        logger.info(f"替换字符串完成，替换后字符串为: {content}")

    return content

# '{"session-token":"$token"}' => {"session-token":"$token"}
def str_to_python(content):
    if content is None:
        return None

    if isinstance(content, str) and len(content) != 0:
        return eval(content)
    else:
        return content


class RequestPreDataHandle:

    def __init__(self, request_data):
        self.request_data = request_data
        self.host = YamlHandle(config_yaml_path).read_yaml["host"]

    def _url_handle(self):
        url = self.request_data["url"]
        if url:
            logger.info(f"请求前url: {self.request_data['url']}")
            if url.startswith("http"):
                url = url
            else:
                if self.host.endswith("/") and not url.startswith("/"):
                    url = self.host + url
                elif not self.host.endswith("/") and url.startswith("/"):
                    url = self.host + url
                elif not self.host.endswith("/") and not url.startswith("/"):
                    url = self.host + "/" + url
                else:
                    self.host.endswith("/") and url.starstwith("/")
                    url = self.host.strip("/") + url

            logger.info(f"请求后url: {url}")

        self.request_data["url"] = url

    def _header_handle(self):
        header = self.request_data.get("header")
        if header:
            logger.info(f"处理请求前header为{header}")
            header = str_to_python(pre_expr_handle(header))
            self.request_data["header"] = header
            logger.info(f"处理请求后header为: {header}")

    # 处理请求数据
    def _data_handle(self):
        data = self.request_data.get("data")
        if data:
            logger.info(f"处理请求前data为: {data}")
            data = str_to_python(pre_expr_handle(data))
            self.request_data["data"] = data
            logger.info(f"处理后data为: {data}")

    def _file_handle(self):
        files = self.request_data.get("file")
        logger.info(f"处理请求前files: {files}")

        if files is None:
            return
        """
        {"file":"E:\\学习文档\\QQ截图20211127102844.png"}
        {"file":["E:\学习文档\QQ截图20211127102844.png","E:\学习文档\QQ截图202111271028456.png"]}
        """
        if files != "" and files is not None:
            files = eval(files)
            for k, v in files.items():
                # 多文件上传
                if isinstance(v, list):
                    files = []
                    for path in v:
                        files.append((k, (open(path, "rb"))))          # 为什么要在这里打开
                else:
                    # 单文件上传
                    files = {k, open(v, "rb")}

        self.request_data["file"] = files
        logger.info(f"处理后file为: {files}")

    def _extract_handle(self):
        extract = self.request_data.get("extract")
        if extract:
            logger.info(f"处理前extract: {extract}")
            extract = str_to_python(extract)
            self.request_data["extract"] = extract
            logger.info(f"处理后extract: {extract}")

    def _validate_handle(self):
        validate = self.request_data.get("validate")
        if validate:
            logger.info(f"处理前validate: {validate}")
            validate = str_to_python(validate)
            self.request_data["validate"] = validate
            logger.info(f"处理后validate: {validate}")

    @property
    def pre_request_handle(self):
        self._url_handle()
        self._header_handle()
        self._data_handle()
        self._file_handle()
        self._extract_handle()
        self._validate_handle()

        return self.request_data


if __name__ == '__main__':
    ExcelHandle("../data/test_01.xlsx")