#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/9
# @Author: xuef
# @File: conftest.py
# @Desc:

import os
import pytest
import requests

from config import BaseConfig
from utils.config_utils.config_control import ConfigGet
from utils.file_utils.operation_cache import OperationCache
from utils.file_utils.operation_json import OperationJson


def pytest_terminal_summary(terminalreporter):
    """统计测试结果"""
    data = {
        "total": terminalreporter._numcollected,
        "passed": len(terminalreporter.stats.get('passed', [])),
        "failed": len(terminalreporter.stats.get('failed', [])),
        "error": len(terminalreporter.stats.get('error', [])),
        "skipped": len(terminalreporter.stats.get('skipped', [])),
        "pass_rate": 0.0
    }
    if data['total'] > 0 :
        data['pass_rate'] = round(data['passed'] / data['total'], 2) * 100
    OperationJson.write_json(data, os.path.join(BaseConfig.report_dir, 'summary.json'))



@pytest.fixture(scope="function")
def case_skip(case_data):
    """处理跳过用例"""
    if case_data['is_run'] is False:
        pytest.skip()


@pytest.fixture(scope="session", autouse=True)
def get_host():
    return ConfigGet.get_host()

# @pytest.fixture(scope="session", autouse=True)
# def token_init():
#     url = 'https://127.0.0.1/auth/token'
#     data = {'username': 'admin', 'password': '123456'}
#     headers={'Content-Type': 'application/json'}
#     res = requests.post(url=url, json=data, headers=headers)
#     OperationCache.write_cache(BaseConfig.cache_dir+'token', res.json()['data']['token'])


