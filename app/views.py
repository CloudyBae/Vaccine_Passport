from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/patients")
def list_of_patients():
    return "List of patients"

@app.route("/patient")
def individual_patient():
    return "Individual patient"