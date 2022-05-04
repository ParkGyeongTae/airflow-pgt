#!/bin/bash

service postgresql start
sleep 1
sudo -u postgres psql -U postgres -c "CREATE DATABASE airflow;"
sleep 1
sudo -u postgres psql -U postgres -c "CREATE USER gyeongtae with ENCRYPTED password 'gyeongtae';"
sleep 1
sudo -u postgres psql -U postgres -c "GRANT all privileges on DATABASE airflow to gyeongtae;"
sleep 1
sudo -u postgres psql -U postgres -d airflow -c "GRANT all privileges on all tables in schema public to gyeongtae;"
sleep 1
bash