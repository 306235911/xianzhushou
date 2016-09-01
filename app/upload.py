# -*- coding: utf-8 -*-
import time
import urllib
import urllib2
import json
import base64
import hmac
import hashlib

## 从贴图库（tietuku.com）相册获取图片

##获取相册信息API
#tmp_params={ "deadline": deadline, "action": "get", "uid":1}
#url="http://api.tietuku.com/v1/Album"

##秘钥
AccessKey = '943de1cd1238eaf9a7d50e5fb9ed5fce2186eb77'
SecretKey = '27fbc6dd555c2802f3c2cbac55f33f67cccee56a'

##预设变量，也可通过相册API获取
album_id = 1;
album_pages = 1;

result = ""

for page in range(1,album_pages+1):
    ##请求参数和URL
    deadline = int(time.time())+ 60
    tmp_params={ "deadline": deadline, "action": "album", "aid":album_id, "page_no":page}
    url="http://api.tietuku.com/v1/List"

    ##请求参数与秘钥生成Token
    jsoncode = json.dumps(tmp_params)
    encodedParam = base64.b64encode(jsoncode)
    sign = hmac.new(SecretKey, encodedParam, digestmod=hashlib.sha1).hexdigest()
    encodedSign = base64.b64encode(sign)
    Token = AccessKey + ':' + encodedSign + ':' + encodedParam

    ##发送http请求
    parameters = {"Token": Token}
    data = urllib.urlencode(parameters)
    request=urllib2.Request(url,data)
    response=urllib2.urlopen(request)

    res_data = response.read()
    res_dict=json.loads(res_data)

    for e in res_dict["pic"]:
        result = result + e["name"]+" : "+"\""+e["linkurl"]+"\"" +",\n"

print result