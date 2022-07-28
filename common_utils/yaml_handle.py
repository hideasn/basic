# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : yaml_handle.py
# @Software: PyCharm
# @time: 2022/7/19 14:56
# @description :
import os.path
import yaml
from outputs.Logs.log_handle import get_logger

logger = get_logger(os.path.basename(__file__))


class YamlHandle:

    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"{filename}不存在")

    @property
    def read_yaml(self):
        with open(self.filename, encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f.read())
        return yaml_data

