#!bin/bash
python3 migrate.py
gunicorn $@