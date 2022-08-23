#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/3
# @Author: xuef
# @File: assert_base.py
# @Desc:

from common.asserts.assert_type import AssertType



class Assert:
    @classmethod
    def expect_check(cls,expect,actual,type):
        if type=="==":
            AssertType.equal(expect, actual)





