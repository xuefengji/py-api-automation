#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/1
# @Author: xuef
# @File: __init__.py
# @Desc:

import os


class BaseConfig:
    """
    兼容windows、Linux的平台
    """
    _sep = os.sep
    # 项目路径
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + _sep).split('config')[0]
    # 环境配置文件
    environment_dir = os.path.join(root_dir, 'config' , 'environment.yaml')
    #项目配置
    setting_dir = os.path.join(root_dir, 'config' , 'setting.yaml')
    # 用例路径
    case_dir = os.path.join(root_dir, 'test_case' )
    # 测试用例数据路径
    data_dir = os.path.join(root_dir, 'datas')

    cache_dir = os.path.join(root_dir, 'cache_utils')
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)

    log_dir = os.path.join(root_dir, 'logs')

    # 测试报告路径
    report_dir = os.path.join(root_dir, 'reports')
    # if not os.path.exists(report_dir):
    #     os.mkdir(report_dir)
    # 测试报告中的 allure 报告路径
    allure_report = os.path.join(report_dir, "allure_report")
    allure_html_report = os.path.join(report_dir, 'allure_html_report')




if __name__ == '__main__':
    print(BaseConfig.allure_html_report)