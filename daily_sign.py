import requests

url = ("https://api.hayfrp.com")

headers = {
    "waf": "off"
}
body = {
    "key1": "value1", 
    "key2": "value2"}

response = requests.post(url=url, data=body, headers=headers)
print(response.text)
