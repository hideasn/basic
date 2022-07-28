# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : basic
# @File : allure_step.py
# @Software: PyCharm
# @time: 2022/7/22 19:13
# @description :
import json

import allure


def allure_title(title):
    allure.dynamic.title(title)


def allure_step(step_title, content):
    with allure.step(step_title):
        allure.attach(json.dumps(content, ensure_ascii=False, indent=4), step_title, allure.attachment_type.JSON)