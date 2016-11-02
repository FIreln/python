import unittest
import requests
from TestData.consultant import Order_Online

class OrderOnline(unittest.TestCase):
    oo = Order_Online.Online()
    def test_online(self):
        self.url, self.data, self.headers = self.oo.online()
        for i in range(self.data.__len__()-1):
            self.res = requests.post(self.url, json=self.data, headers=self.headers)
            self.code = self.res.status_code
            if self.code == 200:
                self.json = self.res.json()
                print(self.code, self.json)
            else:
                print('接口调用错误', self.code)

    def suite(self):
        self.suite = unittest.TestSuite()
        self.suite.addTest(OrderOnline('test_online'))
        return self.suite
if __name__ == '__main__':
    oo = OrderOnline()
    runner = unittest.TextTestRunner()
    runner.run(oo.suite())