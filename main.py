import streamlit as st
import pandas as pd
import numpy as np


st.title('Welcome to Konverge.AI')

header = st.container()
dataset = st.container()
load_dataset = st.container()
Model = st.container()
#model_training = st.beta_container()

@st.cache
def get_data():
	
	sample_data = pd.read_csv('sample_data.csv')
	
	return sample_data

with header:
    st.header('Data Science and Engineering Department')
    st.text('')
    
with dataset:
	st.header('Anomaly detection in a time series data')
	st.text('Here we have taken a time series data')
	sample_data = get_data()
	st.write(sample_data.head())
	st.subheader('Connection hour distribution over time')
	date_connectionhour = pd.DataFrame(sample_data['Connection Hours'])
	st.line_chart(date_connectionhour)

with load_dataset:
	st.markdown('#### You can enter your own data here')
	uploaded_file = st.file_uploader("Choose a file", type={"csv"})
	
	if uploaded_file is not None:
  		uploaded_df = pd.read_csv(uploaded_file)
st.write(uploaded_df.head())
	
with load_dataset:
	total_cost = uploaded_df['Total']
	st.line_chart(total_cost)


	#df1 = uploaded_file
	st.markdown("#### Select x and y variable to plot a line graph")
	x_var = st.selectbox('Select the variable to display on x-axis', options=uploaded_df.columns)

	y_var = st.selectbox('Select the variable to display on y-axis', options=uploaded_df.columns)
# y_val = uploaded_df.loc[uploaded_df.items == y_var['Total']]
# y_val = pd.DataFrame(uploaded_df['y_var'])



with Model:
	st.markdown('### Anomaly Detection Model')
	st.text('The model first check that whether the given time series is stationary or not,and the time series is ')
	data_columns, output = st.columns(2)
	
	#input_feature = data_columns.text_input("Enter the feature in which you want to see Anomaly", 'Connection Hours')
	feature = data_columns.selectbox('In which column you want to see Anomaly in the data', options=sample_data.columns)
