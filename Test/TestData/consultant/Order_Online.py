from comment import login
class Online:
    host = r'http://consultant.test.didixl.com/'
    login = login.login()
    def online(self):
        self.url = self.host+r'api/Order/online'
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.login.login(),
        }
        self.data = {"SellerNumber": "Dr20160722111840U49gWDPf","Description": "月经不调怎么治疗"}
        #print(self.url, self.data,self.headers)
        return self.url, self.data, self.headers

if __name__ == '__main__':
    on = Online()
    on.online()