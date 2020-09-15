import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('host', default='localhost', nargs='?')
parser.add_argument('port', default='5000', nargs='?')
args = parser.parse_args()

r = requests.get('http://{}:{}/super-duper-extra-secret-very-interesting'.format(args.host, args.port))
print(r.text)
