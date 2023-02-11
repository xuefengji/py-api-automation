#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/1
# @Author: xuef
# @File: operation_yaml.py
# @Desc:
import os, yaml
from typing import Dict


class OperationYaml:

    @classmethod
    def read_yaml(cls,yaml_path:str) -> Dict:
        """
        读取 yaml 内容
        :param yaml_path: yaml 文件路径
        """
        if not os.path.exists(yaml_path):
            raise FileNotFoundError('yaml文件不存在！')
        try:
            with open(yaml_path, 'r', encoding='utf-8') as fp:
                return yaml.load(fp, Loader=yaml.SafeLoader)
        except Exception as e:
            raise IOError('读取yaml文件失败！')


    @classmethod
    def write_yaml(cls, data, yaml_path):
        """
        将内容写入 yaml
        :param data: 要写入的数据
        :param yaml_path: yaml 文件路径
        """
        try:
            with open(yaml_path, 'w', encoding='utf-8') as fp:
                 yaml.dump(data, fp)
        except Exception as e:
            raise IOError('写入 yaml 文件失败！')

