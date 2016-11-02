from TestResult import ActionFIle
class title:
    af = ActionFIle.File()
    def test_action(self,url):
        self.af.OpenFile()
        self.af.Write('*********************************************************************'
                      +'\n'+ url + '接口开始进行测试'
                      +'\n'+'*********************************************************************')
        self.af.CloseFile()

