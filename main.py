import streamlit as st
import panda as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import logisticregression
from sklearn.metrics import accuracy_score, classification_report

# load the dataset
data = pd.read_csv('stressdetector.csv')

st.title("stress detector app")

#taking users input
name=st.text_input("enter your name")

#display a message when a button is clicked 
if st.button("submit"):
  st.write(f"hlo, {name}! welcome to stress detector app.")
  st.write(f"please choose the correct option")
