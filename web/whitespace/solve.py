import requests


username = '  admin  '

r = requests.post(
    'http://localhost:5000/register',
    data={'username': username, 'password': 'password'})
print(r.text)

r = requests.post(
    'http://localhost:5000/login',
    data={'username': username, 'password': 'password'})
print(r.text)
