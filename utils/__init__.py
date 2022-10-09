#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/1
# @Author: xuef
# @File: __init__.py
# @Desc:

from utils.data.models.model import Config
from utils.file.operation_yaml import OperationYaml
from config import BaseConfig

config_data = OperationYaml.read_yaml(BaseConfig.setting_dir)
config = Config(**config_data)

