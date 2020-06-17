#!/bin/bash

echo './solve.sh [challenge ip]'

curl http://${1:-localhost}:5000 -H 'Host:flag'
