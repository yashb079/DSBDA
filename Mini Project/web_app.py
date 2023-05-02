import pandas as pd
from flask import Flask, render_template

df = pd.read_csv('covid_vaccine_statewise.csv')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/first_dose')
def first_dose():
    first_dose = df.groupby('State')['First Dose Administered'].sum()
    return render_template('first_dose.html', first_dose=first_dose)

@app.route('/second_dose')
def second_dose():
    second_dose = df.groupby('State')['Second Dose Administered'].sum()
    return render_template('second_dose.html', second_dose=second_dose)

@app.route('/males_vaccinated')
def males_vaccinated():
    males_vaccinated = df.groupby('State')['Male'].sum()
    return render_template('males_vaccinated.html', males_vaccinated=males_vaccinated)

@app.route('/females_vaccinated')
def females_vaccinated():
    females_vaccinated = df.groupby('State')['Female'].sum()
    return render_template('females_vaccinated.html', females_vaccinated=females_vaccinated)

if __name__ == '__main__':
    app.run(debug=True)
