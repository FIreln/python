import  json
import time
import random


class DataProcessing():

    def __init__(self,UseType,Params,Data,ActualRes,UseKey):
        self.rd = ('abc','gda','cgd','asd','xvv')
        self.usertype = UseType
        self.patams = Params
        self.data = Data
        self.actualres = ActualRes
        self.usekey = UseKey
        self.nowdata = ''

    def processdata(self):

        """
            根据userkey获取actualres中的所需数据
        """

        pass
    def processUsertype(self):
        """
            根据usertype生成最终参数
        """
        if self.usertype == '/':

            return
        elif self.usertype == '?':

            return
        elif self.usertype == 'b':

            return
        else:

            return

    def processbody(self):
        try:
            data = json.loads(self.data)
            for key in data.keys():
                if data[key] == 'x':
                    data[key] = str(time.time())[-6:]+random.choice(self.rd)
                    print(data)
            return data
        except Exception:
            return self.data
