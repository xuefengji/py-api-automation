#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/8
# @Author: xuef
# @File: random_data.py
# @Desc:

import random, string


class RandomUtil:
    @classmethod
    def random_string(cls, str, length_of_string):
        """
        生成指定字符开头的字符串
        :param str: 指定字符串
        :param length_of_string: 生成字符串的长度
        :return:
        """
        data = ''.join(random.choice(string.ascii_letters+string.digits)for _ in range(length_of_string))
        return str+data

    #TODO 随机生成数字
    @classmethod
    def random_int(cls, length_of_int):
        """
        生成指定位数的字符串
        :param length_of_int:
        :return:
        """
        pass


if __name__ == '__main__':
    data=RandomUtil.random_string('test',2)
    print(data)