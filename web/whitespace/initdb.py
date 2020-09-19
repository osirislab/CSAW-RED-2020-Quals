import os
import hashlib
import sqlite3

def get_random():
    """Generate a random string."""
    return hashlib.sha512(os.urandom(32)).hexdigest()


DB_FILE = '/tmp/db.db'

# Reset the database
if os.path.isfile(DB_FILE):
    os.remove(DB_FILE)

# Create a new one and add my admin user
db = sqlite3.connect(DB_FILE)
c = db.cursor()
c.execute('CREATE TABLE users (username VARCHAR(256), password VARCHAR(256));')
c.execute('INSERT INTO users VALUES (?, ?);', ('admin', get_random()))
c.close()
db.commit()
