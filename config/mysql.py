import pymysql
def connectDB(sql,args=None):
    mydb = pymysql.connect(
        host="101.201.233.118",
        port=33033,
        user="root",
        password="123123",
        database="ruoxi_db"
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