import requests

url = ("https://api.hayfrp.com")

headers = {"waf": 'off'}
data = {
    'type': 'login',
    'user':'Kirin',
    'passwd':"123456"
}

response = requests.post(url=url, data=data, headers=headers)
print(response.text)
