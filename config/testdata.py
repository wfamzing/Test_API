from faker import Faker

def create_Testdata(data):
    f = Faker(locale='zh_CN') # 为生成数据的文化选项，默认为en_US，只有使用了相关文化，才能生成相对应的随机信息
    data = data
    if data.find("${name}") != -1:
        data = data.replace("${name}", f.name()) #生成随机人名
    if data.find("${code}") != -1:
        data = data.replace("${code}", str(f.random_int())) #生成随机数字0-9999
    if data.find("${ssn}") != -1:
        data = data.replace("${ssn}", str(f.ssn())) #生成随机身份证号
    if data.find("${address}") != -1:
        data = data.replace("${address}", f.address()) #生成随机地址
    if data.find("${company}") != -1:
        data = data.replace("${company}", f.company()) #生成随机公司
    if data.find("${card}") != -1:
        data = data.replace("${card}", str(f.credit_card_number())) #生成随机银行卡号
    if data.find("${pstr}") != -1:
        data = data.replace("${pstr}", f.pystr()) #生成随机字符串
    if data.find("${img}") != -1:
        data = data.replace("${img}", f.image_url()) #生成随机图片url
    if data.find("${s}") != -1:
        data = data.replace("${s}", f.sentence()) #生成随机一句话
    if data.find("${wd}") != -1:
        data = data.replace("${wd}", f.word()) #生成随机词语
    if data.find("${fn}") != -1:
        data = data.replace("${fn}", f.file_name()) #生成随机文件名
    if data.find("${stm}") != -1:
        data = data.replace("${stm}", str(f.past_date())) #生成随机时间
    return data
