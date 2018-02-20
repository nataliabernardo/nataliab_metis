from flask import Flask
from flask import request
from flask import render_template
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

#---------- MODEL IN MEMORY ----------------#

# Read the scientific data on breast cancer survival,
# Build a LogisticRegression predictor on it


#---------- URLS AND WEB PAGES -------------#

# Initialize the app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('first_app.html')
@app.route("/pred2", methods=['POST'])
def pred2():
    return('hello world')


# Get an example and return it's score from the predictor model
@app.route("/pred", methods=['POST','GET'])
def render_message():
    if request.method=='POST':
        result=request.form
        sex = result['sex_M']
        #family_support = result['famsup_yes']
        #tutoring = result['paid_yes']
        address = result['address_U']
        higher_education = result['higher_yes']
        internet = result['internet_yes']
        romantic_relationship = result['romantic_yes']
        #Medu = result['Medu']
        #Fedu = result['Fedu']
        #famrel = result['famrel']
        failures = result['failures']
        absences = result['absences']


        """  When A POST request with json data is made to this uri,
            Read the example from the json, predict probability and
            send it with a response
        """



        #return render_template('result.html',score=score_perc)

        message = muffin_or_cupcake(sex,
                        address,
                        higher_education,
                        internet,
                        romantic_relationship,
                        failures,
                        absences)

    return render_template('index.html',
                           message=message)

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)

app.run(host='0.0.0.0', port=8000)
app.run(debug=True)