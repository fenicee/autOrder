# -*-coding:utf-8-*-

import uuid
import requests
import json
import hmac
from hashlib import sha1
from hashlib import sha256
import urllib
import copy
import time
import curlify


class RequestMsgByUrl:
    def __init__(self,access_key,secret_key,method,endpoint,path,body):
        self.access_key = access_key
        self.secret_key = secret_key
        self.method = method
        self.endpoint = endpoint
        self.path = path
        self.body = body

    # 参数编码
    def percent_encode(self,encode_str):
        encode_str = str(encode_str)
        res = urllib.parse.quote(encode_str.encode('utf-8'), '')
        res = res.replace('+', '%20')
        res = res.replace('*', '%2A')
        res = res.replace('%7E', '~')
        return res
    # 签名计算
    def sign(self,http_method, playlocd, servlet_path):
        time_str = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())
        playlocd['Timestamp'] = time_str
        parameters = copy.deepcopy(playlocd)
        parameters.pop('Signature')
        sorted_parameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
        canonicalized_query_string = ''
        for (k, v) in sorted_parameters:
            canonicalized_query_string += '&' + self.percent_encode(k) + '=' + self.percent_encode(v)
        string_to_sign = http_method + '\n' \
     \
                         + self.percent_encode(servlet_path) + '\n' \
     \
                         + sha256(canonicalized_query_string[1:].encode('utf-8')).hexdigest()

        key = ("BC_SIGNATURE&" + self.secret_key).encode('utf-8')
        string_to_sign = string_to_sign.encode('utf-8')
        signature = hmac.new(key, string_to_sign, sha1).hexdigest()
        return signature

    def requestByUrl(self):
        method = self.method
        endpoint = self.endpoint
        endpointurl = {
            "CIDC-RP-25":"api-wuxi-1.cmecloud.cn:8443",
            "CIDC-RP-26":"api-dongguan-1.cmecloud.cn:8443",
            "CIDC-RP-27":"api-yaan-1.cmecloud.cn:8443",
            "CIDC-RP-28":"api-zhengzhou-1.cmecloud.cn:8443",
            "CIDC-RP-29":"api-beijing-2.cmecloud.cn:8443",
            "CIDC-RP-30":"api-zhuzhou-1.cmecloud.cn:8443",
            "CIDC-RP-31":"api-jinan-1.cmecloud.cn:8443",
            "CIDC-RP-32":"api-xian-1.cmecloud.cn:8443",
            "CIDC-RP-33":"api-shanghai-1.cmecloud.cn:8443",
            "CIDC-RP-34":"api-chongqing-1.cmecloud.cn:8443",
            "CIDC-RP-35":"api-ningbo-1.cmecloud.cn:8443",
            "CIDC-RP-48":"api-huhehaote-1.cmecloud.cn:8443",
            "CIDC-RP-49":"api-guiyang-1.cmecloud.cn:8443"
        }
        url = "https://%s" % (endpointurl[endpoint])
        path = self.path
        headers = {'Content-Type': 'application/json'}
        querystring = {"AccessKey": self.access_key, "Timestamp": "2020-12-11T16:27:01Z", "Signature": "",
                            "SignatureMethod": "HmacSHA1", "SignatureNonce": "", "SignatureVersion": "V2.0"}
        body = self.body
        # 生成SignatureNonce
        querystring['SignatureNonce'] = uuid.uuid4()
        querystring['Signature'] = self.sign(method, querystring, path)
        test = requests.request(method, url + path, headers=headers, params=querystring, json=body)
        result = json.loads(test.text)
        return result

# if __name__ == '__main__':
#     # http method
#     method = 'GET'
#     # 目标域名 端口
#     url = "https://%s " % ('api-beijing-1.cmecloud.cn:8443')
#     # 请求url
#     path = '/api/v2/region'
#
#     # 可以不改
#     headers = {'Content-Type': 'application/json'}
#     # 签名公参，如果有其他参数，同样在此添加
#     querystring = {"AccessKey": access_key, "Timestamp": "2020-12-11T16:27:01Z", "Signature": "",
#                    "SignatureMethod": "HmacSHA1", "SignatureNonce": "", "SignatureVersion": "V2.0"}
#
#     # 请求body
#     payload = {}
#     # 生成SignatureNonce
#     querystring['SignatureNonce'] = uuid.uuid4()
#     # 生成签名
#     querystring['Signature'] = sign(method, querystring, path)
#     print(method, url + path, headers, querystring)
#     test = requests.request(method, url + path, headers=headers, params=querystring, json=payload)
#     # 转化为curl命令
#     ci = curlify.to_curl(test.request)
#     print('============================================================')
#     # 将request转换成curl
#     print(ci)
#     print('============================================================')
#     print('url : %s' % url)
#     result = json.loads(test.text)
#     print(result)
#     try:
#         assert result.get('state') == 'OK'
#         print('response: %s' % json.dumps(result, indent=4, ensure_ascii=False))
#     except AssertionError as ae:
#         print(json.dumps(result, indent=4, ensure_ascii=False))