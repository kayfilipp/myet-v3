import streamlit as st 
from models.AssessmentScore import AssessmentScore
from components import results

score : AssessmentScore = st.session_state.get('view_score')


st.page_link("./app/app.py", label="Back")

if score.results:
    results.render(st, score.results)