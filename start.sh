#!/bin/bash

echo "Will Kill uWsgi."
ps -ef | grep uwsgi | grep -v grep | awk '{print $2}' | xargs -n 1 kill -9
echo "Killed! Will start uWsgi."
#uwsgi -x django.xml
cd $(dirname $0)
uwsgi -s :8630 -w wsgi -M -p 8 -t 30 -d /var/log/uwsgi/uwsgi.log --max-requests 500 --log-maxsize 5000000
echo "Start completed!"
