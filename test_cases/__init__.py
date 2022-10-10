#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/10/9
# @Author: xuef
# @File: __init__.py
# @Desc: 获取测试用例


from utils.file.get_all_case_files import get_all_files
from config import BaseConfig
from utils.file.yaml_data_analysis import CaseData
from utils.caches.redis_cache import RedisHandle
from utils import config
from utils.caches.local_cache import CacheHandle, _cache_data


def case_set_cache():
    """
    将获取的用例写入缓存中
    """
    _files_list = get_all_files(BaseConfig.data_dir)
    if _files_list:
        for file in _files_list:
            _case_data = CaseData(file).get_case()
            if _case_data:
                for case in _case_data:
                    for k, v in case.items():
                        if config.cache_type == 1:
                            RedisHandle(config.redis).hash_set(k,v)
                        else:
                            if k not in _cache_data.keys():
                                CacheHandle.update_cache(k,v)
                            else:
                                raise ValueError(f"case_id: {k} 存在重复项, 请修改case_id\n"
                                         f"文件路径: {file}")

case_set_cache()








