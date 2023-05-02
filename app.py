from flask import Flask, render_template, request,jsonify, url_for
import os
import pickle
import plotly.express as px
import pandas as pd
import numpy as np



picfolder = os.path.join("static","images")

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
app.config["UPLOAD_FOLDER"] = picfolder

@app.route("/")
def home():

    return render_template("homepage.html")







@app.route('/visulisation')
def visulisation():
    df = pd.read_csv("DryBeanDataset/crop_yield_data.csv")
    # Create your Plotly Express visualization
    fig = px.bar(df, x='Year', y='Export Quantity')

    # Convert the figure to JSON
    graphJSON = fig.to_json()

    fig2 = px.bar(df, x='Yield', y='Crop')
    graphJSON2 = fig2.to_json()


    # Render the HTML template with the graphJSON
    return render_template('visulisation.html', graphJSON=graphJSON, graphJSON2=graphJSON2)

@app.route("/predict", methods = ['GET','POST'])
def mypredict():
    if request.method == 'POST':
        myTemperature = int(request.form.get("Temperature", False))
        myPrecipitation	= int(request.form.get("Precipitation", False))
        myExport	= int(request.form.get("Export", False))
        myFertilizer = int(request.form.get("Fertilizer", False))	
        myAvocados = int(request.form.get("Crop_Avocados", False))	
        myBananas = int(request.form.get("Crop_Bananas", False))	
        myRice	 = int(request.form.get("Crop_Rice", False)) 	
        myWheat	= int(request.form.get("Crop_Wheat", False))

        print([myTemperature,myPrecipitation,myExport,myFertilizer,myAvocados,myBananas,myRice,myWheat ])
        myfin = np.array([[myTemperature,myPrecipitation,myExport,myFertilizer,myAvocados,myBananas,myRice,myWheat ]])
        prediction = model.predict(myfin)
        if prediction[0]:
                my = prediction[0]
        else:
            my = " "

        return render_template("predict.html", my_ourbeans=f"{prediction[0]}")

    else:
        return render_template("predict.html", my_ourbeans=f" ")
         
         


if  __name__ == "__main__":
    app.run(debug=True)     