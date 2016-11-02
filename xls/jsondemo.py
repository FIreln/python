dict_a = {
  "PageIndex": 0,
  "PageSize": 10,
  "TotalCount": 42,
  "TotalPages": 5,
  "IndexFrom": 0,
  "Items": [
    {
      "Id": 65,
      "UserId": 107,
      "UserNickName": "姜飞龙真帅+1",
      "AvatarUrl": "http://imgapi.didixl.com/image/201608/20160817105434716137-1.png@l=1",
      "CityName": "null",
      "Content": "不知道为什么天天抑郁",
      "Labels": [
        "狂躁症子标题"
      ],
      "ReplyCount": 6,
      "CreateTime": "2016-10-19 11:58:05"
    },
    {
      "Id": 63,
      "UserId": 114,
      "UserNickName": "137****3183",
      "AvatarUrl": "http://imgapi.didixl.com/image/201610/20161018181823981923-0.png@l=1",
      "CityName": "null",
      "Content": "不知道为什么天天抑郁",
      "Labels": [
        "狂躁症子标题"
      ],
      "ReplyCount": 9,
      "CreateTime": "2016-10-19 10:10:02"
    },
    {
      "Id": 62,
      "UserId": 3,
      "UserNickName": "天才医生",
      "AvatarUrl": "http://imgapi.didixl.com/image/201607/20160722175809296308-0.jpg@l=1",
      "CityName": "null",
      "Content": "哼哼唧唧几斤斤计较好纠结",
      "Labels": [
        "狂躁症子标题",
        "狂躁症子标题",
        "703845a"
      ],
      "ReplyCount": 1,
      "CreateTime": "2016-10-19 09:34:39"
    },
    {
      "Id": 61,
      "UserId": 114,
      "UserNickName": "137****3183",
      "AvatarUrl": "http://imgapi.didixl.com/image/201610/20161018181823981923-0.png@l=1",
      "CityName": "null",
      "Content": "不知道为什么天天抑郁",
      "Labels": [
        "狂躁症子标题"
      ],
      "ReplyCount": 1,
      "CreateTime": "2016-10-18 18:12:45"
    },
    {
      "Id": 60,
      "UserId": 114,
      "UserNickName": "137****3183",
      "AvatarUrl": "http://imgapi.didixl.com/image/201610/20161018181823981923-0.png@l=1",
      "CityName": "null",
      "Content": "不知道为什么天天抑郁",
      "Labels": [
        "狂躁症子标题"
      ],
      "ReplyCount": 0,
      "CreateTime": "2016-10-18 18:07:15"
    },
    {
      "Id": 59,
      "UserId": 114,
      "UserNickName": "137****3183",
      "AvatarUrl": "http://imgapi.didixl.com/image/201610/20161018181823981923-0.png@l=1",
      "CityName": "null",
      "Content": "不知道为什么天天抑郁",
      "Labels": [
        "狂躁症子标题"
      ],
      "ReplyCount": 0,
      "CreateTime": "2016-10-18 18:04:39"
    },
    {
      "Id": 58,
      "UserId": 114,
      "UserNickName": "137****3183",
      "AvatarUrl": "http://imgapi.didixl.com/image/201610/20161018181823981923-0.png@l=1",
      "CityName": "null",
      "Content": "不知道为什么天天抑郁",
      "Labels": [
        "狂躁症子标题"
      ],
      "ReplyCount": 0,
      "CreateTime": "2016-10-18 18:04:03"
    },
    {
      "Id": 57,
      "UserId": 114,
      "UserNickName": "137****3183",
      "AvatarUrl": "http://imgapi.didixl.com/image/201610/20161018181823981923-0.png@l=1",
      "CityName": "null",
      "Content": "不知道为什么天天抑郁",
      "Labels": [
        "狂躁症子标题"
      ],
      "ReplyCount": 2,
      "CreateTime": "2016-10-18 15:14:03"
    },
    {
      "Id": 56,
      "UserId": 55,
      "UserNickName": "test_dd4",
      "AvatarUrl": "http://imgapi.didixl.com/image/201608/20160817105434716137-1.png@l=1",
      "CityName": "null",
      "Content": "2343463434",
      "Labels": [
        "L"
      ],
      "ReplyCount": 1,
      "CreateTime": "2016-10-18 14:26:30"
    },
    {
      "Id": 55,
      "UserId": 114,
      "UserNickName": "137****3183",
      "AvatarUrl": "http://imgapi.didixl.com/image/201610/20161018181823981923-0.png@l=1",
      "CityName": "null",
      "Content": "不知道为什么天天抑郁",
      "Labels": [
        "狂躁症子标题"
      ],
      "ReplyCount": 1,
      "CreateTime": "2016-10-18 14:12:36"
    }
  ],
  "HasPreviousPage": "false",
  "HasNextPage": "true"
}
def list_all_dict(dict_a):

    if isinstance(dict_a,dict):
            for temp_key in dict_a.keys():
                temp_value = dict_a[temp_key]
                print("%s : %s %s" %(temp_key,temp_value,type(temp_value)))
                list_all_dict(temp_value)
    elif isinstance(dict_a,list):
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            if isinstance(dict_b,dict):
                for temp_key in dict_b.keys():
                    #print(dict_b[temp_key])
                    temp_value = dict_b[temp_key]
                    print("%s : %s %s" %(temp_key,temp_value,type(temp_value)))
                    list_all_dict(temp_value)
            else:
                print(dict_b)

list_all_dict(dict_a)





