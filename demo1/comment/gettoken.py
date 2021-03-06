import requests
import hashlib
class GetToken:
    def md(self,num):
        #print(hashlib.new('md5',num).hexdigest())
        return hashlib.new('md5',num).hexdigest()
    def login(self):
        '''
            生成token
        '''
        self.url = r'http://oauth.test.didixl.com/api/account/login'
        self.data = {
                'username': '13783783183',
                'password': self.md(b'123456')
            }
        self.res = requests.post(self.url, json=self.data)
        if self.res.status_code == 200:
            self.token = self.res.json()['AccessToken']
            return self.token
        else:
            print('登录失败，请确认账号密码！')


if __name__ == '__main__':
    print(GetToken().login())