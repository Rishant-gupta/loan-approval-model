# Importing necessary files:
import streamlit as st
import pandas as pd
import pickle

# Loading model and model columns
with open("models.pkl", "rb") as f:
    model = pickle.load(f)

with open("model_column.pkl", "rb") as f:
    model_column = pickle.load(f)

# Initiating interface formation
st.title("Loan Approval Prediction App")
st.write("Fill the details below to check if your loan might be approved or not.")

# Making the variables to take input from user
Name = st.text_input("Name")
Gender = st.selectbox('Gender', ['Male', 'Female'])
Married = st.selectbox('Married', ['Yes', 'No'])
Dependents = st.selectbox('Dependent', ['0', '1','2','3+'])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
ApplicantIncome = st.number_input("Applicant Income", min_value=0)
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
LoanAmount = st.number_input("Loan Amount (in thousands)", min_value=0)
Loan_Amount_Term = st.number_input("Loan Amount Term (in months)", min_value=0)
Credit_History = st.selectbox("Credit History", [1.0, 0.0])
Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Creating dataframe to train model
input_data = pd.DataFrame({
    'Name': [Name],
    'Gender': [Gender],
    'Married': [Married],
    'Dependents': [Dependents],
    'Education': [Education],
    'Self_Employed': [Self_Employed],
    'ApplicantIncome': [ApplicantIncome],
    'CoapplicantIncome': [CoapplicantIncome],
    'LoanAmount': [LoanAmount],
    'Loan_Amount_Term': [Loan_Amount_Term],
    'Credit_History': [Credit_History],
    'Property_Area': [Property_Area]
})

# Clearing the data
input_data = input_data.drop(columns=['Name','Gender'])

# Encoding the data
ohe_columns = (columns for columns in input_data if input_data[columns].dtypes== 'object')
input_data = pd.get_dummies(input_data, columns=ohe_columns , drop_first=True)

# Align columns to match model training data columns
model_columns = pickle.load(open("model_column.pkl", "rb"))
input_data = input_data.reindex(columns=model_columns, fill_value=0)

# Prediction
if st.button("Predict Loan Approval"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Not Approved")


