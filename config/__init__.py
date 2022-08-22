#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/1
# @Author: xuef
# @File: __init__.py
# @Desc:

import os

from utils.file_utils.operation_yaml import OperationYaml


class BaseConfig:
    """
    兼容windows、Linux的平台
    """
    _sep = os.sep
    # 项目路径
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))+ _sep).split('config')[0]
    # 环境配置文件
    environment_dir = os.path.join(root_dir, 'config' + _sep + 'environment.yaml')
    #项目配置
    setting_dir = os.path.join(root_dir, 'config' + _sep + 'setting.yaml')
    # 用例路径
    case_dir = os.path.join(root_dir, 'test_case' + _sep)
    # 测试用例数据路径
    data_dir = os.path.join(root_dir, 'datas' + _sep)

    cache_dir = os.path.join(root_dir, 'cache' + _sep)
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)

    log_dir = os.path.join(root_dir, 'logs' + _sep)

    # 上传的文件路径
    file_dir = os.path.join(root_dir, 'files' + _sep)

    util_dir = os.path.join(root_dir, 'utils' + _sep)
    util_install_dir = util_dir + 'otherUtils' + _sep + 'InstallUtils' + _sep
    # 测试报告路径
    report_dir = os.path.join(root_dir, 'reports'+ _sep)
    # if not os.path.exists(report_dir):
    #     os.mkdir(report_dir)
    # 测试报告中的 allure 报告路径
    allure_report = os.path.join(report_dir, "allure_report"+_sep)
    allure_html_report = os.path.join(report_dir, 'allure_html_report'+_sep)
    # 测试报告中的test_case路径
    report_html_test_case_dir = os.path.join(root_dir, 'reports' + _sep +
                                             "html" + _sep + 'data' + _sep + "test-cases" + _sep)

    # 获取环境地址
    @classmethod
    def get_environment(cls, environment:str) -> str:
        env = OperationYaml.read_yaml(BaseConfig.environment_dir)
        if environment == 'test':
            return env['test']['host']
        return env['test']['host']

if __name__ == '__main__':
    print(BaseConfig.root_dir)