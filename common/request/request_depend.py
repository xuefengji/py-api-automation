#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/7
# @Author: xuef
# @File: request_depend.py
# @Desc: 请求初始化


import os

from config import BaseConfig
from utils.file.operation_yaml import OperationYaml
from common.request.request_send import RequestHandle
from common.request.request_teardown import TearDown
from common.request.request_check import Check
from utils.data.models.model import TestCase


class Depend():

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, yaml_case: TestCase):
        self._case = yaml_case

    #TODO 前置sql数据操作
    def set_up_sql_depend(self):
        pass

    def depend_init(self):
        """
        获取依赖数据

        """
        _is_depends = self._case.is_depend
        _depends_case = self._case.depends_case
        if _is_depends in [True, None]:
            pass
        # _check_data = self._case.case
        # _check_info = self._case.info
        # # check_data = data
        # # check_info = info
        # # check_info['url'] = config.host + check_info['url']
        # # is_run = data['is_run']
        # is_depend = _check_data.is_depend
        # if is_depend:
        #     depends_cases = _check_data.depends_case
        #     for depends_case in depends_cases:
        #         case_id = depends_case.case_id
        #         depends_data = depends_case.depends_data
        #         if case_id == 'sql':
        #             self.set_up_sql_depend()
        #         else:
        #             pass



        # if is_run:
        #     if is_depend:
        #         depends = check_data['depends_data']
        #         for depends_data in depends:
        #             depends_yaml = depends_data['depends_yaml']
        #             depends_case = depends_data['depends_case']
        #             yaml_data = OperationYaml.read_yaml(os.path.join(BaseConfig.data_dir, depends_yaml))
        #             case_info = yaml_data['info']
        #             case_info['url'] = host + case_info['url']
        #             cases = yaml_data['cases']
        #             case_data = cases[int(depends_case)]
        #             if case_data['is_depend']:
        #                 Depend.depend_init(case_info, case_data)
        #             res = RequestSend().send_request(case_info, case_data)
        #             check_data['depends_data'] = TearDown.get_depend_data(res, depends_data)
        #             check_info, check_data = Check.check(check_info, check_data)
        #         res = RequestSend().send_request(check_info, check_data)
        #         return res
        #     check_info, check_data = Check.check(check_info, check_data)
        #     res = RequestSend().send_request(check_info, check_data)
        #     return res





