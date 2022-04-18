# /airflow-pgt/0_airflow


## DAG
1. dag_id = 'first_dag',
2. default_args = default_args,
3. description = 'Sample DAG',
4. start_date = datetime(2022, 1, 1), : DAG가 시작되는 기준 시점 (start_date 는 최소 하루전)
5. schedule_interval = '0 15 * * *', : 매일 15시에 한번
6. schedule_interval = '0 */1 * * *', : 매일 1시간마다
7. schedule_interval = timedelta(minutes = 1), : 1분마다
8. catchup = False,
9. tags = ['박경태', 'sample'] : 태그


## 기타
1. airflow db init
2. airflow scheduler -D
3. airflow webserver -D -p 28080