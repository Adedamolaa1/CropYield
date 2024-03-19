import streamlit as st
import pandas as pd 
import numpy as np 
import joblib 
import warnings 
warnings.filterwarnings('ignore')

#import data
data = pd.read_excel('crop yield data sheet.xlsx', engine='openpyxl')

data['Temperatue'] = pd.to_numeric(data['Temperatue'], errors = 'coerce')
for i in data.columns:
    if data[i].isnull().sum() / len(data)< 30:
        if i in data.columns:
            data[i].fillna(data[i].median(), inplace = True)
    else:
        data.drop(i, axis = 1, inplace = True)


#import model
model = joblib.load('cropModel.pkl')

st.markdown('<h1 style = "color: #1F4172; text-align:center; font-family:helvetica">CROP YIELD PREDICTION PROJECT</h1>', unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #F11A7B; text-align: center; font-family: cursive '>Built By ADEYEKUN</h4>", unsafe_allow_html = True)
st.image('pngwing.com (15).png', width = 350, use_column_width = True)
st.markdown('<br>', unsafe_allow_html = True)
st.markdown('<h4 style = "text-align: center; font-family: cursive; font-size; 40px; "> PROJECT OVERVIEW </h4>', unsafe_allow_html = True)
st.markdown("<p>A crop prediction model using linear regression leverages historical data on factors such as weather conditions, soil quality, and agricultural practices to forecast crop yields. By analyzing these variables, linear regression algorithms can identify patterns and relationships that enable accurate predictions of future crop yields. This predictive model helps farmers make informed decisions about planting strategies, resource allocation, and crop management practices, ultimately optimizing agricultural productivity and ensuring food security.</p>", unsafe_allow_html = True)
st.sidebar.image('pngwing.com (16).png', caption = 'welcome user')
st.dataframe(data, use_container_width = True)

input_choice = st.sidebar.radio('Choose your input type', ['Slider Input', 'Number Input'])

if input_choice == 'Slider Input':
    Rainfalls = st.sidebar.slider('Rainfall', data['Rain Fall (mm)'].min(), data['Rain Fall (mm)'].max())
    Fertilizers = st.sidebar.slider('Fertilizer', data['Fertilizer'].min(), data['Fertilizer'].max())
    Temperature = st.sidebar.slider('Temperature', data['Temperatue'].min(), data['Temperatue'].max())
    Nitrogen = st.sidebar.slider('Nitrogen', data['Nitrogen (N)'].min(), data['Nitrogen (N)'].max())
    Phosphorus = st.sidebar.slider('Phosphorus', data['Phosphorus (P)'].min(), data['Phosphorus (P)'].max())
    Potassium = st.sidebar.slider('Potassium', data['Potassium (K)'].min(), data['Potassium (K)'].max())

else:
    Rainfalls = st.sidebar.number_input('Rainfall', data['Rain Fall (mm)'].min(), data['Rain Fall (mm)'].max())
    Fertilizers = st.sidebar.number_input('Fertilizer', data['Fertilizer'].min(), data['Fertilizer'].max())
    Temperature = st.sidebar.number_input('Temperature', data['Temperatue'].min(), data['Temperatue'].max())
    Nitrogen = st.sidebar.number_input('Nitrogen', data['Nitrogen (N)'].min(), data['Nitrogen (N)'].max())
    Phosphorus = st.sidebar.number_input('Phosphorus', data['Phosphorus (P)'].min(), data['Phosphorus (P)'].max())
    Potassium = st.sidebar.number_input('Potassium', data['Potassium (K)'].min(), data['Potassium (K)'].max())

input_var = pd.DataFrame({'RainFall': [Rainfalls], 'Fertilizer': [Fertilizers], 
                          'Temperatue': [Temperature], 'Nitrogen (N)': [Nitrogen],
                          'Phosphorus': [Phosphorus], 'Potassium (K)': [Potassium]})

st.markdown("<br>", unsafe_allow_html = True)
st.markdown("<h4 style = 'text-align: center;; color: olive; font-family: helvetica'>User Input Variables</h4>", unsafe_allow_html = True)
st.dataframe(input_var)

predicted = model.predict(input_var)

prediction, interprete = st.tabs( ['Model prediction', 'Model evaluation'])

with prediction:
    outcome = st.button('Tap to predict')
    if outcome:
        st.success(f'The predicted yield is {predicted}')

with interprete:
    st.header('The interpretation of the Model')
    st.write(f'The intercept of the model is {(model.intercept_)}')
    st.write(f'A unit change in the rainfall causes the yield to change by {model.coef_[0]} acre')
    st.write(f'A unit change in the fertilizer causes the yield to change by {model.coef_[1]} acre')
    st.write(f'A unit change in the Temperature causes the yield to change by {model.coef_[2]} acre')
    st.write(f'A unit change in the Nitrogen causes the yield to change by {model.coef_[3]} acre')
    st.write(f'A unit change in the Phosphorus causes the yield to change by {model.coef_[4]} acre')




