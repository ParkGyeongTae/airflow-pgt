from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

dag = DAG (
	dag_id = '3_python_operator_xcom',
	start_date = datetime(2022, 12, 3),
	schedule_interval = '* * * * *',
	catchup = False,
	tags = ['server_local', 'detail_test'],
	description = 'Python Operator Sample',
	default_args = {'owner': 'ParkGyeongTae'})

def func_xcom_push_1(**context):
    return context['task_instance'].xcom_push(key = 'xcom_push_key_1', value = 'xcom_push_value_1')

task_xcom_push_1 = PythonOperator(task_id = 'xcom_push_1', python_callable = func_xcom_push_1, dag = dag, do_xcom_push = True)

task_xcom_push_1