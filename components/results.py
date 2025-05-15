from components import trait_descriptions, score_chart
from models.Personality import *
import asyncio 
import streamlit 
import json

def get_personality(st, assessment_score):

    if not st.session_state.get('personality_picker'):

        personalities = json.load(open("personalities.json"))['personalities']
        personalities = [Personality(**personality) for personality in personalities]
        st.session_state['personality_picker'] = PersonalityPicker(personalities)

    picker : PersonalityPicker = st.session_state['personality_picker']
    results = assessment_score.results

    return picker.get_personality_match(results)['personality']



def render(st: streamlit, assessment_score, enable_management=True):

    # PERSONA PICKER 
    persona : Personality = get_personality(st, assessment_score)

    results = assessment_score.results

    c = st.columns([2,2.5,2, 8], gap='medium')
    with c[0]:
        st.subheader(persona.name)
        st.caption(persona.description)
        st.image(persona.image_path)

    with c[1]:
        st.subheader("Your Scores")
        st.caption("Here's how you did.")
        st.dataframe(results, use_container_width=True, column_config={"value": 'score'})

    with c[2]:
        st.subheader("Visual Breakdown")
        st.caption("Who doesn't like pictures?")
        score_chart.render(st, results)

    c = st.columns([4.5, 8])

    with c[0]:
        st.subheader("About You")
        st.write(persona.description)

    st.divider()

    c = st.columns(2)

    with c[0]:
        st.subheader("Understanding your Results")
        trait_descriptions.render(st)

    with c[1]:

        if not enable_management:
            # don't let the user share / delete / edit etc
            return 

        st.subheader("Manage Your Score")

        # SHARE SCORE
        if assessment_score.saved:
            
            st.text_input(label="enter one or more emails separated by a comma to share this result with others.", key="share_emails")
            if st.button("Share Results", use_container_width=True):
                asyncio.run(assessment_score.share(st.session_state['share_emails']))
                st.caption("Shared!")

            # DELETE SCORE
            if st.button("Remove From Saved", use_container_width=True):
                assessment_score.saved = False
                asyncio.run(assessment_score.delete())
                st.rerun()
        
        # SAVE SCORE
        else:

            if st.button("Save This Score", use_container_width=True, type="primary"):
                assessment_score.saved = True # <- speed up loading time
                asyncio.run(assessment_score.save())
                st.rerun()
            
