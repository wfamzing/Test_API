import pymysql
def connectDB(sql,args=None):
    mydb = pymysql.connect(
        host="xxx.xxx.xxx.118",
        port=xxxxx,
        user="root",
        password="xxxxxx",
        database="xxxxx"
    )

    cursor = mydb.cursor()

    sql = sql
    cursor.execute(sql,args=args)
    result = cursor.fetchone() #fetchall（）获取所有记录
    #print(result)
    #for x in result:
        #print(x)
    return result
    cursor.close()
    mydb.close()
