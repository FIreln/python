from Didixl.comment import gettoken
from Didixl.dorequest import docase
from Didixl.testcase import database
from Didixl.comment import check

class RunCase:

    def __init__(self,isheader):
        """
            初始化....
            Paramet,host:域名
        """
        self.database = database.FindCase()
        self.check = check.Check()
        self.login = gettoken.GetToken().login()
        self.isheader = isheader
    def run_activity_case(self,name):
        """
            遍历执行测试用例接口
            Params，name:excel sheet名，即域名关键字
        """
        table,nrows = self.database.openFile(name)
        if self.isheader == 0:
            token = None
        else:
            token = self.login
        #print(token)
        for i in range(1,int(nrows)):
            Method,Data,Api,Key,CaseID,Params,CaseName,CheckPoint,ActualRes,ExpectedRes,Host = self.database.getCase(name,i)
            try:
                if Method == 'Get':
                    response = docase.HttpClent(Host, Api, Params, Data, token).doGet()
                    resoult = self.check.checkResoult(response.json(),Key,ExpectedRes)
                    self.database.writeResponse(name,i,response.text)
                    print(resoult,CheckPoint,response.status_code,response.text)
                elif Method == 'Post':
                    docase.HttpClent(Host, Api, Params, Data, token).doPost()
                elif Method == 'Put':
                    docase.HttpClent(Host, Api, Params, Data, token).doPut()
                elif Method == 'Delete':
                    docase.HttpClent(Host, Api, Data, Params, token).doDelete()
            except Exception as e:
                print('CaseID：%s、CheckPoint：%s  接口调用失败；错误类型：%s'%(CaseID,CheckPoint,e))


if __name__ == '__main__':
    RunCase = RunCase(0)
    RunCase.run_activity_case('activity')




