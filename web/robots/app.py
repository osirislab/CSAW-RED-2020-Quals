from flask import Flask

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
    return robots

@app.route('/super-duper-extra-secret-very-interesting')
def flag():
    return 'flag{welcome_to_website_hacking}'

if __name__ == "__main__":
    app.run()
