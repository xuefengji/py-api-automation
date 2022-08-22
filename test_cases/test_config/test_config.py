#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/4 15:10
# @Author: xuef
# @File: test_config.py
# @Desc:


import pytest
from utils.file_utils.operation_yaml import OperationYaml
from config import BaseConfig
from common.request.request_depend import SetUp
from common.request.request_teardown import TearDown


yaml_data = OperationYaml().read_yaml(BaseConfig.data_dir + 'config/config.yaml')
case_data = yaml_data['cases']
case_info = yaml_data['info']


class TestConfig():
    @pytest.mark.parametrize("case_data", case_data)
    def test_config(self,case_data, case_skip):
        res = SetUp.request_init(case_info, case_data)
        check_data = TearDown().get_assert_jsonpath(res, case_data['assert'])
        TearDown().check_actual(check_data)
        # print(type(res))


if __name__ == '__main__':
    if __name__ == '__main__':
        pytest.main(['-s','-v'])