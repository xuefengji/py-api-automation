#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/17
# @Author: xuef
# @File: assert_enum.py
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

