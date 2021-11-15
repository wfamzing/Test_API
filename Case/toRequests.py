# _*_ coding:utf-8 _*_
#发送请求
import json
import os
import re
from Config.mysql import connectDB

dynamic_path = os.path.join(os.getcwd() + '\Config\\dynamic.md')

class SendRequests():

    """发送请求数据"""
    def sendRequests(s,url,params,method,heard,type,dynamic,sql):
        try:
            #从读取的表格中获取响应的参数作为传递
            if dynamic == "U":
                url_d = url.replace("${id}","/"+getDynamic())
                url = "http://dykttest.zsyky.cn:9999" + url_d
            else:
                if params.find("${id}") != -1:         #if params.find("${id}") != -1:
                    params = params.replace("${id}",getDynamic())
                    #url = "http://dykttest.zsyky.cn:9999" + url  # 这里更改接口的url
                url = "http://dykttest.zsyky.cn:9999" + url  # 这里更改接口的url
                params = params

            h = heard
            method = method
            type = type
            #通过判断参数类型选择转化相应类型转化，同时将其他两个类型置空
            if type == "json":
                data_json = json.loads(params)
                data = None
                data_params = None
            elif type == "data":
                data_json = None
                data = eval(params)
                data_params = None
            else:
                data_json = None
                data = None
                data_params = eval(params)



            #发送请求
            r = s.request(method=method,url=url,headers=h,params=data_params,data=data,json=data_json).text
            r = json.loads(r)
            print(r)
            dic = {}
            dic["code"] = r["code"]
            dic["msg"] = r["msg"]
            if dynamic == 'D':
                ID = str(connectDB(sql)[0])
                with open(dynamic_path, 'w') as f:
                    f.write(ID)
                print(str(ID))

            if r["code"] == eval('0'):
                dic["success"] = True
            else:
                dic["success"] = False
            return dic
        except Exception as e:
            print(e)

def getDynamic():
    with open(dynamic_path, 'r') as f:
        return f.read()
