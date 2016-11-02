import requests

class HttpClent:

    def __init__(self,host,api,params,data,token):
        """
            初始化....
            Parames,host:域名
            Parames,api:接口url
            Parames,params:path\query参数
            Parames,token:有效token
        """
        self. header = {
            "Accept":"application/json",
            "Content-Type":"application/json",
            "Authorization":'Bearer '+"%s" % token
       }
        self.url = host + api
        self.params = params
        self.data = data
    def doGet(self):
        #print('%s %s %s' % (self.url,self.params,self.data))
        if self.params[0] == '{':
            response = requests.get(url=self.url,params=self.params,headers=dict(self. header))
            return response
        else:
            response = requests.get(url=self.url+self.params,headers=dict(self. header))
            return response

    def doPost(self):
        response = requests.post(url=self.url,params=self.params,json=self.data,headers=self. header)
        #print(responsetext.status_code)
        return response
    def doPut(self):
        response = requests.post(url=self.url,params=self.params,json=self.data,headers=self. header)
        #print(responsetext.status_code)
        return response
    def doDelete(self):
        response = requests.post(url=self.url,params=self.params,headers=self. header)
        #print(responsetext.status_code)
        return response
if __name__ == '__main__':
    hc = HttpClent('http://club.test.didixl.com/','api/Label',None,None,None)

    hc.doGet()