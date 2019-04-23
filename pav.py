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

APIURL = 'https://sandbox.api.visa.com/pav/v1/cardvalidation'

cardInfo = {
    'cardCvv2Value': '',
    'cardExpiryDate': '',
    'primaryAccountNumber': ''
}

cardInfo['cardCvv2Value'] = input('CVC > ')
cardInfo['cardExpiryDate'] = input('CED > ')
cardInfo['primaryAccountNumber'] = input('PAN > ')

reqHeaders = {
    'Accept': 'application/json',
    'Authorization': base64.b64encode(uAuth).decode('utf-8'),
    'Content-Type': 'application/json'
}

reqData = json.dumps(cardInfo)
req = requests.post(APIURL, cert = (clCertPath, clKeyPath), headers = reqHeaders, auth = (uId, uPw), data = reqData)
res = json.loads(req.text)

if res['actionCode'] != '00' or res['responseCode'] != '5': print('Something is wrong!')
if res['cvv2ResultCode'] == 'M': print('Your card is good!')
elif res['cvv2ResultCode'] == 'P': print('You can input test data only!')
else: print('You are fraud!')

print('The end')
exit(0)
