#!/usr/bin/env bash
/etc/init.d/fcgiwrap start
service nginx start

/opt/.dev/auth/venv/bin/python /opt/.dev/auth/app.py
