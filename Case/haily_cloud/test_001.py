# -*- coding:utf-8 -*-
# 登录用例执行
# 1、导入模块
import unittest
import os
import ddt
import time
import xlrd
import requests
from xlutils.copy import copy
from config.gettoken import login,getHeaders
from config.readexcel import Read_Ex
from Case.haily_cloud.toRequests import SendRequests

login()
test_data = Read_Ex().read_excel()
now = time.strftime("%Y-%m-%d-%H_%M_%S") #获取当前日期
case_path = os.path.join(os.getcwd() + '\Case\excel\海疆接口测试.xls')
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
    def test_api(self,data):

        print('start ...')
        if data[10] == 'True':
            ee = True
        else:
            ee = False
        try:
            head = getHeaders()
            # 发送请求
            self.assertEqual(ee, SendRequests.sendRequests(self.s,data[2],data[5],data[3],head,data[6])["success"])
            test_result = 'pass'
        except AssertionError:
            test_result = 'failed'
            raise
        finally:
            print(data[0])
            print(test_result)
            Read_Ex.write_excel(self,data[0],test_result,path_name)





