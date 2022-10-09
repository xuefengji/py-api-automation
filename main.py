#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/8/10
# @Author: xuef
# @File: main.py
# @Desc:

import os, pytest
from config import BaseConfig
from utils.notify.notify_mail import SendMail
from utils.report.report_summary import Summary


def main():

    pytest.main(['-s', '-v', "--alluredir", BaseConfig.allure_report, '--clean-alluredir'])
    os.system('allure generate -c -o {0} {1}'.format(BaseConfig.allure_html_report, BaseConfig.allure_report))
    SendMail(Summary.get_case_report()).send_main()

if __name__ == '__main__':
    main()