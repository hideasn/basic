# _*_ coding:utf-8 _*_

"""
# @Time　 : 2021/12/28 22:42
# @Author : king
# @File　 : exec_default_func.py
# @project: ApiPytestFramework
# @QQ     : 772084279
# @Email  : 772084279@qq.com
# @blog   : https://ceshizhilu.blog.csdn.net/
"""


def eval_func(func: str) -> str:
    """
    :params func 字符的形式调用函数
    : return 返回的转换成函数执行的结果,已字符串格式返回
    """
    result = eval(f"{func}")
    return str(result)
