# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : case_handle.py
# @Software: PyCharm
# @time: 2022/7/20 17:53
# @description :
import os

from common_utils.yaml_handle import YamlHandle
from common_utils.api_path import config_yaml_path
from common_utils.global_vars import CaseTypeEnum
from common_utils.excel_handle import ExcelHandle
from common_utils.api_path import data_path
from common_utils.gen_case import gen_case


def get_case_data():
    case_type_ = YamlHandle(config_yaml_path).read_yaml["case_type"]
    if case_type_ == CaseTypeEnum.CASE_TYPE_EXCEL.value:
        cases = []
        for execl_path in [path for path in os.listdir(data_path) if os.path.splitext(path)[1] == ".xlsx"]:
            case_data = ExcelHandle(data_path + execl_path).read_excel()
            func_name = os.path.splitext(execl_path)[0]
            class_name = func_name.split("_")[0].title() + func_name.split("_")[1].title()
            gen_case(case_data, class_name, func_name)
            cases.extend(case_data)

        return cases
    elif case_type_ == CaseTypeEnum.CASE_TYPE_YAML.value:
        cases = []
        for yaml_path in [path for path in os.listdir(data_path) if os.path.splitext(path)[1] in [".yaml", ".yml"]]:
            case_data = YamlHandle(data_path + yaml_path).read_yaml
            func_name = os.path.splitext(yaml_path)[0]
            class_name = yaml_path.split("_")[0].title() + yaml_path.split("_")[1].title()
            gen_case(case_data, class_name, func_name)
            cases.extend(case_data)

        return cases
    else:
        cases = []
        for file in [excel for excel in os.listdir(data_path) if
                     os.path.splitext(excel)[1] in [".yaml", ".yml", ".xlsx"]]:
            if os.path.splitext(file)[1] == ".xlsx":
                data = ExcelHandle(data_path + file).read_excel()
                name = os.path.splitext(file)[0]
                cases.extend(data)
            else:
                data = YamlHandle(data_path + file).read_yaml
                name = os.path.splitext(file)[0]
                cases.extend(data)

            class_name = name.split("_")[0].title() + name.split("_")[1].title()
            gen_case(name, data, class_name)
        return cases