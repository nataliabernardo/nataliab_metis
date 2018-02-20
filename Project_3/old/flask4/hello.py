from flask import Flask, render_template, request, jsonify
import sys
import json
import logging
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from logging.handlers import RotatingFileHandler

#---------- MODEL IN MEMORY ----------------#

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

X = students[['sex_M','address_U','higher_yes', 'internet_yes','romantic_yes','failures','famrel']]
y = students['G3']

PREDICTOR = RandomForestClassifier(max_depth=15, n_estimators=18, n_jobs = -1,random_state =50).fit(X,y)

#---------- URLS AND WEB PAGES -------------#

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("index.html")

@app.route("/calculate/", methods=['GET','POST'])
def calculate():
	json = request.get_json()
	#number1 = json['number1']
	#number2 = json['number2']
	#number3 = json['number3']

	sex = json['sex_M']
	#family_support = result['famsup_yes']
	#tutoring = result['paid_yes']
	address = json['address_U']
	higher_education = json['higher_yes']
	internet = json['internet_yes']
	romantic_relationship = json['romantic_yes']
	#Medu = result['Medu']
	#Fedu = result['Fedu']
	failures = json['failures']
	famrel = json['famrel']
	#absences = json['absences']

	X_test = pd.DataFrame({'sex': [sex], 'address': [address], 'higher_education': [higher_education], 'internet': [internet], 'romantic_relationship': [romantic_relationship],'failures': [failures], 'famrel': [famrel]})
	prediction = str(PREDICTOR.predict(X_test)[0])
	score = PREDICTOR.predict_proba(X_test)[0,1]
	
	results = {"score": str(round(score * 100,2)) + "%"}

	#threshold = 0.3
	#prediction2 = str(np.where(score >= threshold, 1, 0))

	return jsonify(result = "Student's chance to fail: " + str(round(score * 100,2)) + "%")
	
	#return jsonify(result="%s %s %s" % (number1,number2,number3))
	

if __name__ == "__main__":
	handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
	handler.setLevel(logging.INFO)
	app.logger.addHandler(handler)
	app.run(host='127.0.0.1',port=5000,debug=True)