# main.py
import random
from datetime import datetime
from db_config import get_db_connection

# Establish a database connection
conn = get_db_connection()
cursor = conn.cursor()

# Drop existing tables if they exist
cursor.execute('DROP TABLE IF EXISTS table1 CASCADE')
cursor.execute('DROP TABLE IF EXISTS table2 CASCADE')

# Create Table 2
cursor.execute('''
CREATE TABLE IF NOT EXISTS table2 (
    pact_id SERIAL PRIMARY KEY,
    patient_name TEXT,
    patient_number INTEGER,
    datetime TIMESTAMP,
    gender TEXT,
    age INTEGER,
    department TEXT
)
''')

# Create Table 1
cursor.execute('''
CREATE TABLE IF NOT EXISTS table1 (
    pact_id INTEGER PRIMARY KEY,
    present_illness TEXT,
    medical_history TEXT,
    symptom1 BOOLEAN,
    symptom2 BOOLEAN,
    symptom3 BOOLEAN,
    symptom4 BOOLEAN,
    symptom5 BOOLEAN,
    symptom6 BOOLEAN,
    symptom7 BOOLEAN,
    symptom8 BOOLEAN,
    symptom9 BOOLEAN,
    symptom10 BOOLEAN,
    vital_sign1 REAL,
    vital_sign2 REAL,
    vital_sign3 REAL,
    vital_sign4 REAL,
    vital_sign5 REAL,
    vital_sign6 REAL,
    vital_sign7 REAL,
    vital_sign8 REAL,
    vital_sign9 REAL,
    pain_assessment_pain TEXT,
    pain_assessment_category TEXT,
    pain_assessment_age TEXT,
    pain_assessment_tool TEXT,
    care_plan TEXT,
    FOREIGN KEY(pact_id) REFERENCES table2(pact_id)
)
''')

# Commit the changes
conn.commit()

# Function to generate random boolean values
def random_boolean():
    return bool(random.getrandbits(1))

# Function to generate random vital signs
def random_vital_sign():
    return round(random.uniform(60, 120), 2)

# Sample data for 10 cases
patients = [
    {
        'patient_name': 'Patient{}'.format(i),
        'patient_number': random.randint(1000, 9999),
        'datetime': datetime.now(),
        'gender': random.choice(['M', 'F']),
        'age': random.randint(1, 90),
        'department': random.choice(['Cardiology', 'Neurology', 'Orthopedics'])
    } for i in range(10)
]

# Insert sample data into Table 2 and retrieve generated pact_id
for patient in patients:
    cursor.execute('''
    INSERT INTO table2 (patient_name, patient_number, datetime, gender, age, department)
    VALUES (%(patient_name)s, %(patient_number)s, %(datetime)s, %(gender)s, %(age)s, %(department)s) RETURNING pact_id
    ''', patient)
    pact_id = cursor.fetchone()[0]

    # Insert corresponding data into Table 1
    cursor.execute('''
    INSERT INTO table1 (pact_id, present_illness, medical_history, symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8, symptom9, symptom10,
    vital_sign1, vital_sign2, vital_sign3, vital_sign4, vital_sign5, vital_sign6, vital_sign7, vital_sign8, vital_sign9, pain_assessment_pain, pain_assessment_category, pain_assessment_age, pain_assessment_tool, care_plan)
    VALUES (%(pact_id)s, %(present_illness)s, %(medical_history)s, %(symptom1)s, %(symptom2)s, %(symptom3)s, %(symptom4)s, %(symptom5)s, %(symptom6)s, %(symptom7)s, %(symptom8)s, %(symptom9)s, %(symptom10)s,
    %(vital_sign1)s, %(vital_sign2)s, %(vital_sign3)s, %(vital_sign4)s, %(vital_sign5)s, %(vital_sign6)s, %(vital_sign7)s, %(vital_sign8)s, %(vital_sign9)s, %(pain_assessment_pain)s, %(pain_assessment_category)s, %(pain_assessment_age)s, %(pain_assessment_tool)s, %(care_plan)s)
    ''', {
        'pact_id': pact_id,
        'present_illness': 'Illness {}'.format(pact_id),
        'medical_history': 'History {}'.format(pact_id),
        'symptom1': random_boolean(),
        'symptom2': random_boolean(),
        'symptom3': random_boolean(),
        'symptom4': random_boolean(),
        'symptom5': random_boolean(),
        'symptom6': random_boolean(),
        'symptom7': random_boolean(),
        'symptom8': random_boolean(),
        'symptom9': random_boolean(),
        'symptom10': random_boolean(),
        'vital_sign1': random_vital_sign(),
        'vital_sign2': random_vital_sign(),
        'vital_sign3': random_vital_sign(),
        'vital_sign4': random_vital_sign(),
        'vital_sign5': random_vital_sign(),
        'vital_sign6': random_vital_sign(),
        'vital_sign7': random_vital_sign(),
        'vital_sign8': random_vital_sign(),
        'vital_sign9': random_vital_sign(),
        'pain_assessment_pain': random.choice(['Yes', 'No', 'Unknown']),
        'pain_assessment_category': random.choice(['General', 'Critical']),
        'pain_assessment_age': random.choice(['Newborn', '0-6 years', '7-12 years', '13+ years']),
        'pain_assessment_tool': random.choice(['Tool1', 'Tool2']),
        'care_plan': 'Care Plan {}'.format(pact_id)
    })

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully with sample data.")