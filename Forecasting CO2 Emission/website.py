# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 14:55:58 2022

@author: Admin
"""

import pandas as pd
import streamlit as st
import numpy as np
import pickle
import seaborn as sns
import matplotlib
matplotlib.use( 'tkagg' )
import matplotlib.pyplot as plt
from pandas.tseries.offsets import DateOffset
import warnings
warnings.filterwarnings("ignore")

st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )


header_container = st.container()
stats_container = st.container()	


st.title("Co2 Levels Forecasting")
st.header("Welcome!")

st.write("IMPORT DATA CO2 dataset.csv")

data = st.file_uploader('',type='csv')


fm = pickle.load(open("C:/Users/Admin/Desktop/Group 6 Project/Co2_Forecasting.pkl", 'rb'))
#st.write("IMPORT DATA")
#st.write("CO2 dataset.csv")


if data is not None:
    dateparse = lambda x: pd.to_datetime(x, format='%Y', errors = 'coerce')
    appdata = pd.read_csv(data, parse_dates=['Year'], index_col='Year', date_parser=dateparse) 
    
    st.write(data)
    

st.write("SELECT FORECAST PERIOD")

periods_input = st.number_input('How many years forecast do you want?',
min_value = 1, max_value = 200)

if data is not None:
    filename= 'Co2_Forecasting.pkl'
    

if data is not None:
    future=[appdata.index[-1]+ DateOffset(years=x)for x in range(0,periods_input)]
    future=pd.DataFrame(index=future[1:],columns=appdata.columns)
    end = len(appdata)+len(future)
    fcst = fm.predict(start = 215, end = end , dynamic= True)
    st.write("Below are the forecasted values")
    fcst
    st.write("VISUALIZE FORECASTED DATA")

    plt.plot(appdata, label='Previous years')
    plt.plot(fcst, label='forecast')
    plt.title('Forecast')
    plt.legend(loc='upper left', fontsize=8)
    plt.show()