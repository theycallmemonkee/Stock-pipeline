from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts.extract import extract_data
from scripts.load import load_data


def run_etl():
    data = extract_data("AAPL")
    load_data(data)


with DAG(
    dag_id="simple_stock_etl",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",  
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id="run_etl",
        python_callable=run_etl
    )