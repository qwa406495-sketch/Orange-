import streamlit as st

st.title("stress detector app")

#taking users input
name=st.text_input("enter your name")

#display a message when a button is clicked 
if st.button("submit"):
  st.write(f"hlo, {name}! welcome to stress detector app.
  please enter your data")
  
