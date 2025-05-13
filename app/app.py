import streamlit as st
from models.Profile import Profile 

st.title("Welcome to your MYET Account!")
user = st.session_state['User']

if not st.experimental_user["email_verified"]:
    st.warning("Please verify your email and login back to unlock all features")

st.divider()


st.subheader(user.name)
st.image(st.experimental_user.get("picture", ".\assets\default_profile.jpg"))
st.page_link("./app/quiz.py", label="Take Assessment")

st.divider()

if user.id:

    profile = st.session_state['profile']
    profile.get_assessment_history()

    st.subheader("Your Previous Assessments")
    if len(profile.assessments)>0:
        for assessment in profile.assessments:
            id = str(assessment['id'])
            date_of = assessment['created_date']

            st.link_button(label=id, url=f"/quiz?assessment_id={id}")
            st.caption(f"Taken on {date_of}")
    else:
        st.caption("You have not taken any assessments.")