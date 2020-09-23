#!/bin/sh

python3 initdb.py

exec gunicorn -b 0.0.0.0:5000 -w 8 --preload app:app
