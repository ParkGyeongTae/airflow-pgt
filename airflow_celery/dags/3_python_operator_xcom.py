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

def func_xcom_push_3(**context):
    xcom_key, xcom_value = 'xcom_push_key_3', 'xcom_push_value_3'
    return context['task_instance'].xcom_push(key = xcom_key, value = xcom_value)

task_xcom_push_3 = PythonOperator(task_id = 'xcom_push_3', python_callable = func_xcom_push_3, dag = dag, do_xcom_push = True)

task_xcom_push_3