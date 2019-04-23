# Python 3.7 is required!
import base64
import json
import os
import requests
import sys

uId = None
uPw = None

with open('id.visa', 'r') as fp:
    uId = fp.read()

with open('pw.visa', 'r') as fp:
    uPw = fp.read()

uAuth = (uId + ':' + uPw).encode('utf-8')

clCertPath = 'cert.pem'
clKeyPath = 'key.pem'

APIURL = 'https://sandbox.api.visa.com/vdp/helloworld'

reqHeaders = {'Accept': 'application/json', 'Authorization': base64.b64encode(uAuth).decode('utf-8')}
req = requests.get(APIURL, cert = (clCertPath, clKeyPath), headers = reqHeaders, auth = (uId, uPw))
resObj = json.loads(req.text)
print(resObj['timestamp'])
print(resObj['message'])
