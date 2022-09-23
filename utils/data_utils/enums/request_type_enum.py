#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/9/6
# @Author: xuef
# @File: request_type_enum.py
# @Desc:

from enum import Enum, unique


@unique
class RequestTypeEnum(Enum):
    JSON = "json"
    PARAMS = "params"
    FILE = "file"
    DATA = "data"