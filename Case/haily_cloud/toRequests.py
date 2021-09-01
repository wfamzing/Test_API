# _*_ coding:utf-8 _*_

import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class SendRequests():
    """发送请求数据"""
    def sendRequests(s,url,params,method,heard,type):
        try:
            #从读取的表格中获取响应的参数作为传递
            h = heard
            url = "http://192.168.1.161:8401" + url #这里更改接口的url
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
            r = s.request(method=method,url=url,heardes=h,params=data_params,data=data,json=data_json).text
            r = json.loads(r)
            print(r)
            dic = {}
            dic["code"] = r["code"]
            dic["message"] = r["message"]
            dic["success"] = r["success"]
            return dic
        except Exception as e:
            print(e)
