import streamlit as st
from models.User import User 
import asyncio 
from datetime import datetime 

st.title("Welcome to your MYET Account!")
user : User = st.session_state['User']

if not st.experimental_user["email_verified"]:
    st.warning("Please verify your email and login back to unlock all features")

st.divider()


st.subheader(user.name)
st.image(st.experimental_user.get("picture", ".\assets\default_profile.jpg"))
st.page_link("./app/quiz.py", label="Take Assessment")

st.divider()

if user.id:

    if not user.assessment_scores:
        user.get_scores()

    with st.expander("Your Previous Scores"):
        for score in user.assessment_scores:

            if st.button("View", key=score.id):
                st.session_state['view_score'] = score 
                st.switch_page("./app/result.py")
            st.dataframe([score.results])
            st.caption(f"taken on {score.created_date.strftime("%Y-%m-%d %H:%M")}")

