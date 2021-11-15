import requests
import os


config_path = os.path.join(os.getcwd() + '\Config\\token.md')

def getHeaders():
    '''获取headers'''
    return { 'Parkingwang-Client-Source': 'ParkingWangAPIClientWeb',
            'Authorization': getToken()}


def login(url,params):
    try:
        url = "http://dykttest.zsyky.cn:9999" + url
        data = eval(params)
        s = requests.post(
            url=url,
            data=data,
            headers={'Content-Type': 'application/x-www-form-urlencoded',
                     'Authorization':'Basic dGVzdDp0ZXN0'}, timeout=5)
        r_token = s.json()['refresh_token']
        r = requests.post(
            url='http://dykttest.zsyky.cn:9999/auth/oauth/token',
            data={"grant_type":"refresh_token","scope": "server", "refresh_token": r_token},
            headers={'Content-Type': 'application/x-www-form-urlencoded',
                     'Authorization':'Basic dGVzdDp0ZXN0'}, timeout=5)
        with open(config_path, 'w') as f:
            f.write('bearer ' + r.json()['access_token'])
        print(r.json()['refresh_token'])
        d = {}
        if r.status_code == 200:
            d['success'] = True
        else:
            d['success'] = False
        return d

    except Exception as e:
        print(e)




def getToken():
    '''读取存储在文件中的token'''
    with open(config_path, 'r') as f:
        return f.read()

