from flask import Flask
from flask import request
from flask import render_template
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
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

#X = students[['sex_M','famsup_yes','higher_yes', 'romantic_yes','Medu', 'Fedu', 'famrel', 'failures','absences']]
#X = students[['sex_M','famsup_yes','paid_yes','higher_yes', 'romantic_yes','Medu', 'Fedu', 'failures','absences']]
X = students[['sex_M','address_U','higher_yes', 'internet_yes','romantic_yes','failures','absences']]
y = students['G3']

#PREDICTOR = LogisticRegression().fit(X,y)
PREDICTOR = RandomForestClassifier(max_depth=15, n_estimators=18, n_jobs = -1,random_state =50).fit(X,y)


X_test = pd.DataFrame({'sex': [sex], 'address': [address], 'higher_education': [higher_education], 'internet': [internet], 'romantic_relationship': [romantic_relationship],'failures': [failures], 'absences': [absences]})

score = PREDICTOR.predict_proba(X_test)[0,1]

score_perc = str(round(score * 100,2)) + "%"
prediction = str(PREDICTOR.predict(X_test)[0])


threshold = 0.3
prediction2 = str(np.where(score >= threshold, 1, 0))


def muffin_or_cupcake(flour_cups_float, milk_cups_float, sugar_cups_float,
                        butter_cups_float, eggs_num_float, bp_tsp_float,
                        vanilla_tsp_float, salt_tsp_float, mc_model=mc_model):
    
    total = 16 * flour_cups_float + \
            16 * milk_cups_float + \
            16 * sugar_cups_float + \
            16 * butter_cups_float + \
            3 * eggs_num_float + \
            .33 * bp_tsp_float + \
            .33 * vanilla_tsp_float + \
            .33 * salt_tsp_float

    flour_cups_prop = 16 * flour_cups_float * 100.0 / total
    milk_cups_prop = 16 * milk_cups_float * 100.0 / total
    sugar_cups_prop = 16 * sugar_cups_float * 100.0 / total
    butter_cups_prop = 16 * butter_cups_float * 100.0 / total
    eggs_num_prop = 3 * eggs_num_float * 100.0 / total
    bp_tsp_prop = .33 * bp_tsp_float * 100.0 / total
    vanilla_tsp_prop = .33 * vanilla_tsp_float * 100.0 / total
    salt_tsp_prop = .33 * salt_tsp_float * 100.0 / total

    input_df = pd.DataFrame({'Flour': flour_cups_prop,
                             'Sugar': sugar_cups_prop}, index=[0])
                             #'Milk': milk_cups_prop,
                             #'Butter': butter_cups_prop,
                             #'Eggs': eggs_num_prop,
                             #'Baking Powder': bp_tsp_prop,
                             #'Vanilla': vanilla_tsp_prop
                             #'Salt': salt_tsp_prop

    prediction = mc_model.predict(input_df)[0]


    

    message_array = ["You have a muffin!",
                     "You have a cupcake!"]

    return message_array[prediction]