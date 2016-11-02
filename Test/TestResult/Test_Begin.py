
import unittest
from TestData import Data_AboutLogin
from TestResult import ActionFIle
from comment import title
from StartAPI import Test_AboutFInance,Test_AboutLogin
class TestBegin(unittest.TestCase):
    def begin(self):
        #Test_AboutFInance.TestFinance()
        Test_AboutLogin.TestAboutLogin().begin()

if __name__ == '__main__':
    tb = TestBegin()
    tb.begin()


