import streamlit as st

st.title("Welcome to your MYET Account!")
user = st.experimental_user

if not user["email_verified"]:
    st.warning("Please verify your email and login back to unlock all features")

st.divider()


st.subheader(user.name)
st.image(user.get("picture", ".\assets\default_profile.jpg"))
st.page_link("./app/quiz.py", label="Take Assessment")