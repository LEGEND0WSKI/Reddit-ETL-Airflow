import os
import sys
from datetime import datetime 
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# easily import packages from anywhere near the location
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.aws_s3_pipeline import upload_s3_pipeline


default_args = {
    'owner': 'Siddhesh Koli',
    'start_date':datetime(2024,2,19)
}

# file name readability
file_postfix = datetime.now().strftime("%Y%m%d")

# create a dag
dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup = False,
    tags= ['reddit','etl','pipeline','data']
)

# extract from reddit 
extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable = reddit_pipeline,
    op_kwargs= {
        'file_name':f'reddit_{file_postfix}',
        'subreddit': 'politics',                      #add a subreddit here(check case)#
        'time_filter': 'day',
        'limit':100
    },
    dag = dag
)

# upload to s3
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

# creates a dependency before using s3
extract >> upload_s3