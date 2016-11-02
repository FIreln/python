import hashlib
import json

from requests import requests

from Didixl.activity import data
from testbasexls import resanalysis


class startapi:
    getdata = data.conxls()
    analysis = resanalysis.ananysis()
    def md(self,num):
        #print(hashlib.new('md5',num).hexdigest())
        return hashlib.new('md5',num).hexdigest()
    def login(self):
        self.url = r'http://oauth.test.didixl.com/api/account/login'
        self.data = {
                'username': '13783783183',
                'password': self.md(b'654321')
            }
        self.res = requests.post(self.url, json=self.data)
        if self.res.status_code == 200:
            self.token = self.res.json()['AccessToken']
            #print(self.token)
            return self.token
        else:
            print('登录失败，请确认账号密码！')
    '''
        1.生成headers
        2.获取接口参数
        3.判断入参Method.
        4.获取入参和对应的期望出参
        5.实现接口生成response
        6.获取code和text
        7.调用分析函数
    '''
    def test_get(self):
        #self.getdata.open('Get')
        nrows,table = self.getdata.open('Get')
        header = {'Authorization': 'Bearer  ' + self.login()}
        #print(header)
        for i in range(1,nrows+1):
            method,host,headers,data,res,api,msg,caseid = self.getdata.getdata('activity',i)
            #hea = eval(str(headers))
            #print(i,nrows)
            if method == 'Path' or method == 'Query':
                #print(self.url)
                for l in range(data.__len__()):
                    dt = data['data' + str(l+1)]
                    expect_res = res['res' + str(l+1)]
                    self.url = host+api+dt
                    response = requests.get(self.url,headers = header,json = dt)
                    code = response.status_code
                    text = json.loads(response.text)
                    self.analysis.judgement(code,text,expect_res,msg,dt,caseid,api)
                    #print(code,text,result)
            else:
                url = host+api
                response = requests.get(url)
                print(response.status_code)
    def test_post(self):
        #self.getdata.open('Get')
        nrows,table = self.getdata.open('Post')
        header = {'Authorization': 'Bearer  ' + self.login()}
        print(header)
        for i in range(nrows):
             method,host,headers,data,length,api = self.getdata.getdata('Post',i)
             #hea = eval(str(headers))
             if method == 'Json':
                self.url = host+api
                d = json.loads(data)
                response = requests.get(self.url,headers = header,json = d)
                code = response.status_code
                content = response.content
                print(self.url)
                print(code,content)
             elif method == 'none':
                url = host+api
                response = requests.get(url)
                print(response.status_code,)
if __name__ == '__main__':
    sta = startapi()
    sta.test_get()



