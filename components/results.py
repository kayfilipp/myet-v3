from components import trait_descriptions, score_chart
import asyncio 
import streamlit 

def render(st: streamlit, assessment_score, enable_management=True):

    results = assessment_score.results

    st.subheader("You are: The Worker Bee")
    c = st.columns([2,2,8], gap='medium')
    with c[0]:
        st.image("./assets/workerbee.png")
    with c[1]:
        st.write("You do stuff!")

    c = st.columns([1.5,2.5,6])

    with c[0]:
        st.subheader("Your Scores")
        st.caption("Here's how you did.")
        st.dataframe(results, use_container_width=True, column_config={"value": 'score'})

    with c[1]:
        st.subheader("Visual Breakdown")
        st.caption("Who doesn't like pictures?")
        score_chart.render(st, results)

    with c[2]:
        st.subheader("Understanding your Results")
        trait_descriptions.render(st)

    st.divider()

    if not enable_management:
        # don't let the user share / delete / edit etc
        return 

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
        
