from requests import requests
from newtest import sqlcon
import hashlib


class startapi:
    getdata = sqlcon.MysqlMethod()
    def md(self,num):
        #print(hashlib.new('md5',num).hexdigest())
        return hashlib.new('md5',num).hexdigest()
    def login(self):
        self.url = r'http://oauth.test.didixl.com/api/account/login'
        self.data = {
                'username': '13783783183',
                'password': self.md(b'123456')
            }
        self.res = requests.post(self.url, json=self.data)
        if self.res.status_code == 200:
            self.token = self.res.json()['AccessToken']
            print(self.token)
            return self.token
        else:
            print('登录失败，请确认账号密码！')
    def action(self):
        self.getdata.condb()
        count = int(self.getdata.condb())
        header = {'Authorization': 'Bearer ' + self.login()}
        for i in range(count):
             len,method,api,headers,data,datalen,host = self.getdata.getdata(i+1)
             if method == 'path' or method == 'Query':
                url = host+api+data
                requests.get(url,header = dict(headers,**header))
             elif method == 'json':
                url = host+api
                requests.get(url = url,header = dict(headers,**header), json = data)
             elif method == 'null':
                url = host+api
                print(url)
                r = requests.get(url)

if __name__ == '__main__':
    sta = startapi()
    sta.action()



