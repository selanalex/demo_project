import streamlit as st

name= st.text_input("Enter your name")

st.title("take the input name")
if st.buttom("Submit Name"):
  st.write(f"print the name : {name}")
