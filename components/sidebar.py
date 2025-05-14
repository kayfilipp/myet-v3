from models.User import User

def render(st):

    user: User = st.session_state.get('User')

    if not user:
        return 

    # add a logout button to the sidebar
    with st.sidebar:
        st.markdown(f"<p style='no-ref'>Logged in with {user.email}<p>", unsafe_allow_html=True)
        if st.button("🔓 Logout"):
            st.logout()

        # st.caption(user.__repr__())