from comment import login

class TestData:
    md = login.login()
    trueusername = '13783783183'
    falseusername = '13783154564'
    oldpassword = b'123456789'
    newpassword = b'123456'
    #login
    def data_login(self):
        url = r'http://oauth.test.didixl.com/api/account/login'
        data = {
            #正常登录
            'data1': {
                'username': self.trueusername,
                'password': self.md.md(self.oldpassword)
            },
            #密码错误
            'data2': {
                'username': self.trueusername,
                'password': self.md.md(self.newpassword)
            },
            #用户名错误
            'data3': {
                'username': self.falseusername,
                'password': self.md.md(self.oldpassword)
            },
            #用户名密码都错误
            'data4': {
                'username': self.falseusername,
                'password': self.md.md(self.newpassword)
            }
        }
        return url,data
    #changepassword
    def data_changepassword(self):
        self.url = r'http://oauth.test.didixl.com/api/account/changepassword'

        self.data = {
            'data1':#正常修改
                {'NewPassword': self.md.md(self.newpassword),
                 'OldPassword': self.md.md(self.oldpassword),
                 'UserName': self.trueusername
                 },
            'data2':#OldPassword错误
                {'NewPassword': self.md.md(self.oldpassword),
                 'OldPassword': self.md.md(self.oldpassword),
                 'UserName': self.trueusername
                 },
            #初始化数据，便于下次运行
            'data3':
                {'NewPassword': self.md.md(self.oldpassword),
                 'OldPassword': self.md.md(self.newpassword),
                 'UserName': self.trueusername
                 }}
        return self.url, self.data
    #changeQualification
    def data_changeQua(self):
        self.url = r'http://doctor.test.didixl.com/api/doctor'
        self.data = {
            'data1':
                {"AvatarUrl": "http://imgapi.didixl.com/image/201608/20160802174744691331-0@l=1",
                 "BirthDate": "1900-01-01 00:00:00",
                 "Credentials":
                     [
                    {"DoctorId": "1136", "Id": "2842", "Kind": 0, "Number": "9",
                     "PhotoUrl": "http://imgapi.didixl.com/image/201607/20160705162135708565-0.jpg@l=1"},
                    {"DoctorId": "1136", "Id": "2843", "Kind": 1, "Number": "8",
                     "PhotoUrl": "http://imgapi.didixl.com/image/201607/20160705162137036368-1.jpg@l=1"},
                    {"DoctorId": "1136", "Id": "2844", "Kind": 2, "Number": "789",
                     "PhotoUrl": "http://imgapi.didixl.com/image/201607/20160707095621995352-0.jpg@l=1"}],
                 "Educations": [],
                 "Email": "",
                 "Gender": 1,
                 "Id": "1136",
                 "Name": "test2",
                 "Phone": "13645810322",
                 "Qualification": {"Bio": "sss", "Department": "", "DoctorId": "1136", "Expertise": "999",
                                   "Hospital": "执业单位1", "HospitalGrading": "", "Id": "8943", "JobPost": "主任医师",
                                   "Tag": "12"},
                 "Status": 2,
                 "UserNumber": "Dr20160704160526KyfFCsmO"},
            'data2':
                {'NewPassword': 'e10adc3949ba59abbe56e057f20f883e',
                 'OldPassword': 'f1887d3f9e6ee7a32fe5e76f4ab80d63',
                 'UserName': '13783783183'
                 },
            'data3':
                {'NewPassword': '25f9e794323b453885f5181f1b624d0b',
                 'OldPassword': '',
                 'UserName': '13783783183'
                 },
            # 初始化数据，便于下次运行
            'data4':
                {'NewPassword': 'e10adc3949ba59abbe56e057f20f883e',
                 'OldPassword': '25f9e794323b453885f5181f1b624d0b',
                 'UserName': '13783783183'
                 }}
        return self.url, self.data