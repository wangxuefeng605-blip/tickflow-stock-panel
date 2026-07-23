import requests


url="https://push2his.eastmoney.com"


r=requests.get(
    url,
    timeout=10
)


print(r.status_code)
print(r.text[:100])