#!/bin/bash

echo './solve.sh [challenge ip]'

curl http://${1:-localhost} -H 'Host:flag'
