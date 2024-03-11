from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH
from etls.reddit_etl import connect_reddit, extract_posts, transform_data,load_data_to_csv
import pandas as pd
## import os

# combines all 4 etl functions from reddit etl folder
def reddit_pipeline(file_name: str, subreddit:str, time_filter='day', limit=None):
    # 1. connct to reddit instance
    instance = connect_reddit(CLIENT_ID,SECRET,'whitemonkeydevil')
    
    # 2. extraction
    posts = extract_posts(instance,subreddit,time_filter,limit)
    post_df = pd.DataFrame(posts)

    # 3.transformattn
    post_df = transform_data(post_df)

    ## Check if the directory exists, and if not, create it
    ## if not os.path.exists(OUTPUT_PATH):
    ##     os.makedirs(OUTPUT_PATH)

    # 4. Save and write out path/filename
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df, file_path)

    return file_path