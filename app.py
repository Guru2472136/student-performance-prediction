import streamlit as st 
import joblib 
import numpy as np 
# Load model 
model = joblib.load("gpa_model_original.pkl") 
st.set_page_config(page_title="Student GPA Predictor", layout="centered") 
st.title("Student GPA Predictor") 
# Mapping dictionaries 
ethnicity_map = { 
"Group A": 0, 
"Group B": 1, 
"Group C": 2, 
"Group D": 3, 
"Group E": 4 
} 
 
parent_edu_map = { 
    "Some High School": 0, 
    "High School": 1, 
    "Some College": 2, 
    "Associate's": 3, 
    "Bachelor's": 4, 
    "Master's": 5 
} 
 
yes_no_map = { 
    "No": 0, 
    "Yes": 1 
} 
 
# Input Fields 
age = st.slider("Age", 10, 25, 17) 
 
gender = st.selectbox("Gender", ["Male", "Female"]) 
gender_val = 1 if gender == "Male" else 0 
 
ethnicity = st.selectbox("Ethnicity", list(ethnicity_map.keys())) 
ethnicity_val = ethnicity_map[ethnicity] 
 
parent_edu = st.selectbox("Parental Education", list(parent_edu_map.keys())) 
parent_edu_val = parent_edu_map[parent_edu] 
 
study_time = st.number_input("Study Time Weekly (in hours)", 0.0, 50.0, 10.0) 
absences = st.number_input("Number of Absences", 0, 100, 4) 
tutoring = st.selectbox("Tutoring", list(yes_no_map.keys())) 
tutoring_val = yes_no_map[tutoring] 
support = st.selectbox("Parental Support", ["Low", "Moderate", "Strong", "Very Strong"]) 
support_val = ["Low", "Moderate", "Strong", "Very Strong"].index(support) 
extracurricular = st.selectbox("Extracurricular Activities", list(yes_no_map.keys())) 
extra_val = yes_no_map[extracurricular] 
sports = st.selectbox("Sports", list(yes_no_map.keys())) 
sports_val = yes_no_map[sports] 
music = st.selectbox("Music", list(yes_no_map.keys())) 
music_val = yes_no_map[music] 
volunteering = st.selectbox("Volunteering", list(yes_no_map.keys())) 
volunteer_val = yes_no_map[volunteering] 
# Combine features 
input_data = np.array([[age, gender_val, ethnicity_val, parent_edu_val, study_time, 
absences, tutoring_val, support_val, extra_val, sports_val, music_val, volunteer_val]]) 
# Predict 
if st.button("Predict GPA"):
    prediction = model.predict(input_data) 
st.success(f"Predicted GPA: {prediction[0]:.2f}")