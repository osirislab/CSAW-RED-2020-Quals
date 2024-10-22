from flask import Flask, request, render_template, send_from_directory
from flag import flag
import os
import requests

app = Flask(__name__)


@app.route('/static/<path:path>')
def serve_da_static(path):
    return send_from_directory(os.path.join(os.getcwd(), 'static'), path)


@app.route('/')
@app.route('/<path:path>')
def route_all(path='index.html'):
    host = request.headers.get('host', default=None)
    x_real_ip = request.headers.get('x-real-ip', default=None)
    ip = request.remote_addr

    if x_real_ip is not None:
        # request has come from another proxy
        # stop here to avoid loop
        return '404 page not found', 404

    if host == 'flag':
        return flag

    print(host)

    if host != 'web.red.csaw.io:5006':
        return '404 page not found', 404

    return render_template(path)



if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
