import streamlit as st 
from models.Assessment import Assessment
from random import randint
from components import results
import asyncio 
import json 

def progress_bar(st, assessment: Assessment):
    progress = len(assessment.answered_questions) / ( len(assessment.answered_questions) + len(assessment.questions) )
    st.progress(progress, "Asessment Progress")

def answer_question(st, assessment: Assessment, id, state_key):
    assessment.answer_question(id=id, answer=st.session_state[state_key])

def render_questions(st, assessment: Assessment):
    
    options = list(range(1,9))

    for question in assessment.current_questions:
        
        # on value change, answer each question in the queue by searching it up via id.
        st.radio(
            label=question.body, 
            options=options, 
            horizontal=True, 
            # if we've answered the question before, show the last answer we submitted. leave blank otherwise.
            index=options.index(question.answer) if question.answer else None, 
            key=question.id, 
            on_change=answer_question, 
            args=(st, assessment, question.id, question.id)
        )

    incomplete = any([question.answer is None for question in assessment.current_questions])

    _c = st.columns([1.2,1.2,8])
    
    with _c[0]:

        if st.button("", icon=":material/arrow_back_ios:", disabled=(not assessment.has_previous)):
            assessment.last_n()
            st.rerun()

    with _c[1]:

        if not assessment.has_next:
            if st.button("submit", icon=":material/check:", disabled=(incomplete)):
                assessment.submit()
                st.rerun()
        else:
            if st.button("", icon=":material/arrow_forward_ios:", disabled=(incomplete)):
                assessment.next_n()
                st.rerun()

def render_assessment_score_radial_chart(st, scores: dict):
    pass


st.title("The MYET Assessment")
st.caption("Discover your strengths and share them with others.")
st.divider()

user = st.session_state['User']
# ***************************************************************IF NO ASSESSMENT ID IS PROVIDED*************************************************************************************** #
if not st.session_state.get('assessment'):
    st.session_state['assessment'] = Assessment(
        user=user, 
        limit=None, 
        chunk_size=st.secrets['questions_chunk_size'])
    
assessment : Assessment = st.session_state['assessment']

if assessment.completed:
    results.render(st, assessment.assessment_score)

    # RESTART ASSESSMENT
    if st.button("Take Test Again", use_container_width=True):
        del st.session_state['assessment']
        st.switch_page("./app/quiz.py")
        st.rerun()

    # SAVE SCORE
    if not assessment.assessment_score.saved:
        if st.button("Save This Score", use_container_width=True):
            assessment.assessment_score.saved = True # <- speed up loading time
            asyncio.run(assessment.assessment_score.save())
            st.rerun()
    else:
        
        # DELETE SCORE
        if st.button("Unsave", use_container_width=True):
            assessment.assessment_score.saved = False
            asyncio.run(assessment.assessment_score.delete())
            st.rerun()

elif assessment.started:

    with st.popover("Quit"):
        st.caption("Are you sure? All progress will be lost.")
        if st.button("Yes"):
            del st.session_state['assessment']
            st.rerun()

    progress_bar(st, assessment)
    render_questions(st, assessment)
    st.caption("1 = Strongly Disagree, 4 = Neutral, 8 = Strongly Agree")

else:

    num_questions = len(assessment.questions)
    st.text(f"This assessment will consist of {num_questions} questions. Feel free to explore our website and take breaks - your progress will be saved.")        
    st.button("Start", on_click=assessment.start)

    # add a demo button because I'm lazy.
    if st.button("Demo"):
        st.session_state['demo'] = True 
        for question in assessment.questions:
            question.answer = randint(1,8)
        assessment.answered_questions = assessment.questions
        assessment.questions = []
        assessment.submit()
        st.rerun()

