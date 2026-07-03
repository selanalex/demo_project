import streamlit as st

name= st.text_input("Enter your name")

st.title("take the input name")
if st.button("Submit Name"):
  st.write(f"print the name : {name}")
