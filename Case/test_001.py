# -*- coding:utf-8 -*-
# 用例执行
# 1、导入模块
import unittest
import os
import ddt
import time
import xlrd
import requests
from xlutils.copy import copy
from Config.getToken import login, getHeaders
from Config.ReadExcel import Read_Ex
from Case.toRequests import SendRequests
from Config.phone import existed_p
from Config.testdata import create_Testdata

#login()
test_data = Read_Ex().read_excel()
now = time.strftime("%Y-%m-%d-%H_%M_%S")  # 获取当前日期
case_path = os.path.join(os.getcwd() + '\Case\excel\大有课堂测试用例.xls')
test_case = os.path.join(os.getcwd() + '\Case\excel')
path_name = test_case + '\\' + now + '-request_case.xls'
read_excel = xlrd.open_workbook(case_path)
workbook = copy(read_excel)
try:
    workbook.save(path_name)
except Exception as e:
    print(e)


# 2、继承自unittest.TestCase类
@ddt.ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    @ddt.data(*test_data)
    def test_api(self, data):

        print('start ...')
        data[5] = create_Testdata(data[5])
        data[5],data[12] = existed_p(data[5],data[12])#替换手机号参数
        if data[10] == 'True':
            ee = True
        else:
            ee = False
        try:
            head = getHeaders()
            if data[8] == "L":
                #login(data[2], data[5])
                self.assertEqual(ee,login(data[2], data[5])["success"])
                test_result = 'pass'
            else:
                # 发送请求
                self.assertEqual(ee, SendRequests.sendRequests(self.s, data[2], data[5], data[3], head, data[6],data[8],data[12])["success"])
                test_result = 'pass'
        except AssertionError:
            test_result = 'failed'
            raise
        finally:
            print(data[0])
            print(test_result)
            Read_Ex.write_excel(self, data[0], test_result, path_name)
