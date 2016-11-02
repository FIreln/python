



class ananysis:
    '''
    参数说明
        code：状态码
        text：接口返回值
        result：期望值
        msg：关键分析字段信息即分析关键字段的key值
    '''
    def judgement(self,code,text,expect_res,msg,dt,caseid,api):
        if code == 200 and msg != 'json':
            for key in text.keys():
                value = text[key]
                #print(code,value,expect_res,key,msg)
                if key == msg and value == expect_res:
                    print('用例'+caseid+' pass')
                else:
                    print('用例'+caseid+' false'+' API:'+api+' 入参：'+str(dt)+' 出参：'+str(text))
        elif code == 200 and msg == 'json':
            #print(text,expect_res)
            if text == expect_res:
                print('用例'+caseid+' pass')
            else:
                print('用例'+caseid+' false'+' API:'+api+' 入参：'+str(dt)+' 出参：'+str(text))

