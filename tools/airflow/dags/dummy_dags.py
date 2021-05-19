from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

with DAG('example_dag', start_date=datetime.now()) as dag:
    op = DummyOperator(task_id='op')