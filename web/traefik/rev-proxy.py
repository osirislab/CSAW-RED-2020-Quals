from flask import Flask, request, render_template
from flag import flag
import requests

app = Flask(__name__)

valid_hosts = {
    'rev-proxy.csaw.io' : 'site',
    'localhost' : 'localhost', # for debugging
}


@app.route('/')
@app.route('/<path:path>')
def route_all(path):
    host = request.headers.get('host', default=None)
    x_real_ip = request.headers.get('x-real-ip', default=None)
    ip = request.remote_addr

    if x_real_ip is not None:
        # request has come from another proxy
        # stop here to avoid loop
        return '404 page not found', 404

    if host == 'flag':
        return flag

    if host != 'rev-proxy.csaw.io':
        return '404 page not found', 404

    return render_template(path)



if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
