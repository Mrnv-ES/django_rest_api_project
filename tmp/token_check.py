import requests

response = requests.post(
    'http://127.0.0.1:8000/api-token-auth/',
    data={
        'username': 'django',
        'password': 'geekbrains'
    }
)

print(response.status_code)
print(response.json())

# 200
# {'token': '086a153de4d99da733c66f94ce7d8e8e042a0b50'}