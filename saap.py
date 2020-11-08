import streamlit as st

import pandas as pd

# from sklearn import datasets

# from sklearn.ensemble import RandomForestClassifier

Model_List=['LINEAR REGRASSION', 'RANDOM FOREST','LSTM','ARIMA','PROPHET','HOLT-WINTER']


st.write("""

 # Covid Analysis!

""")



st.sidebar.header('User Input Values')



def user_input_features():

    From_Date = st.sidebar.slider('From Date', 1 , 31, 10)
    To_Date = st.sidebar.slider('To Date', 1 , 31, 10)
	
	   ##st.sidebar.add_rows

    Country = st.sidebar.text_input('Please input Country',)

       ##st.sidebar.add_rows

    Model = st.sidebar.selectbox('Select Model',Model_List)

    data = {'From_Date': From_Date,	
            'To_Date': To_Date,	
            'Country': Country,
			'Model':  Model}
    features = pd.DataFrame(data, index=[0])
    return features
		
    
df = user_input_features()

st.subheader('User Entered parameters for confirmed cases, Deaths cases and recovred cases is')

st.write(df)


# Compound Interest function
def compound_int(From_Date,to_Date,Country,Model):

    comp=1.0
    for i in range(0, int(confirmed)):
        comp=comp*(1+Int_Rate/100)
        #st.write(comp)
    comp=float(Country)*(comp-1)
    comp_text= str("Compound Interest is " + str("%.3f" % comp) )
    st.write(comp_text)
    data_1 = {'Computed_Compound_Interest': comp_text}

    result = pd.DataFrame(data_1, index=[0])

    return result






st.subheader('The calculated compound interest is')

#st.write(result)
df_1=compound_int(df.Principal, df.Int_Rate, df.No_Of_Years)


st.subheader('This is print of data frame')

st.write(df_1)
