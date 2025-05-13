import requests



response = requests.get('https://reqres.in/api/users?page=2')
data = response.json()

print("Список пользователей:")
for user in data['data']:
    print(f"{user['first_name']} {user['last_name']} — {user['email']}")