#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/2
# @Author: xuef
# @File: test_login.py
# @Desc:

import os, pytest
from utils.file_utils.operation_yaml import OperationYaml
from config import BaseConfig
from common.request.request_depend import SetUp
from common.request.request_teardown import TearDown


yaml_data = OperationYaml().read_yaml(os.path.join(BaseConfig.data_dir, 'login', 'login.yaml'))
case_data = yaml_data['cases']
case_info = yaml_data['info']



class TestLogin():
    @pytest.mark.parametrize("case_data", case_data)
    def test_login(self, case_data, case_skip, get_host):
        res = SetUp.request_init(case_info, case_data, get_host)
        check_data = TearDown().get_assert_jsonpath(res, case_data['assert'])
        TearDown().assert_actual(check_data)
        # print(type(res))



if __name__ == '__main__':
    pytest.main(['-s','-v',"--alluredir", BaseConfig.allure_report, '--clean-alluredir'])
    os.system('allure generate -c -o {0} {1}'.format(BaseConfig.allure_html_report, BaseConfig.allure_report))
