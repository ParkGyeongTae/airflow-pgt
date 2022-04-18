from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


def print_hello():
	print("hello!")
	return "hello!"

def print_goodbye():
	print("goodbye!")
	return "goodbye!"


#DAG 설정
dag = DAG (
	dag_id = 'my_first_dag',
	start_date = datetime(2022, 4, 16),
	schedule_interval = '* * * * *',
    catchup = False
    )

#DAG Task 작성
print_hello = PythonOperator (
	task_id         = '1_print_hello',
	python_callable = print_hello,
	dag             = dag
    )

print_goodbye = PythonOperator(
	task_id         = '2_print_goodbye',
	python_callable = print_goodbye,
	dag             = dag
    )

print_hello >> print_goodbye