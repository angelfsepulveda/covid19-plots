import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import os
import plotly.express as px
import logging
###### begin logger config
logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('/tmp/covid19_info.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -\n %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
# WHO API LINK
# https://extranet.who.int/xmart-api/odata/NCOV_PHM/CLEAN_PHSM
st.title("003 Covid 2019 Data")
DATA_URL =  "dataset/worldometer_data.csv"
@st.cache
def load_data():
	data = pd.read_csv(DATA_URL)
	logger.debug(data.head())
	return data

#
data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")
#
show_data_bol = st.sidebar.checkbox("Show Raw data")
if show_data_bol:
	st.subheader('Raw data')
	st.write(data)
#
st.subheader('Total of: Cases, Deaths, Recovered, Active Cases')
#
columns = ["TotalCases","TotalDeaths", "TotalRecovered","ActiveCases"]
for x in columns:	
	fig = px.treemap(data.iloc[0:20],path=['Country/Region'],values=x,title="treemap Covid  %s" %x)
	st.plotly_chart(fig)

#
st.subheader('line chart: Cases, Deaths, Recovered, Active Cases')
#
chart_data = pd.DataFrame(
	data.iloc[0:20],
	columns=columns
	)
st.line_chart(chart_data)
#option = st.sidebar.selectbox(
#	'Which country do you love more?',
#	data['Country/Region'])

#'You selected:', option
#show_data_bol = st.sidebar.selectbox('Show raw Data:', ['Yes','No'])
