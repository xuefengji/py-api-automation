#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/9
# @Author: xuef
# @File: log_control.py
# @Desc:

import os, time
import logging
from config import BaseConfig

class LogUtils():

    def __init__(self, log_path, level):
        # 判断文件目录是否存在
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        self.level = level
        self.log_name = os.path.join(log_path, '%s_%s.log'% (time.strftime('%Y-%m-%d'), level))
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.INFO)
        # 设置日志的格式
        self.formatter = logging.Formatter('%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s: %(message)s')

    def log_handle(self, message):
        # 设置文件对象
        file_log = logging.FileHandler(filename=self.log_name, encoding="utf-8")
        # 设置控制台输出
        console = logging.StreamHandler()
        # 将日志格式给控制台对象
        file_log.setFormatter(self.formatter)
        console.setFormatter(self.formatter)
        # 判断日志对象中是否有 handler，如果没有则添加
        if not self.logger.handlers:
            # 把控制台日志对象给logging
            self.logger.addHandler(file_log)
            self.logger.addHandler(console)

        if hasattr(self.logger, self.level):
            getattr(self.logger, self.level)(message)

    def info(self, message):
        self.log_handle(message)

    def error(self, message):
        self.log_handle(message)

    def warning(self, message):
        self.log_handle(message)

    def debug(self, message):
        self.log_handle(message)


INFO = LogUtils(BaseConfig.log_dir, 'info')
ERROR = LogUtils(BaseConfig.log_dir, 'error')

if __name__ == '__main__':
    from config import BaseConfig
    log = LogUtils(BaseConfig.log_dir, 'info')
    log.info("eee")