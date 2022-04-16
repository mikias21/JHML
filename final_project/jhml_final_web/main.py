import pandas as pd 
from joblib import load
from flask import Flask, render_template, request
from model.model import make_prediction

app = Flask(__name__)

work_type = {
    'SELFEMP': 'Self-employed',
    'CHILD': 'children',
    'GOV': 'Govt_job',
    'PRI': 'Private',
    'NEVWOR': 'Never_worked'
}
residance_type = {
    'RURAL': 'Rural',
    'URBAN': 'Urban'
}
smoking_status = {
    'NEVERSOMKED': 'never smoked',
    'UNKNOWN': 'Unknown',
    'USEDTOSMOKE': 'formerly smoked',
    'SMOKING': 'smokes'
}


@app.route('/')
def load_index():
    return render_template('index.html')

@app.route('/acceptForm', methods=['POST'])
def accept_form():
    if request.form:
        age = request.form['age']
        gender = request.form['gender']
        hypertension_val = request.form['hypertension_val']
        heart_val = request.form['heart_val']
        marriage = request.form['marriage']
        worktype = work_type[request.form['worktype']]
        residance = residance_type[request.form['residance']]
        glucose = request.form['glucose']
        bmi = request.form['bmi']
        smoking = smoking_status[request.form['smoking']]

        # Create simple Pandas dataframe 
        data = [[gender, age, hypertension_val, heart_val, marriage, worktype, residance, glucose, bmi, smoking]]
        data_frame = pd.DataFrame(data, 
                            columns=['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 
                            'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status'])

        # Load compiled model 
        prediction = make_prediction(data_frame)
        # print(age, gender, hypertension_val, heart_val, marriage, worktype, residance, glucose, bmi, smoking)
        return str(int(prediction[0]))


if __name__ == '__main__':
    app.debug = True 
    app.run()
