import xlrd
import os
import json

currentdir=os.path.split(os.path.realpath(__file__))[0]#获取当前工作文件夹
class conxls:
    def open(self,num):
        casefile = currentdir + '\case.xlsx'
        if os.path.exists(casefile) == False:
            print("当前目录下没有case文件，请检查！！！")
        data = xlrd.open_workbook(casefile)#打开文档
        table = data.sheet_by_name(num)
        nrows = table.nrows #行数
        ncols = table.ncols #列数
        #print(nrows)
        return nrows,table
    #colnames = table.row_values(1) #某一行数据
    def getdata(self,num,i):
        nrows,table = self.open(num)
        CaseID = str(int(table.row(i)[0].value))
        CaseName = table.row(i)[1].value
        Method = table.row(i)[2].value
        Host = table.row(i)[3].value
        Api = table.row(i)[4].value
        Headers = table.row(i)[5].value
        Data = json.loads(table.row(i)[6].value)
        Res = json.loads(table.row(i)[7].value)
        Msg = table.row(i)[9].value
        #Length = table.row(i)[7].value
        #print(Res.__len__())
        #print(Res['res1'])
        return Method,Host,Headers,Data,Res,Api,Msg,CaseID


if __name__ == '__main__':
    con = conxls()
    con.getdata('activity',4)




