import random
from Config.mysql import connectDB
import re

def create_mobile():
    """
    随机生成11位手机号
    start_mobile 为初始三位数
    :return: 返回一个手机号字符串
    """
    start_mobile = ['138', '139', '188', '130', '131', '132', '133', '135', '136', '137', '150']
    start_mobile = random.choice(start_mobile)
    end_num = ''.join(random.sample('0123456789', 8))
    return start_mobile + end_num


def is_existed_mobile(mobile):
    """
    判断指定的手机号在数据库中是否存在
    """

    sql = 'SELECT phone FROM rx_organization_main WHERE phone=%s;'
    if connectDB(sql, args=[mobile]):  # 手机号已经存在，则返回True，否则返回False
        return True
    else:
        return False


def create_not_existed_mobile():
    """
    随机生成一个在数据库中不存在的手机号
    :return: 返回一个手机号字符串
    """
    while True:
        one_mobile = create_mobile()
        if not is_existed_mobile(one_mobile):
            print(11111)
            break

    return str(one_mobile)


def existed_p(d,s):
    data = d
    sql = s
    phone = create_not_existed_mobile()
    if data.find("${ph}") != -1 or sql.find("${ph}") != -1:
        data = data.replace("${ph}", phone)
        #return data
    #if sql.find("${ph}") != -1:
        sql = sql.replace("${ph}", phone)
        #return sql
    return data,sql
