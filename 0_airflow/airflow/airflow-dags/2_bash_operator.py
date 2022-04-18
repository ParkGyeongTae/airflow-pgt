from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
	'owner' : 'ParkGyeongTae'
}

dag = DAG (
	dag_id            = 'my_first_bash_dag',
	start_date        = datetime(2022, 4, 16),
	schedule_interval = '* * * * *',
	catchup           = False,
	tags              = ['박경태'],
	description       = 'Sample',
	default_args      = default_args
	)

sleep_1 = BashOperator (
	task_id      = 'sleep_1',
	bash_command = 'sleep 10',
	dag          = dag
    )

sleep_2 = BashOperator (
	task_id      = 'sleep_2',
	bash_command = 'sleep 10',
	dag          = dag
    )

sleep_3 = BashOperator (
	task_id      = 'sleep_3',
	bash_command = 'sleep 10',
	dag          = dag
    )

sleep_4 = BashOperator (
	task_id      = 'sleep_4',
	bash_command = 'sleep 5',
	dag          = dag
    )

sleep_5 = BashOperator (
	task_id      = 'sleep_5',
	bash_command = 'sleep 5',
	dag          = dag
    )

sleep_6 = BashOperator (
	task_id      = 'sleep_6',
	bash_command = 'sleep 5',
	dag          = dag
    )

sleep_1 >> sleep_2 >> sleep_3 >> sleep_4 >> sleep_5 >> sleep_6