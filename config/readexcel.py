import os
import xlrd
import time
import xlwt
from xlutils.copy import copy





class Read_Ex():
    def read_excel(self):

        case=[]
        # 用例存放路径
        case_path = os.path.join(os.getcwd() + '\Case\excel\大有课堂测试用例.xls') #读取excel表格用例，暂时只支持xls格式
        try:
            # 打开excel表格
            wb1 = xlrd.open_workbook(case_path)
        except Exception as e:
            print (e)
        #找到sheet页
        table = wb1.sheet_by_name("Sheet1")
        #获取总行数总列数
        row_Num = table.nrows
        col_Num = table.ncols

        data_value = table.row_values(0)  # 获取第一行的标题
        case_id = data_value.index('序列')
        title = data_value.index('名称')
        url = data_value.index('请求地址')
        data = data_value.index('请求参数')
        data_type = data_value.index('参数类型')
        method = data_value.index('请求方式')
        headers = data_value.index('请求头')
        dynamic = data_value.index('用例类型')
        status = data_value.index('状态码')
        expect = data_value.index('success')
        sql = data_value.index('SQL')



        if row_Num <= 1:
            print("没数据")
        else:
            for i in range(1,row_Num):
                data_dict = {}
                data_dict[case_id] = table.cell(i,0).value
                data_dict[title] = table.cell(i,1).value
                data_dict[url] = table.cell(i,2).value
                data_dict[method] = table.cell(i,3).value
                data_dict[headers] = table.cell(i,4).value
                data_dict[data] = table.cell(i,5).value
                data_dict[data_type] = table.cell(i,6).value
                data_dict[dynamic] = table.cell(i, 8).value
                data_dict[status] = table.cell(i,9).value
                data_dict[expect] = table.cell(i,10).value
                data_dict[sql] = table.cell(i, 12).value

                case.append(data_dict)
            return case

    def write_excel(self,case_id,result,path_name):

        case_path = path_name
        read_excel = xlrd.open_workbook(case_path)
        workbook = copy(read_excel)
        #workbook = read_excel
        #sheet = read_excel.sheet_by_name("Sheet1")
        sheet = workbook.get_sheet(0) #获取第1个表的数据
        sheet.write(case_id,11,result)
        try:
            workbook.save(path_name)
        except Exception as e:
            print(e)
