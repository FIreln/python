import unittest

from Didixl.dorequest import runcase


class BeginTest(unittest.TestCase):
    """
        unittest封装执行
    """
    def test_hd(self):
        self.runcase = runcase.RunCase()
        self.runcase.run('activity')

    def suite(self):
        self.suite = unittest.TestSuite()
        self.suite.addTest(BeginTest('test_hd'))
        return self.suite
if __name__ == '__main__':
    tf = BeginTest()
    runer = unittest.TextTestRunner()
    runer.run(tf.suite())
