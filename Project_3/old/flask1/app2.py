from flask import Flask
from flask import render_template
from sklearn.linear_model import LogisticRegression
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

X = students[['famsup_yes','higher_yes','romantic_yes']]
y = students['G3']

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

PREDICTOR = LogisticRegression().fit(X,y)

#---------- URLS AND WEB PAGES -------------#

# Initialize the app
app = Flask(__name__)

@app.route("/")
def viz_page():
    """
    Homepage: serve our visualization page, first_app.html
    """
    with open("first_app2.html", 'r') as viz_file:
        return viz_file.read()

# Get an example and return it's score from the predictor model
@app.route("/score", methods=["POST"])

def predictmodel():

    data = flask.request.json
    X_test = np.matrix(data["example"])

    #X_test = pd.DataFrame({'famsup': [famsup], 'higher': [higher], 'relationship': [relationship]})

    print (X_test)
    score = PREDICTOR.predict_proba(X_test)
    prediction = PREDICTOR.predict(X_test)
    results = {"score": score[0,1]}
    return(prediction)

#print (predictmodel(0, 0, 1))

#--------- RUN WEB APP SERVER ------------#
app.debug = True
# Start the app server on port 80
# (The default website port)

app.run(host='0.0.0.0', port=8000)