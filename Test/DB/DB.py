import pymysql

class Odbc():
    def connectDb(self):
        self.coon = pymysql.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '123456',
        db = 'ddtest'
        )
        self.cur =self.coon.cursor()
        return self.cur,self.coon
    def creatTable(self):
        quary = r"create table Students" \
            "(Id INT NOT NULL AUTO_INCREMENT," \
            "Name VARCHAR(100) NOT NULL,"\
            "Address VARCHAR(100) NOT NULL," \
            "Gender INT NOT NULL," \
            "Leader VARCHAR(100) NOT NULL,"\
            "PRIMARY KEY ( Id ));"
        self.cur, self.coon = Odbc().connectDb()
        self.cur.execute(quary)
        self.coon.close()
    def insertData(self):
        quary = r"insert into Students VALUES(1,'蛋蛋','杭州',1,'宏正')"
        self.db = Odbc()
        #print('ab'+str(self.db))
        self.cur,self.coon = self.db.connectDb()
        #print('cur'+str(self.cur))
        self.cur.execute(quary)
        self.coon.close()

if __name__ == '__main__':
    db = Odbc()
    #db.creatTable()
    db.insertData()



