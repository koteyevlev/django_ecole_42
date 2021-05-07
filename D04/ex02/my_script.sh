#!/bin/zsh

python3 -m virtualenv --python=python3 django_venv
source django_venv/bin/activate
pip3 --version
pip3 install -r requirements.txt
django-admin startproject d04
cd d04
python manage.py startapp ex02
