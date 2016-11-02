from demo1.comment import gettoken
from demo1.dorequest import docase
from demo1.testcase import database
from demo1.comment import check

class RunCase:

    def __init__(self):
        """
            初始化....
            Paramet,host:域名
        """
        self.database = database.FindCase()
        self.check = check.Check()
        self.login = gettoken.GetToken().login()
    def run(self,name):
        """
            遍历执行测试用例接口
            Params，name:excel sheet名，即域名关键字
        """
        table,nrows = self.database.openFile(name)
        token = self.login
        #print(token)
        for i in range(1,int(nrows)):
            Method,data,Api,Key,CaseID,Params,CaseName,CheckPoint,ActualRes,ExpectedRes,Host = self.database.getCase(name,i)
            try:
                if Method == 'Get':
                    response = docase.HttpClent(Host, Api, Params, data, token).doGet()
                    #self.database.writeResponse('club',i,response.text)
                    resoult = self.check.checkResoult(response.json(),Key,ExpectedRes)
                    print(resoult,CaseName,response.status_code,response.text)
                elif Method == 'Post':
                    docase.HttpClent(Host, Api, Params, data, token).doPost()
                elif Method == 'Put':
                    docase.HttpClent(Host, Api, Params, data, token).doPut()
                elif Method == 'Delete':
                    docase.HttpClent(Host, Api, data, Params, token).doDelete()
            except Exception as e:
                print('CaseID：%s、CheckPoint：%s  接口调用失败；错误类型：%s'%(CaseID,CheckPoint,e))


if __name__ == '__main__':
    RunCase = RunCase()
    RunCase.run('club')




