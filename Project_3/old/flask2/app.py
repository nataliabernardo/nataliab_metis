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
students = pd.read_csv("df_students.csv")
students.columns=['G1', 'G2', 'G3', 'school_MS', 'sex_M', 'address_U', 'famsize_LE3',
       'Pstatus_T', 'schoolsup_yes', 'famsup_yes', 'paid_yes',
       'activities_yes', 'nursery_yes', 'higher_yes', 'internet_yes',
       'romantic_yes', 'age', 'Medu', 'Fedu', 'traveltime', 'studytime',
       'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences',
       'failures', 'Mjob_health', 'Mjob_other', 'Mjob_services',
       'Mjob_teacher', 'Fjob_health', 'Fjob_other', 'Fjob_services',
       'Fjob_teacher', 'reason_home', 'reason_other', 'reason_reputation',
       'guardian_mother', 'guardian_other']

#X = students[['sex_M','famsup_yes','higher_yes', 'romantic_yes','Medu', 'Fedu', 'famrel', 'failures','absences']]
#X = students[['sex_M','famsup_yes','paid_yes','higher_yes', 'romantic_yes','Medu', 'Fedu', 'failures','absences']]
X = students[['sex_M','address_U','higher_yes', 'internet_yes','romantic_yes','failures','absences']]
y = students['G3']

#PREDICTOR = LogisticRegression().fit(X,y)
PREDICTOR = RandomForestClassifier(max_depth=15, n_estimators=18, n_jobs = -1,random_state =50).fit(X,y)

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
def pred():
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

        X_test = pd.DataFrame({'sex': [sex], 'address': [address], 'higher_education': [higher_education], 'internet': [internet], 'romantic_relationship': [romantic_relationship],'failures': [failures], 'absences': [absences]})
        
        score = PREDICTOR.predict_proba(X_test)[0,1]

        score_perc = str(round(score * 100,2)) + "%"
        prediction = str(PREDICTOR.predict(X_test)[0])


        threshold = 0.3
        prediction2 = str(np.where(score >= threshold, 1, 0))

        return render_template('result.html',score=score_perc)

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)

app.run(host='0.0.0.0', port=8000)
app.run(debug=True)