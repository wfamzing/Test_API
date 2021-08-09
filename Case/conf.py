# -*- coding:utf-8 -*-
import requests
import json

# 定义全局变量被测接口url
#def testurl():
    #url = "http://192.168.1.161:8401"
    #return url
# 全局变量被测接口各类参数返回值
def enumerations(url,params,method,heard):
    headers = heard
    url = "http://192.168.1.161:8401"+url
    method = method

    if method == 'post':
        params = json.loads(params) #将文件params数据改为list类型
        try:
            r = requests.post(url,json=params).text
            r = json.loads(r)
            print(r)
            dic = {}
            dic["code"] = r["code"]
            dic["message"] = r["message"]
            dic["success"] = r["success"]
            #print(11111111111111111111111111)
            return dic
        except Exception as  e:
            print (e)

    if method == 'get':
        if eval(params) == None:
            #print(params)
            #print(1)
            try:
                r = requests.get(url).text
                #print(1111)
                r = json.loads(r)
                dic = {}
                dic["code"] = r["code"]
                dic["message"] = r["message"]
                dic["success"] = r["success"]
                return dic
            except Exception as  e:
                print(e)
        else:
            params = json.loads(params)
            try:
                r = requests.get(url, headers=headers, json=params).text
                print(1111)
                r = json.loads(r)
                dic = {}
                dic["code"] = r["code"]
                dic["message"] = r["message"]
                dic["success"] = r["success"]
                return dic
            except Exception as  e:
                print (e)

    if method == 'put':
        try:
            r = requests.put(url, headers=headers, json=params).text
            r = json.loads(r)
            dic = {}
            dic["code"] = r["code"]
            dic["message"] = r["message"]
            dic["success"] = r["success"]
            return dic
        except Exception as  e:
            print (e)

    if method == 'delete':
        try:
            r = requests.delete(url, headers=headers, json=params).text
            r = json.loads(r)
            dic = {}
            dic["code"] = r["code"]
            dic["message"] = r["message"]
            dic["success"] = r["success"]
            return dic
        except Exception as  e:
            print (e)



#r = requests.post(url,data=json.dumps(params))
#response = r.json()

