import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.title('JGG Data Analysis Simulation')
st.subheader('This is a very quick example of some of tools available for data analysis that could help the airport make sense of its income and to spot trends to plan for the future.')
st.subheader('This example does not even scratch the surface of what is possible, and everything is completley configurable.')
'_Note, I made up all of this data on the spot, so do not expect accurate or realistic values._'
df = pd.read_excel('./JGG_Data_sim (2).xlsx')
st.header('Example excerpt from transaction excel file (interactive)')
df
st.header('Example interactive bar chart from data above')
fig = px.bar(df, x="Date", y="Amount", color='Type', title='$ per day')
st.plotly_chart(fig)
st.header("Example revenue metrics (random values)")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Day", "$275.20", "7.2%")
col2.metric("Week", "$1,780.03", "-10.4%")
col3.metric("Month", "$6,651.76", "4.7%")
col4.metric("YTD", "$17,843.33")
st.header("Example interactive line chart of earnings over a longer period (This chart is just using the Microsoft stock price)")
df1 = px.data.stocks()
fig = px.line(df1, x='date', y="MSFT")
st.plotly_chart(fig)