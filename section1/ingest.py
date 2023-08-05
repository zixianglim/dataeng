from flask import Flask, render_template, request
import pandas as pd
import os
from datetime import datetime
import uuid
from cron import cron_job
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    submission_method = request.form['submission_method']

    current_date_hour = datetime.now().strftime('%Y%m%d_%H')

    if submission_method == 'form':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        dob = request.form['dob'].replace('-','') 
            #processing the date as per format if we clean before passing into dataset *as an example*
            #however, as stated in assignment, we will ingest first before cleaning and performing validity checks
        
        data = {
            'applicant_name': [name],
            'applicant_email': [email],
            'applicant_mobile': [mobile],
            'applicant_dob': [dob]
        }
        df = pd.DataFrame(data)

        filename = f'./raw_datasets/member_signup_{current_date_hour}hour.csv'
        df.to_csv(filename, mode='a', header=not os.path.isfile(filename), index=False)
            #a new file for each hour irregardless of number of entries
    
    elif submission_method == 'csv':
        file = request.files['csv']
        if file:
            filename = file.filename.replace('.csv','')
            filename = f'./datasets/{filename}_{str(uuid.uuid4())[:5]}_{current_date_hour}hour.csv'
            #added uuid incase of name duplication
            
            file.save(filename)

    return 'Your application is being processed. We will get back to you soon :)'

if __name__ == '__main__':

    scheduler = BackgroundScheduler()
    trigger = CronTrigger(hour='*', minute = '59') #hourly job at e.g 12.59
    scheduler.add_job(cron_job, trigger)
    scheduler.start()

    app.run(debug=True)
