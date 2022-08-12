
# coding: utf-8

import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf 
from tensorflow import keras
from flask import Flask, request, render_template
import pickle
from keras.models import load_model

app = Flask("__name__")

df_1=pd.read_csv("train_data_evaluation_part_2.csv")

q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")


@app.route("/", methods=['POST'])
def predict():
    
    '''
    Nationality
    Age
    DaysSinceCreation
    AverageLeadTime
    LodgingRevenue
    OtherRevenue
    BookingsCanceled
    BookingsNoShowed
    PersonsNights
    RoomNights
    DaysSinceLastStay
    DaysSinceFirstStay
    DistributionChannel
    MarketSegment
    SRHighFloor
    SRLowFloor
    SRAccessibleRoom
    SRMediumFloor
    SRBathtub
    SRShower
    SRCrib
    SRKingSizeBed
    SRTwinBed
    SRNearElevator
    SRAwayFromElevator
    SRNoAlcoholInMiniBar
    SRQuietRoom
    '''
    

    
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    inputQuery9 = request.form['query9']
    inputQuery10 = request.form['query10']
    inputQuery11 = request.form['query11']
    inputQuery12 = request.form['query12']
    inputQuery13 = request.form['query13']
    inputQuery14 = request.form['query14']
    inputQuery15 = request.form['query15']
    inputQuery16 = request.form['query16']
    inputQuery17 = request.form['query17']
    inputQuery18 = request.form['query18']
    inputQuery19 = request.form['query19']
    inputQuery20 = request.form['query20']
    inputQuery21 = request.form['query21']
    inputQuery22 = request.form['query22']
    inputQuery23 = request.form['query23']
    inputQuery24 = request.form['query24']
    inputQuery25 = request.form['query25']
    inputQuery26 = request.form['query26']
    inputQuery27 = request.form['query27']
    
    
    model = load_model('./model.h5')
    #model = pickle.load(open("D:/CustomerCheckinPrediction/ann_customer_model.pkl", "rb"))
    
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, 
             inputQuery8, inputQuery9, inputQuery10, inputQuery11, inputQuery12, inputQuery13, inputQuery14,
             inputQuery15, inputQuery16, inputQuery17, inputQuery18, inputQuery19, inputQuery20, inputQuery21,
             inputQuery22, inputQuery23, inputQuery24, inputQuery25, inputQuery26, inputQuery27]]
    
    new_df = pd.DataFrame(data, columns = ['Nationality', 'Age', 'DaysSinceCreation', 'AverageLeadTime',
       'LodgingRevenue', 'OtherRevenue', 'BookingsCanceled',
       'BookingsNoShowed', 'PersonsNights', 'RoomNights',
       'DaysSinceLastStay', 'DaysSinceFirstStay', 'DistributionChannel',
       'MarketSegment', 'SRHighFloor', 'SRLowFloor', 'SRAccessibleRoom',
       'SRMediumFloor', 'SRBathtub', 'SRShower', 'SRCrib', 'SRKingSizeBed',
       'SRTwinBed', 'SRNearElevator', 'SRAwayFromElevator',
       'SRNoAlcoholInMiniBar', 'SRQuietRoom'])
    
    df_2 = pd.concat([df_1, new_df], ignore_index = True)  
    
    
    
    
    new_df__dummies = pd.get_dummies(df_2[['Nationality', 'Age', 'DaysSinceCreation', 'AverageLeadTime',
       'LodgingRevenue', 'OtherRevenue', 'BookingsCanceled',
       'BookingsNoShowed', 'PersonsNights', 'RoomNights',
       'DaysSinceLastStay', 'DaysSinceFirstStay', 'DistributionChannel',
       'MarketSegment', 'SRHighFloor', 'SRLowFloor', 'SRAccessibleRoom',
       'SRMediumFloor', 'SRBathtub', 'SRShower', 'SRCrib', 'SRKingSizeBed',
       'SRTwinBed', 'SRNearElevator', 'SRAwayFromElevator',
       'SRNoAlcoholInMiniBar', 'SRQuietRoom']])
    
    
    #final_df=pd.concat([new_df__dummies, new_dummy], axis=1)
        
    
    single = model.predict(new_df__dummies.tail(1))
    probablity = model.predict_proba(new_df__dummies.tail(1))[:,1]
    
    
    
    if single>0.5:
        o1 = "This customer will checkin!!"
        o2 = "Confidence: {}".format(probablity*100)
    else:
        o1 = "This customer will not checkin!!"
        o2 = "Confidence: {}".format(probablity*100)
    

        
    return render_template('home.html', output1=o1, output2=o2, 
                           query1 = request.form['query1'], 
                           query2 = request.form['query2'],
                           query3 = request.form['query3'],
                           query4 = request.form['query4'],
                           query5 = request.form['query5'], 
                           query6 = request.form['query6'], 
                           query7 = request.form['query7'], 
                           query8 = request.form['query8'], 
                           query9 = request.form['query9'], 
                           query10 = request.form['query10'], 
                           query11 = request.form['query11'], 
                           query12 = request.form['query12'], 
                           query13 = request.form['query13'], 
                           query14 = request.form['query14'], 
                           query15 = request.form['query15'], 
                           query16 = request.form['query16'], 
                           query17 = request.form['query17'],
                           query18 = request.form['query18'], 
                           query19 = request.form['query19'],
                           query20 = request.form['query20'],
                           query21 = request.form['query21'],
                           query22 = request.form['query22'],
                           query23 = request.form['query23'],
                           query24 = request.form['query24'],
                           query25 = request.form['query25'],
                           query26 = request.form['query26'],
                           query27 = request.form['query27']
                           )


    
app.run()

