from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd


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


X = students[['famsup_yes','higher_yes']]
y = students['G3']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

PREDICTOR = LogisticRegression().fit(X_train,y_train)
score = PREDICTOR.predict_proba(X_test)
prediction = PREDICTOR.predict(X_test)

print(score)
print(prediction)