# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
# from datetime import datetime

# default_args = {
# 	'owner' : 'ParkGyeongTae'
# }

# dag = DAG (
# 	dag_id = '1_python_operator',
# 	start_date = datetime(2022, 12, 3),
# 	schedule_interval = '* * * * *',
# 	catchup = False,
# 	tags = ['test'],
# 	description = 'Python Operator Sample',
# 	default_args = {'owner': 'ParkGyeongTae'}
# 	)

# def print_1():
# 	print("111")
# 	return "111"

# def print_2():
# 	print("222")
# 	return "222"

# def print_3():
# 	print("333")
# 	return "333"

# def print_4():
# 	print("444")
# 	return "444"

# def print_5():
# 	print("555")
# 	return "555"

# def print_6():
# 	print("666")
# 	return "666"

# print_11 = PythonOperator (
# 	task_id         = 'print_1',
# 	python_callable = print_1,
# 	dag             = dag
#     )

# print_22 = PythonOperator(
# 	task_id         = 'print_2',
# 	python_callable = print_2,
# 	dag             = dag
#     )

# print_33 = PythonOperator (
# 	task_id         = 'print_3',
# 	python_callable = print_3,
# 	dag             = dag
#     )

# print_44 = PythonOperator(
# 	task_id         = 'print_4',
# 	python_callable = print_4,
# 	dag             = dag
#     )

# print_55 = PythonOperator (
# 	task_id         = 'print_5',
# 	python_callable = print_5,
# 	dag             = dag
#     )

# print_66 = PythonOperator(
# 	task_id         = 'print_6',
# 	python_callable = print_6,
# 	dag             = dag
#     )

# print_11 >> print_22 >> print_33 >> print_44 >> print_55 >> print_66