from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import time

dag = DAG (
	dag_id = '5_python_operator',
	start_date = datetime(2022, 12, 10),
	schedule_interval = '* * * * *',
	catchup = False,
	tags = ['server_local', 'detail_test'],
	description = 'Python Operator Sample',
	default_args = {'owner': 'ParkGyeongTae'})

def func_print_1():
	time.sleep(120)
	return 'return_print'

task_print_1 = PythonOperator(task_id = 'print_1', python_callable = func_print_1, dag = dag, do_xcom_push = False)

task_print_1