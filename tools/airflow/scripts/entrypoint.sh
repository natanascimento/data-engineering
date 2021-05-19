#!/usr/bin/env bash
airflow db init
airflow users create -r Admin -u admin -e admin@natanascimento.com -f admin -l user -p natan12345
airflow webserver