# -*-coding:utf-8-*-
import datetime
import json
import time
import uuid
import hmac
from hashlib import sha1
from hashlib import sha256
import urllib
import copy

import curlify
import httplib2

# 填写您的accesskey 和secretKey
import requests
from urllib3.util import url

access_key = "7bee2d8d0a38429dbaaade711bc42baf"
secret_key = "9a7bd2bb5f50488eb16dcb0547b12435"
# 签名计算
def sign(http_method, playlocd, servlet_path):
    #time_str = datetime.datetime.now().isoformat()
    time_str = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())
    playlocd['Timestamp'] = time_str
    parameters = copy.deepcopy(playlocd)
    parameters.pop('Signature')
    sorted_parameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
    canonicalized_query_string = ''
    for (k, v) in sorted_parameters:
        canonicalized_query_string += '&' + percent_encode(k) + '=' + percent_encode(v)
    string_to_sign = http_method + '\n' \
 \
                     + percent_encode(servlet_path) + '\n' \
 \
                     + sha256(canonicalized_query_string[1:].encode('utf-8')).hexdigest()

    key = ("BC_SIGNATURE&" + secret_key).encode('utf-8')
    string_to_sign = string_to_sign.encode('utf-8')
    signature = hmac.new(key, string_to_sign, sha1).hexdigest()
    return signature
# 参数编码
def percent_encode(encode_str):
    encode_str = str(encode_str)
    res = urllib.parse.quote(encode_str.encode('utf-8'), '')
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res



# 签名公参，如果有其他参数，同样在此添加
querystring = {"AccessKey": access_key, "Timestamp": "", "Signature": "",
                "SignatureMethod": "HmacSHA1", "SignatureNonce": "", "SignatureVersion": "V2.0"}
headers = {'Content-Type': 'application/json'}
# 请求body
payload = { "productType":"vm",
                "bootVolume":{
                    "size":40,
                    "volumeType":"highPerformance"
                },
                "specsName":"t2.medium.4",
                "quantity":1,
                "duration":1,
                "feeUnit":"month"}
# 生成SignatureNonce
querystring['SignatureNonce'] = uuid.uuid4()
# 生成签名
querystring['Signature'] = sign('POST', querystring, '/api/v2/server/query/price')
print(querystring)
    # url = 'api-beijing-1.cmecloud.cn'+'?'+querystring
    # httpClient = httplib2.HTTPSConnectionWithTimeout(url,8443,timeout=30)
    # headers = {'Content-Type': 'application/json'}
    # httpClient.request('GET','/api/v2/region',headers=headers)
    # response = httpClient.getresponse()
    # print(response.status)
    # print(response.getheaders())
test = requests.post('https://api-wuxi-1.cmecloud.cn:8443/api/v2/server/query/price', headers=headers, params=querystring, json=payload)
# 转化为curl命令
ci = curlify.to_curl(test.request)
print('============================================================')
# 将request转换成curl
print(ci)
print('============================================================')
print('url : %s' % url)
result = json.loads(test.text)
print(result)
try:
    assert result.get('state') == 'OK'
    print('response: %s' % json.dumps(result, indent=4, ensure_ascii=False))
except AssertionError as ae:
    print(json.dumps(result, indent=4, ensure_ascii=False))
