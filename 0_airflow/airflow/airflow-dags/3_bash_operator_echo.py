from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
	'owner' : 'ParkGyeongTae'
}

dag = DAG (
	dag_id            = '3_bash_operator_echo',
	start_date        = datetime(2022, 5, 4),
	schedule_interval = '* * * * *',
	catchup           = False,
	tags              = ['test'],
	description       = 'Bash Operator Sample',
	default_args      = default_args
	)

echo_1 = BashOperator (
	task_id      = 'echo_1',
	bash_command = 'echo "1"',
	dag          = dag
    )

echo_2 = BashOperator (
	task_id      = 'echo_2',
	bash_command = 'echo "2"',
	dag          = dag
    )

echo_3 = BashOperator (
	task_id      = 'echo_3',
	bash_command = 'echo "3"',
	dag          = dag
    )

echo_4 = BashOperator (
	task_id      = 'echo_4',
	bash_command = 'echo "4"',
	dag          = dag
    )

echo_5 = BashOperator (
	task_id      = 'echo_5',
	bash_command = 'echo "5"',
	dag          = dag
    )

echo_6 = BashOperator (
	task_id      = 'echo_6',
	bash_command = 'echo "6"',
	dag          = dag
    )

[echo_1, echo_2] >> echo_3 >> [echo_4, echo_5] >> echo_6