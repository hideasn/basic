# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : global_vars.py
# @Software: PyCharm
# @time: 2022/7/8 18:17
# @description :
from enum import Enum, unique


GLOBAL_VARS = {}


@unique
class CaseEnum(Enum):
    CASE_ID = 1
    CASE_FEATURE = 2
    CASE_TITLE = 3
    API_PATH = 4
    API_HEADER = 5
    API_METHOD = 6
    API_PK = 7
    API_DATA = 8
    API_FILE = 9
    API_EXTRACT = 10
    API_EXPECTED = 11
    API_EXEC = 12


@unique
class CaseTypeEnum(Enum):
    CASE_TYPE_EXCEL = 1
    CASE_TYPE_YAML = 2
    CASE_TYPE_ALL = 0
