import streamlit as st
from models.Profile import Profile 

st.title("Welcome to your MYET Account!")
user = st.session_state['User']

if not user["email_verified"]:
    st.warning("Please verify your email and login back to unlock all features")

st.divider()


st.subheader(user.name)
st.image(user.get("picture", ".\assets\default_profile.jpg"))
st.page_link("./app/quiz.py", label="Take Assessment")

st.divider()

profile = Profile(user)
profile.get_assessment_history()

st.subheader("Your Previous Assessments")
st.dataframe(profile.assessments)