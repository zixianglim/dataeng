from flask import Flask, render_template, request
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    mobile = request.form['mobile']
    dob = request.form['dob'].replace('-','') 
        #preprocessing the date as per format before passing into dataset as an example
        #however, in this case, we will ingest first before cleaning and performing validity checks
    
    data = {
        'applicant_name': [name],
        'applicant_email': [email],
        'applicant_mobile': [mobile],
        'applicant_dob': [dob]
    }
    df = pd.DataFrame(data)

    current_date_hour = datetime.now().strftime('%Y-%m-%d_%H')
    filename = f'./datasets/member_signup__{current_date_hour}hour.csv'
    df.to_csv(filename, mode='a', header=not os.path.isfile(filename), index=False)
        #a new file for each hour irregardless of number of entries

    return 'Your application is being processed. We will get back to you soon :)'

if __name__ == '__main__':
    app.run(debug=True)
