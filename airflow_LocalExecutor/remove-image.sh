#!/bin/bash

docker rmi -f airflow-pgt:0.01
docker rmi -f postgresql-airflow-pgt:0.01
docker rmi -f dpage/pgadmin4:6.8