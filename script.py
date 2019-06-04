import requests

a = "a"
r = requests.get("https://coreyms.com")
print(r.status_code)
