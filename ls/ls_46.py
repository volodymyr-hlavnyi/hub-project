import requests
response = requests.get("https://example.com")
print(response.status_code) # Выводит код состояния ответа
print(response.headers) # Выводит данные, полученные от сервера

import requests
response = requests.get("https://api.github.com/users/github")
data = response.json()
for k, v in data.items():
    print(f"{k}: {v}")

response = requests.get("https://example.com")
print(response.cookies) # Выводит cookie, полученные от сервера
cookies = {"session_id": "123456789"}
response = requests.get("https://example.com", cookies=cookies)

response = requests.get('https://random-data-api.com/api/v2/users?size=10')
res=response.json()
for person in res:
    print(f"{person['last_name']:12} {person['first_name']:10} {person['email']}")
