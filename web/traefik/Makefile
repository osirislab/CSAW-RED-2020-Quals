
all: run

run: venv rev-proxy.py
	./venv/bin/python rev-proxy.py

venv: requirements.txt
	virtualenv -p $(shell which python3) venv
	./venv/bin/pip install -r ./requirements.txt
