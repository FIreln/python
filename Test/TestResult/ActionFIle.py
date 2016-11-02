
class File:

    #打开文件
    def OpenFile(self):
        self.file = open(r'D:\PythonProject\TestResult\TestResult','a+',encoding='utf-8')
    #关闭文件
    def CloseFile(self):
        self.file.close()
    #写入文件
    def Write(self,result):
        self.file.writelines(result +'\n')
    #清空文件
    def Truncate(self):
        self.f = open(r'D:\PythonProject\TestResult\TestResult','w',encoding='utf-8')
        self.f.truncate()
        self.f.close()

if __name__ == '__main__':
    file = File()
    file.OpenFile()
    file.Truncate()
