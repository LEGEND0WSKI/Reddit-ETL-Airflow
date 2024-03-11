# ETL Reddit Pipeline


## Overview
This repository contains the code for an ETL (Extract, Transform, Load) pipeline designed to extract data from Reddit, perform necessary transformations, and upload the data to AWS S3. The pipeline is implemented using Apache Airflow, Docker, and Python.

## Installation
To use this ETL pipeline, follow these steps:

1. Clone this repository to your local machine:
2. Install Docker Desktop
3. Create a virtual environment uisng python:
    ```
    python -m venv venv
    ```

4. Activate the virtual environment:

   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

6. Install the required Python dependencies:

     ```
     pip install -r requirements.txt
     ```

7. Obtain your Reddit API key and AWS secret key. These keys are required for accessing the Reddit API and AWS S3, respectively.

8. Make changes to the config file config.conf

## Usage
To run the ETL pipeline:

1. Start Docker containers:
    ```
    docker-compose up -d --build
    ```

2. Trigger the Airflow DAG `etl_reddit_pipeline` either manually from the Airflow UI or using the Airflow CLI.
    ```
    http://localhost:8080/
    ```
3. Monitor the progress of the DAG execution in the Airflow UI.

## Output is ready in your output folder as well as s3.
There are 5 main places to make changes
1. dags
2. etls
3. pipelines
4. config
5. utils