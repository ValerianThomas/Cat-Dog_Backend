#!/bin/sh

cd /Model_api
gunicorn -b 0.0.0.0:"$PORT" --workers=2 wsgi:app