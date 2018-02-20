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


X = students[['famsup_yes','higher_yes','romantic_yes']]
y = students['G3']

PREDICTOR = LogisticRegression().fit(X,y)

def predictmodel(famsup, higher, romantic):

    X_test = pd.DataFrame({'famsup': [famsup], 'higher': [higher], 'romantic': [romantic]})

    print (X_test)
    score = PREDICTOR.predict_proba(X_test)[0,1]
    prediction = PREDICTOR.predict(X_test)

    return(score)

print (predictmodel(0, 0, 1))
