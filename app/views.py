from app import app

@app.route("/")
def index():
    return "Homepage"

@app.route("/patients")
def list_of_patients():
    return "List of patients"

@app.route("/patient")
def individual_patient():
    return "Individual patient"