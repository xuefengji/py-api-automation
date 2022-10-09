#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/10
# @Author: xuef
# @File: operation_json.py
# @Desc:封装操作 json

import os, json


class OperationJson:

    @classmethod
    def read_json(cls, json_path):
        if os.path.exists(json_path):
            try:
                with open(json_path, 'r', encoding='utf-8') as fp:
                    return json.load(fp)
            except Exception as e:
                raise IOError('读取 json 文件失败！')
        else:
            raise FileNotFoundError('json文件不存在！')

    @classmethod
    def write_json(cls, data, json_path):
        try:
            with open(json_path, 'w', encoding='utf-8') as fp:
                json.dump(data, fp)
        except Exception as e:
            raise IOError('写入 json 文件失败！')
