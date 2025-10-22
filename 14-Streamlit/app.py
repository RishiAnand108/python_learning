import streamlit as st
import numpy as np
import pandas as pd

## Title of the Application
st.title("Hello Streamlit")

## Display a Simple Text
st.write("this is  a simple web page")

## create  a  simple dataframe

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20, 30, 40]
})


##Display the Dataframe
st.write("here is the dataframe")
st.write(df)


##create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)