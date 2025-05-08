from models.Assessment import Assessment
import streamlit 

def render(st: streamlit):
    st.subheader("MYET Assessment")
    st.caption("See your score, share with others, and save for later.")
    st.divider()

    if not st.session_state.get('assessment'):
        st.session_state['assessment'] = Assessment(
            user=st.session_state['user'], 
            limit=None, 
            chunk_size=st.session_state['questions_chunk_size'])

    assessment = st.session_state.get('assessment')

    # if assessment completed, print some stuff out 
    if assessment.completed:
        st.subheader("Nice Job!")
        st.caption("Here's how you did.")
        
        st.dataframe(assessment.results, use_container_width=False)

    elif not assessment.started:

        num_questions = len(assessment.questions)
        st.text(f"This assessment will consist of {num_questions} questions. Please do not refresh or close the page.")        
        st.button("Start", on_click=assessment.start)

    else:

        # the only other option is that the assessment hasn't been completed.
        st.caption("1 = Strongly Disagree, 5 = Strongly Agree")
        render_questions(st, assessment)


def answer_question(st, assessment: Assessment, id, state_key):
    assessment.answer_question(id=id, answer=st.session_state[state_key])


def render_questions(st: streamlit, assessment: Assessment):
    
    options = list(range(0,6))

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

        if st.button("⬅️", disabled=(not assessment.has_previous)):
            assessment.last_n()
            st.rerun()

    with _c[1]:

        if not assessment.has_next:
            if st.button("Submit", disabled=(incomplete)):
                assessment.submit()
                st.rerun()
        else:
            if st.button("➡️", disabled=(incomplete)):
                assessment.next_n()
                st.rerun()





# def display_question_input(st: streamlit, assessment):

#     question = assessment.current_question

#     st.radio(question.body,options=range(1,6), horizontal=True, label_visibility="visible", index=None, key="current_question_answer")
#     answer = st.session_state.get('current_question_answer')

