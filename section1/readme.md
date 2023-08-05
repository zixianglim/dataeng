**E-commerce Company Product Pipeline**
This repository contains the code for an E-commerce company's product pipeline. The pipeline is designed and implemented to process membership applications submitted by users.

**Requirements**
The pipeline is built with Python and requires the following dependencies:
- python 3.x
- pandas
- flask
- apscheduler

**Pipeline Overview**

1. It uses the Flask framework to allow users to sign up through a membership form or in this case, to upload a csv file of applicants
2. Saved these raw files into a folder: raw_datasets
3. Schedule a job hourly with Cron to process and approve successful applications
4. Save the processed files into their folders and log the summary into test_log.log

**How to run**
1. Navigate to the section1 directory: cd ./section1
2. Run the ingest.py script using Python: python ingest.py
