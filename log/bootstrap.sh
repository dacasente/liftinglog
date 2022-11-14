#!/bin/sh
export FLASK_APP=./liftlog/index.py

python -m flask --debug run -h 0.0.0.0