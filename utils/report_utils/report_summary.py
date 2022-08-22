#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/10
# @Author: xuef
# @File: report_summary.py
# @Desc:
import os
from utils.file_utils.operation_json import OperationJson
from config import BaseConfig

class Summary:
    @classmethod
    def get_case_report(cls):
        case_report = OperationJson.read_json(os.path.join(BaseConfig.report_dir,'summary.json'))
        return case_report