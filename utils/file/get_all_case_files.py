#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/10/9
# @Author: xuef
# @File: get_all_case_files.py
# @Desc: 获取所有用例文件

import os


def get_all_files(file_dir: str) -> list:
    """
    param file_path: 文件目录
    """
    files_path = []
    if not os.path.exists(file_dir):
        raise FileNotFoundError('当前文件夹不存在')
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            path = os.path.join(root, file)
            files_path.append(path)
    return files_path



