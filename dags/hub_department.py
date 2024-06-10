from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

# Установите аргументы по умолчанию для DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retry_delay': timedelta(minutes=5),
}

# Определите DAG
dag = DAG(
    'spark_streaming_dag',
    default_args=default_args,
    description='A simple Spark Streaming DAG',
    schedule_interval=timedelta(days=1),
)

# Определите задачу SparkSubmitOperator
spark_submit_task = SparkSubmitOperator(
    task_id='spark_submit_task',
    application='sripts/hub_department_script.py',  # Путь к вашему Spark Streaming скрипту
    conn_id='spark_default',  # Подключение Spark, определенное в Airflow
    conf={'spark.master': 'spark://localhost:7077'},  # Адрес Spark Master
    name='spark_streaming_task',
    dag=dag,
)

# Установите зависимости задач, если они есть
spark_submit_task
