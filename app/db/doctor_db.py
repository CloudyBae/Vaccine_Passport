import sqlite3 as db
import os

def register_doctor(input_dict):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SQLPATH = os.path.join(BASE_DIR, "vaccine_passport.db")
    
    conn = db.connect(SQLPATH)
    conn.execute("INSERT INTO DOCTORS (NAME, GOVERNMENT_ID, EMAIL_ADDRESS, PHONE_NUMBER, PASSWORD) \
        VALUES (?, ?, ?, ?, ?)", (input_dict['name'], input_dict['government-id'], input_dict['email-address'], input_dict['phone-number'], input_dict['password']))
    
    conn.commit()
    conn.close()

