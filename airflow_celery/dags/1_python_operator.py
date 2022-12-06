from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

dag = DAG (
	dag_id = '1_python_operator',
	start_date = datetime(2022, 12, 3),
	schedule_interval = '* * * * *',
	catchup = False,
	tags = ['server_local', 'detail_test'],
	description = 'Python Operator Sample',
	default_args = {'owner': 'ParkGyeongTae'})

def func_print_1():
	return '1'

def func_print_2():
	return '2'

def func_print_3():
	return '3'

def func_print_4():
	return '4'

def func_print_5():
	return '5'

def func_print_6():
	return '6'

task_print_1 = PythonOperator(task_id = 'print_1', python_callable = func_print_1, dag = dag, do_xcom_push = False)
task_print_2 = PythonOperator(task_id = 'print_2', python_callable = func_print_2, dag = dag, do_xcom_push = False)
task_print_3 = PythonOperator(task_id = 'print_3', python_callable = func_print_3, dag = dag, do_xcom_push = False)
task_print_4 = PythonOperator(task_id = 'print_4', python_callable = func_print_4, dag = dag, do_xcom_push = False)
task_print_5 = PythonOperator(task_id = 'print_5', python_callable = func_print_5, dag = dag, do_xcom_push = False)
task_print_6 = PythonOperator(task_id = 'print_6', python_callable = func_print_6, dag = dag, do_xcom_push = False)

task_print_1 >> task_print_2 >> task_print_3 >> task_print_4 >> task_print_5 >> task_print_6