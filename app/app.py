import streamlit as st
from models.User import User 
from components import results

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

    # show score if the user has selected one, otherwise display all scores.
    # really got find an alt to this.

    view_score = st.session_state.get('view_score')

    if view_score:
        if st.button("Back"):
            del st.session_state['view_score']
            del st.session_state['enable_management']
            st.rerun()

        results.render(st, view_score, st.session_state['enable_management'])
        st.stop()

    with st.expander("Your Previous Scores", expanded=True):
        for score in user.assessment_scores:

            if st.button("View", key=score.id):
                st.session_state['view_score'] = score 
                st.session_state['enable_management'] = True
                st.rerun()

            st.dataframe([score.results])
            st.caption(f"taken on {score.created_date.strftime("%Y-%m-%d %H:%M")}")


    if not user.shared_scores:
        user.get_shared_scores()

    st.write(len(user.shared_scores))

    with st.expander("Scores Shared With You", expanded=True):
        for score in user.shared_scores:

            if st.button("View", key=score.id):
                st.session_state['view_score'] = score 
                st.session_state['enable_management'] = False
                st.rerun()

            st.dataframe([score.results])
            st.caption(f"taken on {score.created_date.strftime("%Y-%m-%d %H:%M")}")


