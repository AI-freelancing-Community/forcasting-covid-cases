# -*- coding: utf-8 -*-
"""
Created on Sat oct 3 18:20:31 2020

@author: Nitin Faye
"""

# -*- coding: utf-8 -*-
"""
Created on sun oct 04 19:50:04 2020

@author: nitin Faye
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
import os
from PIL import Image

#app=Flask(__name__)
#Swagger(app)
pickle_in = open("model_scores.p","rb")
classifire = pickle.load(pickle_in)
#model 
Model_List=['LINEAR REGRASSION', 'RANDOM FOREST','LSTM','ARIMA','PROPHET','HOLT-WINTER']
#cases
Cases_List=['Confiremd', 'Deaths', 'Recovered']

#@app.route('/')
def welcome():
    return "Welcome All"
	
def user_input_features():

    st.sidebar.header('User Input Values')

    From_Date = st.sidebar.slider('From Date March', 1  , 31, 10)
    To_Date = st.sidebar.slider('To Date May', 1 , 31, 10)
	
	   ##st.sidebar.add_rows

    Country = st.sidebar.text_input('Please inter Country',)

       ##st.sidebar.add_rows

    Model = st.sidebar.selectbox('Select Model',Model_List)
	
	    ##st.sidebar.add_rows 
		
	


    data = {'From_Date': From_Date,	
            'To_Date': To_Date,	
            'Country': Country,
			'Model':  Model}
    features = pd.DataFrame(data, index=[0])
    return features
		
    
df = user_input_features()

st.subheader('User Entered parameters for confirmed cases, Deaths cases and Recovred cases is')

st.write(df)

	
def main():
	st.title("Covid Analysis App")
	#show the entire dataset
	st.checkbox("Show All Dataset")
	st.write('hi1!!!:welcome')
	 
	st.text("Built with Streamlit")
	
if __name__=='__main__':
    main()
    
    
    
