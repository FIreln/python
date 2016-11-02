import os
import xlrd
from xlutils.copy import copy
import json
import time
import random

class FindCase:
    '''
    获取测试数据
    '''
    def __init__(self):
        """
            初始化....
        """
        #当前工作路径
        self.currentdir=os.path.split(os.path.realpath(__file__))[0]
        self.casefile = self.currentdir + '/case.xls'
        if os.path.exists(self.casefile) == False:
            print("用例文件不存在请检查")
        else:
            self.file = xlrd.open_workbook(self.casefile)
    def openFile(self,sheetname):
        """
            根据sheetname 获取表对象
            Paramet，sheetname:excel sheet名
        """
        table = self.file.sheet_by_name(sheetname)
        nrows = table.nrows
        return table,nrows
    def writeResponse(self,sheetname,i,response):
        """
            将接口返回的respose写入对case行
            Parames,response:接口返回的response
            Parames,i:response的对应nrow
        """
        wb = copy(self.file)
        ws = wb.get_sheet(0)
        ws.write(i,8,response)
        wb.save('case.xls')
    def getCase(self,sheetname,i):
        """
            获取单个case的所有原子
            Parames,i:case的对应nrow
        """
        table,norws = self.openFile(sheetname)
        CaseID = str(int(table.row(i)[0].value))
        CaseName = table.row(i)[1].value
        CheckPoint = table.row(i)[2].value
        Api = table.row(i)[3].value
        Host =('http://%s.test.didixl.com/')%(Api.split('/')[1])
        Method = table.row(i)[4].value
        ExpectedRes = table.row(i)[7].value
        Data = table.row(i)[6].value
        Key = table.row(i)[8].value
        ActualRes = table.row(i-1)[9].value
        #IsHeader = int(table.row(i)[10].value)
        try:
            Params = json.loads(table.row(i)[5].value)
        except Exception:
            Params = table.row(i)[5].value

        '''
            生成随机数
        '''
        try:
            data = json.loads(Data)
            for key in data.keys():
                if data[key] == 'x':
                    data[key] = str(time.time())[-6:]+random.choice(Api)
                    print(data)
            return Method,data,Api,Key,CaseID,Params,CaseName,CheckPoint,ActualRes,ExpectedRes,Host
        except Exception:
            return Method,Data,Api,Key,CaseID,Params,CaseName,CheckPoint,ActualRes,ExpectedRes,Host

if __name__ == '__main__':
    fc = FindCase()
    print(fc.getCase('club',1))



