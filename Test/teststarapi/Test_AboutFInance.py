from TestData import Data_AboutFinance
import requests
import unittest
class TestFinance(unittest.TestCase):
    fin = Data_AboutFinance.TestData()

    def setUp(self):
        return None

    def tearDown(self):
        return None

    def test_OutlayAccount(self):
        self.url, self.headers, self.data = self.fin.bingOutlayAccount()
        self.res = requests.post(self.url, json = self.data, headers = self.headers)
        print(self.res.json())

    def suite(self):
        self.suite = unittest.TestSuite()
        self.suite.addTest(TestFinance('test_OutlayAccount'))
        return self.suite
if __name__ == '__main__':
    tf = TestFinance()
    runer = unittest.TextTestRunner()

    runer.run(tf.suite())