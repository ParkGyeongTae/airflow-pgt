from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pprint

dag = DAG(
	dag_id = '4_python_operator_context',
	start_date = datetime(2022, 12, 3),
	schedule_interval = '* * * * *',
	catchup = False,
	tags = ['server_local', 'detail_test'],
	description = 'Python Operator Sample',
	default_args = {'owner': 'ParkGyeongTae'})

def func_print_context(**context):
    return pprint.pprint(context)

def func_print_kwargs(**kwargs):
    return pprint.pprint(kwargs)

task_print_context = PythonOperator(task_id = 'print_context', python_callable = func_print_context, dag = dag, do_xcom_push = False)
task_print_kwargs = PythonOperator(task_id = 'print_kwargs', python_callable = func_print_kwargs, dag = dag, do_xcom_push = False)

task_print_context >> task_print_kwargs