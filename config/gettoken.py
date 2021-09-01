import requests
import os


config_path = os.path.join(os.getcwd() + '\config\\token.md')

def getHeaders():
    '''获取headers'''
    return {'Content-Type': 'application/json;charset=UTF-8', 'Parkingwang-Client-Source': 'ParkingWangAPIClientWeb',
            'Authorization': getToken()}


def login():
    r = requests.post(
        url='http://192.168.1.161:8401/login/login',
        json={"account": "admin", "password": "111111"},
        headers={'Content-Type': 'application/json;charset=UTF-8',
                 'Parkingwang-Client-Source': 'ParkingWangAPIClientWeb'}, timeout=5)
    with open(config_path, 'w') as f:
        f.write(r.json()['data'])
    print(r.json()['data'])




def getToken():
    '''读取存储在文件中的token'''
    with open(config_path, 'r') as f:
        return f.read()

