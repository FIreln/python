import requests
import unittest
from TestData import Data_AboutLogin
from TestResult import ActionFIle
from comment import title

class TestAboutLogin(unittest.TestCase):
    t_data = Data_AboutLogin.TestData()
    file = ActionFIle.File()
    title = title.title()
    def setUp(self):
        self.file.OpenFile()
    def tearDown(self):
        self.file.CloseFile()
    #login
    def test_Login(self):
        self.url,self.data = self.t_data.data_login()
        self.title.test_action(self.url)
        for i in range(self.data.__len__()):
            self.login = requests.post(self.url, json = self.data['data'+str(i+1)])
            self.code = self.login.status_code
            if self.code == 200:
                self.token = self.login.json()['AccessToken']
                self.result1 = r'PASS  正常登录用例，token ='+ self.token
                self.file.Write(self.result1)
                #return self.token
            elif self.code != 200:
                self.mes = self.login.json()['ErrorMessage']
                if self.mes == '电话号码或者密码错误':
                    self.result1 = r'PASS  用户名或密码错误用例，code ='+ str(self.code)+'， Mes = '+ self.mes
                    self.file.Write(self.result1)
                elif self.mes != '电话号码或者密码错误':
                    self.result2 = r'FALSE  用户名或密码错误用例，code ='+ str(self.code)+'， Mes = '+ self.mes
                    self.file.Write(self.result2)
    # changepassword
    def test_changepassword(self):
        self.url, self.data = self.t_data.data_changepassword()
        self.title.test_action(self.url)
        for i in range(self.data.__len__()):
            self.chpw = requests.post(self.url, json = self.data['data'+str(i+1)])
            self.json = self.chpw.json()
            self.code = self.chpw.status_code
            if self.code == 200:
                self.result1 = r'PASS  密码修改成功，code ='+ str(self.code)
                self.file.Write(self.result1)
            elif self.code != 200:
                self.mes = str(self.json['ErrorMessage'])
                if self.data['data'+str(i+1)]['OldPassword'] == '':
                    if self.mes == '更改密码失败':
                        self.result2 = r'PASS  旧密码为空用例，code ='+ str(self.code)+'， Mes = '+ self.mes
                        self.file.Write(self.result2)
                    elif self.mes != '更改密码失败':
                        self.result3 = r'FALSE  旧密码为空时用例，code ='+ str(self.code)+'， Mes = '+ self.mes
                        self.file.Write(self.result3)
                if self.data['data'+str(i+1)]['OldPassword'] != '':
                    if self.mes == '更改密码失败':
                        self.result = r'PASS  旧密码输入错误用例，code ='+ str(self.code)+'， Mes = '+ self.mes
                        self.file.Write(self.result)
                    elif self.mes != '更改密码失败':
                        self.result5 = r'FALSE  旧密码输入错误用例，code ='+ str(self.code)+'， Mes = '+ self.mes
                        self.file.Write(self.result5)
    # 使用suite封装case，构造测试集
    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestAboutLogin('test_Login'))
        suite.addTest(TestAboutLogin('test_changepassword'))
        return suite
    def begin(self):
        self.SA = TestAboutLogin()
        self.file = ActionFIle.File()
        self.runner = unittest.TextTestRunner()
        self.file.Truncate()
        self.runner.run(SA.suite())
if __name__ == '__main__':
    #使用suite封装case，构造测试集
    '''
    suite = unittest.TestSuite()
    suite.addTest(StartApi("test_Login"))
    suite.addTest(StartApi("test_changepassword"))
    '''
    #执行测试
    SA = TestAboutLogin()
    file = ActionFIle.File()
    runner = unittest.TextTestRunner()
    file.Truncate()
    runner.run(SA .suite())