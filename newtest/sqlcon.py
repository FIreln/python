import  pymysql

class MysqlMethod:
    #连接数据库，生成游标#
    def condb(self):
        self.coon = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root',password = '123456',db = 'test')
        self.cur = self.coon.cursor()
        count = self.cur.execute(r'SELECT count(*) from get')
        return count
    #关不数据了和游标#
    def clodb(self):
        self.coon.close()
        self.cur.close()
    #获取测试数据#
    def getdata(self,length):
        query = r'select count(*),method,api,headers,data,datalen,host from get where id = '+str(length)
        #print(r'select method from get '+where)
        self.cur.execute(query)
        value = self.cur.fetchall()[0]
        print(value)
        len = value[0]
        method = value[1]
        api = value[2]
        headers = value[3]
        data = value[4]
        datalen = value[5]
        host = value[6]
        return len,method,api,headers,data,datalen,host

if __name__ == '__main__':
    sqlme = MysqlMethod()
    sqlme.condb()
    sqlme.getdata(1)