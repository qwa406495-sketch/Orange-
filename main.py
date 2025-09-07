import streamlit as st

st.title("stress detector app")

#taking users input
name=st.text_input("enter your name")

#display a message when a button is clicked 
if st.button("submit"):
  st.write(f"hlo, {name}! welcome to stress detector app.")
  st.write("please choose the correct options")
  sleep = st.number_input("enter your sleeping hours", min_value=0.0, max_value=24.0, value=7.0)
  work = st.number_input("Work Hours (today)", min_value=0, max_value=24, value=8)
  exercise = st.number_input("Exercise Minutes (today)", min_value=0, max_value=180, value=30)
  caffeine = st.number_input("Caffeine Intake (mg)", min_value=0, max_value=1000, value=100)
  input_features = np.array([[sleep, work, exercise, caffeine]])
  if st.button("percentage of stress"):
    predicted_stress = model.predict(input_features)
    if prediction[0] == 1:
      st.error("You are likely stressed. Consider taking a break or relaxing.")
    else:
      st.success("You are likely not stressed. Keep it up!")
