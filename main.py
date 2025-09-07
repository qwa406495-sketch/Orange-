import streamlit as st

st.title("stress detector app")

#taking users input
name=st.text_input("enter your name")

#display a message when a button is clicked 
if st.button("submit"):
  st.write(f"hlo, {name}! welcome to stress detector app.")
  st.write("please choose the correct options")
  sleep = st.number_input("enter your sleeping hours", min_value=0.0, step=0.1)
  if st.button("percentage of stress"):
    predicted_stress = model.predict([hours])[0]
    st.success(f"predicted stress: {predicted_stress:.2f}")
