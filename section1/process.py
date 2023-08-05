import pandas as pd
from dateutil.parser import parse
import hashlib
import string
import re
from datetime import datetime
import os

salutations = ['Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Miss.', 'Sir.', 'Madam.', 'Prof.', 'Rev.']
current_date_hour = datetime.now().strftime('%Y%m%d_%H_%M')

def remove_salutations(name): 
    for salutation in salutations:
        name = name.replace(salutation, '')
    return name.strip()

def format_date(date_str): #format date to YYYYMMDD
    try:
        date_obj = parse(date_str)
        return date_obj.strftime('%Y%m%d')
    except:
        return None

def process_dataset(filepath):

    df = pd.read_csv(filepath)

    #drop rows with blank space and NA in name columns
    df = df.dropna(subset=['applicant_name'], how='all', inplace=False)
    df = df[df['applicant_name'].str.strip() != '']

    #removal of salutations for more accurate retrieval of first and last name
    df.loc[:, 'applicant_name'] = df['applicant_name'].apply(remove_salutations)

    #split and get the first name
    #middle and last name combined by removing all punctuations and spaces
    name_split = df['applicant_name'].str.split(n=1, expand=True)
    trans = str.maketrans('', '', string.punctuation + ' ')
    df.loc[:, 'first_name'] = name_split[0]
    df.loc[:, 'last_name'] = name_split[1].apply(lambda x: x.translate(trans))

    #ensure numeric numbers only for mobile and that there are only 8 numbers
    df = df[pd.to_numeric(df['applicant_mobile'], errors='coerce').notnull()]
    df = df[df['applicant_mobile'].astype(str).str.len() == 8]

    #ensure email ends with .com and .net as required
    df = df[df['applicant_email'].str.endswith(('.com', '.net'))]

    #change format of date to YYYYMMDD
    #application_dob will be used for calculation, date_of_birth will be kept
    df.loc[:,'applicant_dob'] = df['applicant_dob'].apply(format_date)
    df.loc[:,'date_of_birth'] = df['applicant_dob'].apply(format_date)
    df = df.dropna(subset=['applicant_dob'], how='all', inplace=False)

    #calculating age of applicants and checking if they are above 18 years old
    df['applicant_dob'] = pd.to_datetime(df['applicant_dob'])
    df['age'] = (pd.Timestamp.now() - df['applicant_dob']).dt.days//365 #finding the days between two dates and divide by 365
    df['above_18'] = df['age'] >= 18

    filename = f'./processed_datasets/processed_{current_date_hour}' #temporary naming of file: to edit
    df.to_csv(filename, mode='a', header=not os.path.isfile(filename), index=False)

    return len(df), df

def successful(df):

    successful_df = df[df['above_18']] #only keeping those that are above 18
    successful_df = successful_df[['first_name','last_name','date_of_birth','above_18']] #filter only required columns

    #finally, generate membership ID for those who have passed the above tests
    successful_df.loc[:,'Membership_ID'] = (successful_df['last_name'] + '_' + successful_df['date_of_birth'].apply(lambda dob: hashlib.sha256(dob.encode()).hexdigest()[:5]))

    filename = f'./successful_datasets/success_{current_date_hour}' #temporary naming of file: to edit
    successful_df.to_csv(filename, mode='a', header=not os.path.isfile(filename), index=False)

    return len(successful_df)
