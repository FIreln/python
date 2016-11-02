from comment import login
class TestData:
    login = login.login()
    def bingOutlayAccount(self):
        self.url = r'http://consultant.test.didixl.com/api/Order/online'
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.login.login(),
        }
        self.data = {
            "SellerId": 0,
            "SellerNumber": "Dr20160722111840U49gWDPf",
            "SellerName": "a",
            "SellerPhone": "1234",
            "BuyerId": 0,
            "BuyerNumber": "Ur20160723161520zDMG8aJH",
            "BuyerName": "b",
            "BuyerPhone": "1234",
            "Description": "月经不调怎么治疗？",
            "Amount": 0
        }
        return self.url, self.headers, self.data