import json
class Check:


    def checkResoult(self,ActualRes,key,value):
        if key == 'int':
            if int(ActualRes) == int(value):
                return 'pass'
            else:
                return 'faile'
        elif key == '':
            pass



