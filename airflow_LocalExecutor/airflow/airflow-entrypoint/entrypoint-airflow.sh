#!/bin/bash

sleep 5

airflow db init

sleep 1

airflow users create --role Admin --username dev3 --email dev3 --firstname dev3 --lastname dev3 --password dev3

sleep 1

airflow scheduler -D

sleep 1

airflow webserver -D -p 8080

sleep 1

bash