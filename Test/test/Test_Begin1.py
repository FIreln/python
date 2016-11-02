import unittest
from TestResult import ActionFIle
from teststarapi import Test_AboutFInance,Test_AboutLogin
class TestBegin(unittest.TestCase):
    file = ActionFIle.File()
    def setUp(self):
        self.file.OpenFile()
    def tearDown(self):
        self.file.CloseFile()
    def suite(self):
        self.StartApi = Test_AboutLogin.TestAboutLogin()
        self.TestFinance = Test_AboutFInance.TestFinance()
        self.suite = unittest.TestSuite()
        self.suite.addTest(self.StartApi('test_Login'))
        self.suite.addTest(self.StartApi('test_changepassword'))
        self.suite.addTest(self.TestFinance('test_OutlayAccount'))
        return self.suite
if __name__ == '__main__':
    testbegin = TestBegin()
    runner = unittest.TextTestRunner()
    file = ActionFIle.File()
    file.Truncate()
    runner.run(testbegin.suite())


