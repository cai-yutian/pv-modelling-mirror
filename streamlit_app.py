import streamlit as st 
import pandas as pd 
from darts import TimeSeries
from darts.models import FFT
import altair as alt 
import requests

# Loading the required information and trained models
model = FFT.load("models/fft.pkl")

# Widgets for User Inputs 
pv_sys_tab, solar_irr_tab = st.tabs(["PV System Info 📝", 
                                     "Prediction Timeline☀️"])

with pv_sys_tab:
    st.subheader("Please enter your PV system information.")
    system_power = st.number_input("Total System Power (W)", min_value=200)

with solar_irr_tab:
    st.subheader("Please choose the number of years that you want to predict your PV ")
    years_to_predict = st.slider("Number of years to predict", 1, 30, 5)

prediction = model.predict(n=12*4*(years_to_predict+3))
plot = prediction.plot(label="forecast", low_quantile=0.05, high_quantile=0.95)
st.pyplot(plot)

# Results View 
st.subheader("")
st.subheader("")
st.subheader("Results")
st.subheader("")
st.write("System Power (W): ", system_power)
st.write("Years to predict: ", years_to_predict)

