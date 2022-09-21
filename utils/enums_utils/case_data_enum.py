#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/9/2
# @Author: xuef
# @File: case_data_enum.py
# @Desc:

from enum import Enum, unique

@unique
class CaseEnum(Enum):
    URL = 'url'
    METHOD = 'method'
    IS_RUN = 'is_run'
    TITLE = 'title'
    HEADERS = 'headers'
    COOKIES = 'cookies'
    IS_DEPEND = 'is_depend'
    DEPENDS_DATA = 'depends_data'
    REQUEST_TYPE = 'request_type'
    data = 'data'
    ENCODE = 'encode'