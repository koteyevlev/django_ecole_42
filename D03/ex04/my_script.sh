#!/bin/zsh

python3 -m virtualenv --python=python3 django_venv
source django_venv/bin/activate
pip3 --version
pip3 install -r requirement.txt
