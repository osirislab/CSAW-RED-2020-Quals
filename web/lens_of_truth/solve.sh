#!/bin/sh

curl http://${1:-localhost}:${2:-5000}/ | grep flag
