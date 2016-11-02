import requests
import hashlib
class login:

    def md(self,num):
        #print(hashlib.new('md5',num).hexdigest())
        return hashlib.new('md5',num).hexdigest()
    def login(self):
        self.url = r'http://oauth.test.didixl.com/api/account/login'
        self.data = {
                'username': '13429104075',
                'password': self.md(b'111111')
            }
        self.res = requests.post(self.url, json=self.data)
        if self.res.status_code == 200:
            self.token = self.res.json()['AccessToken']
            print(self.token)
            return self.token
        else:
            print('登录失败，请确认账号密码！')
if __name__ == '__main__':
    l = login()
    l.login()