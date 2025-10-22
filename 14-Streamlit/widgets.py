
import streamlit as st
import pandas as pd
st.title("Streamlit text input")

name=st.text_input("Enter your Name:")


age=st.slider("Select your age:",0,100,25)

st.write(f"Your age is {age}, ")

options = ["Python ","JAva","C++","JavaScript"]
choice=st.selectbox("Choose your favourite language:", options)
st.write(f"You Selected {choice}.")

if name:
    st.write(f"HEllo, {name}")
    

data = {
    "Name":["John", "Jane", "jake", "JIll"],
    "Age":[28, 24, 35, 40],
    "City":["Nashik","patna","munger","nalasopara"]
}    

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)