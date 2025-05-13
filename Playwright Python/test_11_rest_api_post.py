import requests

payload = {
    "name": "morpheus",
    "job": "Developer"
}

response = requests.post('https://reqres.in/api/users', json=payload)
data = response.json()

print(f"Создан пользователь: {data['name']} с работой {data['job']}")
print(f"ID: {data['id']}, Время создания: {data['createdAt']}")