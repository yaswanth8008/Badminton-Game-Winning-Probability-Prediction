import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask('game_winning_probability')
model = pickle.load(open('RandomForest_model.pkl', 'rb'))


@app.route('/')
def Home():
    return render_template('index.html')


@app.route('/',methods = ['POST'])
def predict():
  
     if request.method == 'POST':

        Service_Errors = request.form['ServiceErrorsBox']
        Net_Errors = request.form['NetErrorsBox']
        Away = request.form['AwayBox']
        Smash_Errors = request.form['SmashErrorsBox']
        WaterDrankInLiters = request.form['WaterDrankBox']
        Meditated = request.form['MeditationBox']
        
        if(Meditated == 'Yes'):
                Meditated = 1
        else:
                Meditated = 0

        Diet = request.form['DietBox']
        if(Diet == 'Light'):
            Diet_Light = 1
            Diet_Moderate = 0
        elif(Diet == 'Moderate'):
            Diet_Light = 0
            Diet_Moderate = 1
        else:
            Diet_Light = 0
            Diet_Moderate = 0

        prediction = model.predict_proba([[Service_Errors,Net_Errors,Away,Smash_Errors,WaterDrankInLiters,Meditated,Diet_Light,Diet_Moderate]])
        prob_winning = prediction[0][1]

      
        return f'The Probability of winning the game is {prob_winning}'

if __name__ == "__main__":
    app.run(debug=True)



