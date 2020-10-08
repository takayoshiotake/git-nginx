#!/usr/bin/env bash
/etc/init.d/fcgiwrap start
service nginx start

/opt/auth/venv/bin/python /opt/auth/app.py
