import os
import logging
import pandas as pd
from datetime import datetime
from process import process_dataset, successful

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, 'test_log.log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

def do_logging(summary) :
    logger.info(summary)

def cron_job():
    
    current_file_path = os.path.abspath(__file__)
    folder_path = os.path.join(os.path.dirname(current_file_path), 'raw_datasets')

    current_date_hour = datetime.now().strftime('%Y%m%d_%H')
    name = f'{current_date_hour}hour.csv'

    file_list = [file for file in os.listdir(folder_path) if file.endswith(name)]

    combined_df = pd.DataFrame()
    for csv_file in file_list:
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    initial_rows, nomissing, missing_field, filename, df = process_dataset(combined_df, name)
    success_len, success_filename = successful(df, name)
    unsuccessful_len = initial_rows - success_len
    percentage = round(success_len/initial_rows*100,2)
    under = unsuccessful_len - missing_field

    summary = f""" 
- Number of rows processed: {initial_rows}
- Number of rows with proper entries eg no missing fields: {nomissing}
    - Processed file of all applicants with no missing fields: {filename}
- Successful applications in this month: {percentage}%:
    - Number of successful applications: {success_len}
    - File with successful applicants: {success_filename}
- Number of unsuccessful applications: {unsuccessful_len}, with
    - Number of rows with missing fields: {missing_field}, 
    - Number of applicants under 18y/o: {under}
"""

    do_logging(summary)

