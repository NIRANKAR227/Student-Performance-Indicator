from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)
app=application

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == 'GET':
        return render_template('home.html')

    else:
        data=CustomData(
            gender = request.form.get('gender') or "",
            race_ethnicity = request.form.get('ethnicity') or "",
            parental_level_of_education = request.form.get('parental_level_of_education') or "",
            lunch = request.form.get('lunch') or "",
            test_preparation_course= request.form.get('test_preparation_course') or "",

            reading_score= int(request.form.get('reading score') or 0),
            writing_score= int(request.form.get('writing score') or 0)
        )

        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        Predict_Pipeline=PredictPipeline()
        print("Mid prediction")
        results=Predict_Pipeline.Predict(pred_df)
        print("After Prediction")
        return render_template('home.html',results=results[0])

if __name__ == "__main__":
    app.run(debug=True)