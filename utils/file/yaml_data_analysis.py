#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/10/9
# @Author: xuef
# @File: yaml_data_analysis.py
# @Desc:

from utils.file.operation_yaml import OperationYaml


class CaseData:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_case(self) -> list:
        """
        获取yaml文件中的用例
        """
        _case_datas = OperationYaml.read_yaml(self.file_path)
        _case_lists = []
        for key, value in _case_datas.items():
            if key != 'info':
                _case_lists.append({key: value})
        return _case_lists






