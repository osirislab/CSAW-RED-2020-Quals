from flask import Flask, make_response

app = Flask(__name__)

robots = """
User-agent: *
Allow: /
Disallow: /super-duper-extra-secret-very-interesting
"""

@app.route('/')
def index():
    return 'Only robots can find the treasure that I hold....'

@app.route('/robots.txt')
def robot():
    r = make_response(robots)
    r.headers['Content-Type'] = 'text/plain'
    return r

@app.route('/super-duper-extra-secret-very-interesting')
def flag():
    return 'flag{welcome_to_website_hacking}'

if __name__ == "__main__":
    app.run()
