#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/3
# @Author: xuef
# @File: assert_base.py
# @Desc:

from common.asserts.assert_type import AssertType
from utils.data.enums.enums import AssertEnum


class Assert(AssertType):

    @classmethod
    def expect_check(cls,expect, actual, type):
        if type in AssertEnum._value2member_map_:
            function = AssertEnum(type).name
            if hasattr(AssertType, function):
                getattr(AssertType, function)(expect, actual)
            raise ValueError("相关断言函数不存在")
        raise ValueError("断言类型不存在")








