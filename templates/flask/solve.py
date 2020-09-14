import requests

print('post')
requests.post(
    'http://web.chal.csaw.io:5000/',
)

print('get')
requests.get("http://web.chal.csaw.io:5000/flag")
