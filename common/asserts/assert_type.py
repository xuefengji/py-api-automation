#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/17
# @Author: xuef
# @File: assert_type.py
# @Desc:

#TODO
class AssertType:

    @classmethod
    def equal(cls, expect, actual):
        assert expect==actual

    @classmethod
    def less_than(cls, expect, actual):
        assert expect < actual

    @classmethod
    def less_than_or_equals(cls,expect, actual):
        assert expect <= actual

    @classmethod
    def greater_than(cls, expect, actual):
        assert expect > actual

    @classmethod
    def greater_than_or_equals(cls, expect, actual):
        assert expect >= actual

    @classmethod
    def not_equals(cls, expect, actual):
        assert expect != actual

    @classmethod
    def contains(cls, expect, actual):
        assert expect in actual


