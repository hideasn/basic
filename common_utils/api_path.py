# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : api_path.py
# @Software: PyCharm
# @time: 2022/7/19 13:40
# @description :
import os

root_path = os.path.dirname(os.path.dirname(__file__))

all_log_path = root_path + os.sep + "outputs\\Logs\\interface_log\\all_Logs" + os.sep

error_log_path = root_path + os.sep + "outputs\\Logs\\interface_log\\error_Logs" + os.sep

config_yaml_path = root_path + os.sep + "config\\config.yaml"

auto_generate_path = root_path + os.sep + "generate_case" + os.sep

data_path = root_path + os.sep + "data" +os.sep