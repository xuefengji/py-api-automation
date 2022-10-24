#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/17
# @Author: xuef
# @File: enums.py
# @Desc:


from enum import Enum, unique

@unique
class AssertEnum(Enum):
    equals = "=="
    less_than = "lt"
    less_than_or_equals = "le"
    greater_than = "gt"
    greater_than_or_equals = "ge"
    not_equals = "not_eq"
    contains = "contains"

@unique
class DependsType(Enum):
    RESPONSE = 'response'
    REQUEST = 'request'
    SQLDATA = 'sql_data'
    CACHE = 'cache'

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

@unique
class RequestTypeEnum(Enum):
    JSON = "json"
    PARAMS = "params"
    FILE = "file"
    DATA = "data"
    EXPORT = "export"
    NONE = "none"

@unique
class RequestMethod(Enum):
    POST = 'post'
    GET = 'get'
    PUT = 'put'
    DELETE = 'delete'
