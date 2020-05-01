#!bin/bash
sleep 9999
python3 migrate.py
gunicorn $@
