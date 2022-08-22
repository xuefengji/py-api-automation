#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/17
# @Author: xuef
# @File: mysql_control.py
# @Desc: 封装操作数据库

import pymysql
import traceback
from utils.log_utils.log_control import ERROR



class MySQL:

    def __init__(self, config: dict):
        try:
            self.conn = pymysql.connect(**config)
            # 使用 cursor 方法获取操作游标，得到一个可以执行sql语句，并且操作结果为字典返回的游标
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  # 括号内不写参数,数据是元组套元组
        except Exception :
            ERROR.error(f"连接数据库失败，错误信息：{traceback.format_exc()}")
            quit()


    def __del__(self):
        if hasattr(self, "conn"):
            self.cursor.close()
            self.conn.close()


    def execute_sql(self, sql_query):
        """
        sql 查询
        :param sql: sql 语句
        :return:
        """
        try:
            self.cursor.execute(sql_query)
        except Exception:
            ERROR.error(f"sql语句执行失败，错误信息：{traceback.format_exc()}")
        else:
            return True

    def select(self, sql):
        flag = self.execute_sql(sql)
        if flag:
            data = self.cursor.fetchone()
            return data

