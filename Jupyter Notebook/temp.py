import numpy as np
import pickle
import streamlit as st
import pandas as pd
from sklearn.svm import SVC
import matplotlib.pyplot as plt


# loading the saved model
dataset = pickle.load(open('trained_model.sav', 'rb'))

# creating a function for Prediction
st.set_page_config(
    page_title="DiabPred"
)
st.title('Data Visualizer')

def main():
    
       st.title('Diabetes Prediction')

       # getting the input data from the user
       col1, col2, col3 = st.columns(3)

       with col1:
           Pregnancies = st.text_input('Pregnancies')

       with col2:
           Glucose = st.text_input('Glucose')

       with col3:
           BloodPressure = st.text_input('BloodPressure (mmHg)')

       with col1:
           SkinThickness = st.text_input('SkinThickness (mm)')

       with col2:
           Insulin = st.text_input('Insulin')

       with col3:
           BMI = st.text_input('BMI')

       with col1:
           Age = st.text_input('Age')

       # code for Prediction
       diab_diagnosis = ''

       # creating a button for Prediction
       if st.button('Diabetes Test Result'):
           diab_prediction = dataset.predict([[Pregnancies, Glucose, BloodPressure,SkinThickness,Insulin, BMI,Age]])

           if diab_prediction[0] == 1:
               diab_diagnosis = 'The person is prone to diabetes.'
           else:
               diab_diagnosis = 'The person is not prone to diabetes.'
       st.success(diab_diagnosis)
    




if __name__ == '__main__':
    main()