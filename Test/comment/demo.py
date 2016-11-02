import requests

url = "http://doctor.test.didixl.com/api/Org/web"

payload = {
  "AvatarUrl": "头像",
  "Name": "机构名称",
  "UserId": 0,
  "Phone": "13783783183",
  "Sequence": "排序号",
  "DoctorAssistantId": 0,
  "SourceId": 0,
  "kind": 0,
  "Weeks": 0,
  "BIO": "机构简介",
  "AdvisoryBIO": "咨询简介",
  "AFCUrl": "app封面（App Front cover）",
  "WXFCUrl": "微信封面（Weixin Front cover）",
  "Tag": "机构Title",
  "ProvinceId": 1,
  "CityId": 35,
  "IsLock": "false",
  "Address": "详细地址"
}
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': "Bearer dda462bc72face66b7350e64991dc3894c196c3a4eb915f8d50c22311431e85d",
    'cache-control': "no-cache",
    'postman-token': "806d26f1-cf13-4173-69a0-24a9afa7f3e3"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)