#!/usr/bin/env bash
source env/local/bin/activate ;
source env/bin/activate ;
./manage.py rabbitmq_consume ;
